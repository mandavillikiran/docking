FROM jupyter/pyspark-notebook
ADD spark-submit.sh .
USER root
RUN chmod 777 ./spark-submit.sh
ADD consumer.py .
CMD ["./spark-submit.sh"]
