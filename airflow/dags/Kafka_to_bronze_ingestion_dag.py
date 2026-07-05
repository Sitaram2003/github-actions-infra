from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import yaml

TOPIC_CONFIG_PATH = "/opt/airflow/CustomFunctions/utils/topics_conf.yaml"

with open(TOPIC_CONFIG_PATH,"r") as file:
    config = yaml.safe_load(file)
topic_config = config["topics"]

for topic_cfg in topic_config:

    topic = topic_cfg['topic'].split(".")[2]

    dag_id = f"{topic}_data_bronze_ingestion"

    dag = DAG(
        dag_id = dag_id,
        schedule='@daily',
        start_date = datetime(2024,1,1),
        end_date = None,
        catchup=False,
        default_args={
            'owner':'airflow',
            'retries':2,
            'retry_delay':timedelta(minutes=1)
        }
    )

    with dag:

        task1 = BashOperator(
            task_id = "Kafka_to_bronze",
            bash_command=f"""
                spark-submit --master spark://spark-master:7077 \
                --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
                --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension \
                --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog \
                /opt/airflow/jobs/bronze/kafka_to_bronze_streams.py \
                {topic_cfg['topic']} \
                {topic_cfg['output_path']} \
                {topic_cfg['checkpoint_path']}
            """
        )

        task1

    globals()[dag_id] = dag

        

