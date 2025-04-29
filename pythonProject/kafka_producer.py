#
from kafka import KafkaProducer

producer = KafkaProducer(boostrap_servers='localhost:9092')

topic = 'chats'
message = b'Hello Kafka'
producer.send(topic, message)