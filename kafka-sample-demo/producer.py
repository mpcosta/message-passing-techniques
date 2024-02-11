from kafka import KafkaProducer

TOPIC_NAME = 'items'
KAKFA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAKFA_SERVER)

producer.send(TOPIC_NAME, b'Hello, Kafka!')
producer.flush()