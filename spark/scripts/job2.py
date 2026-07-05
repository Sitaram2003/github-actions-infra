from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, to_date
import sys

topic = sys.argv[1]
output_path = sys.argv[2]
checkpoint_path = sys.argv[3]


spark = SparkSession.builder.appName("Orders-Bronze-Ingestion").getOrCreate()

df = ( 
    spark
    .readStream
    .format('kafka')
    .option("kafka.bootstrap.servers","kafka:29092")
    .option("subscribe", topic)
    .option("startingOffsets","earliest")
    .load()
)

query = (
    df
    .writeStream
    .format('parquet')
    .option("checkpointLocation", checkpoint_path)
    .option("path", output_path)
    .partitionBy("ingestion_date")
    .outputMode('append')
    .start()
)

query.awaitTermination()