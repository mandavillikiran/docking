## Requirements
docker-compose version 1.25.4+
docker 18.09.6+

## Operating the Pipeline

#### to build the containers
`docker-compose build`

#### to start the containers
`docker-compose up -d`

#### to print the logs for the consumer
`docker-compose logs -f consumer`
`docker-compose logs -f producer`

#### to stop the containers
`docker-compose down`


How could we keep the producer from crashing when the Kafka topic is not ready?
