from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import time
from bs4 import BeautifulSoup
import random
import pandas as pd

import json
from airflow import DAG
from pendulum import yesterday
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

dag = DAG(
	dag_id="crawling",
	schedule_interval="@daily",
	start_date=yesterday("Asia/Seoul"),
	catchup=False
)



##############################디시인사이드 실시간베스트게시판 댓글크롤링#######################################################
def python_task():
    sleep_time = random.randint(3,5)
    time.sleep(sleep_time)

    # Selenium 설정
    options = webdriver.ChromeOptions()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0"
    options.add_argument('user-agent=' + user_agent)
    ser = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=ser, options=options)

    # 기본 URL
    BASE = "http://gall.dcinside.com"
    yesterday = (datetime.now() - timedelta(days=1)).date()
    comments = []  

    start_page = 1
    Flag = True

    while Flag:
        base_url = BASE + '/board/lists/?id=dcbest&page=' + str(start_page) + '&_dcbest=1'
        time.sleep(sleep_time)

        try:
            driver.get(base_url)
            time.sleep(sleep_time)
        except:
            time.sleep(sleep_time)
            continue


        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        article_list = soup.find(class_='listwrap2').find_all('tr')

        for article in article_list:
            try:
                date_str = article.find("td", {"class": "gall_date"})['title']
                contents_date = datetime.strptime(date_str[:10], "%Y-%m-%d").date()

                head = article.find('td', {"class": "gall_num"}).text

                if head not in ['설문', 'AD', '공지'] :
                    if contents_date == yesterday:
                        tag = article.find('a', href=True)
                        content_url = BASE + tag['href']

                        driver.get(content_url)
                        time.sleep(sleep_time)
                        contents_soup = BeautifulSoup(driver.page_source, "html.parser")

                        last_page = int(contents_soup.find("div", class_="cmt_paging").find_all("a")[-1].text)

                        for page_number in range(1, last_page + 1):
                            if page_number > 1:
                                driver.get(f"{content_url}&cpage={page_number}")
                                time.sleep(sleep_time)

                            contents_soup = BeautifulSoup(driver.page_source, "html.parser")
                            reply_comments = contents_soup.find_all("p", class_="usertxt ub-word")
                            for comment in reply_comments:
                                comments.append(comment.text.strip())
                    elif contents_date < yesterday:
                        Flag=False
                        break

            except:
                continue

        start_page += 1
        if not Flag:
            break

    df_comments = pd.DataFrame(comments, columns=['문장'])
    df_comments.to_csv(f'/home/big/temp/{yesterday}.csv', index=False, encoding='utf-8')

    driver.quit()


####################################################################################################

crawling = PythonOperator(
	task_id="crawling",
	python_callable=python_task,
	dag=dag
)

target_date = (datetime.now() - timedelta(days=1)).date()


exists = FileSensor(
	task_id="exists",
	filepath= f"/home/big/temp/{target_date}.csv",
	poke_interval=30,
    fs_conn_id='fs_default',
	dag=dag
)

upload = BashOperator(
    task_id="upload",
    bash_command=f'hdfs dfs -put /home/big/temp/{target_date}.csv /crawling/{target_date}.csv',
    dag=dag
)

crawling >> exists >> upload

