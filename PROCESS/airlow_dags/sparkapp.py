from pyspark.sql import SparkSession
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime, timedelta


target_date = (datetime.now() - timedelta(days=1)).date()

engine = create_engine('mysql+pymysql:/회원db')


query = "SELECT 회원상담내용 as 문장 from 상담내용"
df_pandas = pd.read_sql(query, engine)


spark = SparkSession.builder.appName("sparkapp").getOrCreate()


df_spark = spark.createDataFrame(df_pandas)


df_spark.write.csv(f"/home/big/temp/sql_{target_date}.csv", header=True)


spark.stop()

