from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()
spark.read.csv("/C:/Users/NITHIN DEEPAK/Desktop/new_testing/data/source_csv/accounts.csv").show() 
import sys
import pyspark
import pytest
import pandas as pd
print("Python:", sys.version)
print("Executable:", sys.executable)
print("PySpark:", pyspark.__version__)
print("pytest:", pytest.__version__)

def reader_func(format, path):
    if format == "csv":
        return spark.read.csv(path, header=True, inferSchema=False)
    elif format == "parquet":
        return spark.read.parquet(path)
    else:
        raise ValueError(f"Unsupported format: {format}")

df_accounts = reader_func("csv", "/C:/Users/NITHIN DEEPAK/Desktop/new_testing/data/source_csv/accounts.csv")
df_transactions = reader_func("csv", "/C:/Users/NITHIN DEEPAK/Desktop/new_testing/data/source_csv/transactions.csv")
df_customers = reader_func("csv", "/C:/Users/NITHIN DEEPAK/Desktop/new_testing/data/source_csv/customers.csv")

df_joined=df_accounts.join(df_transactions, df_accounts.account_number == df_transactions.account_number, "inner")
df_final=df_joined.filter(df_joined.status.isin("success","POSTED"))\
    .withColumn("processing_fee", df_joined.amount * 0.02) \
    .orderBy(df_joined.amount, ascending=False)

df_pandas = df_final.toPandas()

# Check the type
print(type(df_pandas))

from pathlib import Path

output_path = Path(
    r"C:\Users\NITHIN DEEPAK\Desktop\new_testing\data\output_csv"
)

output_path.mkdir(parents=True, exist_ok=True)

df_pandas.to_csv(
    output_path / "processed_transactions.csv",
    index=False
)
df_pandas.show()