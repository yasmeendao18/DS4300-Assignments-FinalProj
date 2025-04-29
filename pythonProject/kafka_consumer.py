from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='localhost:9092')

for message in consumer:
    print(f"Received message: {message.value}")

    consumer.close()