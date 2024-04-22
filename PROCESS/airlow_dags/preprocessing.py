import os
import pandas as pd

import re
import emoji
from datetime import datetime, timedelta
from konlpy.tag import Okt
from soynlp.normalizer import repeat_normalize

import json
from airflow import DAG
from pendulum import yesterday
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.external_task_sensor import ExternalTaskSensor

dag = DAG(
	dag_id="preprocessing",
	schedule_interval="@daily",
	start_date=yesterday("Asia/Seoul"),
	catchup=False
)

wait_for_crawling = ExternalTaskSensor(
    task_id='wait_for_crawling',
    external_dag_id='crawling',  # 대상 DAG ID
    external_task_id=None,  
    check_existence=True,
    timeout=4000,
    dag=dag,
)

target_date = (datetime.now() - timedelta(days=1)).date()
###################################################################################################################

def python_task():

    # 정규 표현식 패턴
    pattern = re.compile(f'[^ .,?!/@%~％·∼()\x00-\x7Fㄱ-ㅣ가-힣>]+')
    url_pattern = re.compile(
        r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')

    # 중복된 문자 제거 함수
    def remove_repeated(word):
        cleaned_text = re.sub(r'(ㅋ+|ㅎ+|ㅜ+|ㅠ+|ㅇㅇ+|ㅡ+|ㅉ+|>+|\b(?!18|28)\d+\b)', '', word)
        return cleaned_text

    # 텍스트 정제 함수
    def clean_and_remove_repeated(x):
        x = pattern.sub(' ', x)  # 정규 표현식에 해당하지 않는 문자 제거
        x = emoji.replace_emoji(x, replace='')  # 이모지 삭제
        x = url_pattern.sub('', x)  # URL 제거
        x = x.strip()
        x = remove_repeated(x)  # 중복 문자 제거
        x = repeat_normalize(x, num_repeats=2)
        return x
    # J 욕설 사전 불러오기
    with open('/home/big/Documents/swear_list.json', 'r', encoding='utf-8') as file:
        profanity_dict = json.load(file)["욕설"]

    # KoNLPy의 Okt 형태소 분석기 인스턴스화
    okt = Okt()

    # 문장을 토큰화하고 태깅하는 함수
    def tag_profanity_ko(sentence):
        tokens = okt.morphs(sentence)
        tags = [ 'B' if token in profanity_dict else 'O' for token in tokens]
        return list(zip(tokens, tags))


    def process_dataframe(df):
        df['content'] = df['문장'].apply(clean_and_remove_repeated)
        df['content'] = df['문장'].apply(tag_profanity_ko)
        df = df[['content']]
        return df


    # CSV 파일이 있는 디렉토리 경로
    directory_path = '/home/big/temp'

    # 디렉토리 내 모든 CSV 파일 목록 가져오기
    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

    # 모든 CSV 파일을 DataFrame으로 불러와 리스트에 저장
    dataframes = []
    for file in csv_files:
        file_path = os.path.join(directory_path, file)
        df = pd.read_csv(file_path, encoding="utf-8")
        dataframes.append(df)

    # 모든 DataFrame을 하나로 합치기
    df_combined = pd.concat(dataframes, ignore_index=True)

    # 데이터프레임 처리
    df_processed = process_dataframe(df_combined)

    df_processed.to_csv(f'/home/big/processing/pre_{target_date}.csv', index=False, encoding='utf-8')  

############################################################################################################

preprocessing = PythonOperator(
	task_id="preprocessing",
	python_callable=python_task,
	dag=dag
)

exists = FileSensor(
	task_id="exists",
	filepath=f'/home/big/processing/pre_{target_date}.csv',
	poke_interval=30,
	dag=dag
)


upload=BashOperator(
	task_id="upload",
	bash_command=f'hdfs dfs -put /home/big/processing/pre_{target_date}.csv /processing/pre_{target_date}.csv',
	dag=dag
)

exists >>   wait_for_crawling >> preprocessing >> upload

