FROM apache/spark:3.5.1

USER root

ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

WORKDIR /opt/spark/jars

# ==============================
# Kafka (Spark + Client)
# ==============================
RUN curl -fLO https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.1/spark-sql-kafka-0-10_2.12-3.5.1.jar \
 && curl -fLO https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.5.1/kafka-clients-3.5.1.jar

RUN curl -L -o /opt/spark/jars/spark-token-provider-kafka-0-10_2.12-3.5.1.jar \
https://repo1.maven.org/maven2/org/apache/spark/spark-token-provider-kafka-0-10_2.12/3.5.1/spark-token-provider-kafka-0-10_2.12-3.5.1.jar

RUN curl -fLO https://repo1.maven.org/maven2/org/apache/commons/commons-pool2/2.11.1/commons-pool2-2.11.1.jar

# ==============================
# S3 / MinIO (Hadoop AWS)
# ==============================
RUN curl -fLO https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar \
 && curl -fLO https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.540/aws-java-sdk-bundle-1.12.540.jar

# # ==============================
# # Delta Lake (Spark 3.5)
# # ==============================
# RUN curl -fLO https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.1.0/delta-spark_2.12-3.1.0.jar \
#  && curl -fLO https://repo1.maven.org/maven2/io/delta/delta-storage/3.1.0/delta-storage-3.1.0.jar

# ==============================
# JDBC Drivers
# ==============================

# PostgreSQL
RUN curl -fLO https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.2/postgresql-42.7.2.jar

RUN curl -fLO https://jdbc.postgresql.org/download/postgresql-42.7.3.jar


# MySQL
RUN curl -fLO https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.3.0/mysql-connector-j-8.3.0.jar

# SQL Server (Java 11 compatible)
RUN curl -fLO https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/12.6.1.jre11/mssql-jdbc-12.6.1.jre11.jar

# ==============================
# Snowflake
# ==============================

# Snowflake JDBC
RUN curl -fLO https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/3.15.1/snowflake-jdbc-3.15.1.jar

# Spark-Snowflake connector (best available for Spark 3.x)
RUN curl -fLO https://repo1.maven.org/maven2/net/snowflake/spark-snowflake_2.12/2.13.0-spark_3.4/spark-snowflake_2.12-2.13.0-spark_3.4.jar

# ==============================
# Permissions
# ==============================
COPY scripts/* /opt/spark/

RUN chmod 644 *.jar && chown spark:spark *.jar

USER spark
