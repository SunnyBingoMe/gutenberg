SPARK_HOME="" HADOOP_HOME="" YARN_HOME="" SPARK_JAR="" HADOOP_COMMON_LIB_NATIVE_DIR="" HADOOP_HDFS_HOME="" HADOOP_COMMON_HOME="" HADOOP_OPTS="" YARN_CONF_DIR="" HADOOP_MAPRED_HOME="" PYSPARK_PYTHON=/usr/bin/python3 PYSPARK_DRIVER_PYTHON="jupyter" PYSPARK_DRIVER_PYTHON_OPTS="notebook --allow-root --no-browser --port 8888 " /root/spark/bin/pyspark --master spark://$SPARK_MASTER_HOST:7077 --driver-memory 2g
