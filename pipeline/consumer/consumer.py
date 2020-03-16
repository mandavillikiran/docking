from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import logging
import time

spark = (
        SparkSession 
        .builder 
        .appName("Prices Consumer") 
        .getOrCreate()
        )

# Default the logging level to ERROR
logger = spark._jvm.org.apache.log4j
logger.LogManager.getLogger("org"). setLevel( logger.Level.ERROR )
logger.LogManager.getLogger("akka").setLevel( logger.Level.ERROR )


df = (spark 
      .readStream 
      .format("kafka")
      .option("kafka.bootstrap.servers", "kafka:9092") 
      .option("subscribe", "prices-topic")
      # load data into spark-structured streaming from Kafka topic
      .load()
      
      ### TODO complete app
      
      ### select only the value and timestamp fields
      
      ### transform the the data into a structured data stream
      #### deserialize the values
      #### add schema
      
      ## Can we add a recovery mechanism in case the app stops working? 

      ## how could we deal with data lateness?

      ## Can we calculate the average price by match?
      )

# Print output
query = (df.writeStream 
            .outputMode("complete") 
            .format("console") 
            .start()
        )

query.awaitTermination()            
