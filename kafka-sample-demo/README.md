# KAFKA Sample Demo
This is a simple app that demonstrates how to use KAFKA to send and receive messages.

## Setting up Kafka Manually
1. https://kafka.apache.org/quickstart

### Create a topic
1. `bin/kafka-topics.sh --create --topic items --botstrap-server localhost:9092`

### Read events (Manually) from the Kafka topic (Consumer)
1. `bin/kafka-console-consumer.sh --topic items --from-beginning --bootstrap-server localhost:9092`

### Write events (Manually) to the Kafka topic (Producer)
1. `bin/kafka-console-producer.sh --topic items --bootstrap-server localhost:9092`
2. You will be on an interface where you can type a message and press enter.
3. You should see the message you typed in the consumer terminal.

## Using Kafka with Python
For this make sure to still have the Kafka server and zookerper running.

#### Start the Kafka broker service
`bin/zookeeper-server-start.sh config/zookeeper.properties`

#### Start the ZooKeeper service
`bin/kafka-server-start.sh config/server.properties`

### Running the Consumer (Server)
1. Run the consumer: `python consumer.py`

### Running the Producer (Client)
1. Run the producer: `python producer.py`

