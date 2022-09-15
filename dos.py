# librerias
import requests
import json
import pandas as pd
from pyspark.sql import SparkSession

# traer info de la api
r = requests.get('https://api.publicapis.org/entries')
a = json.loads(r.text)

# cargar dato en dataframe
pandas_df = pd.DataFrame(data=a['entries'])

# pyspark
spark = SparkSession.builder.getOrCreate()
df = spark.createDataFrame(pandas_df)
df.show()
df.printSchema()
df.select('API','Description').show()
