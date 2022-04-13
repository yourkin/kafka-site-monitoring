from kafka import KafkaConsumer

consumer = KafkaConsumer("users", group_id="my-group", bootstrap_servers=["kafka:9092"])


def read_stream():
    """
    Reads Kafka stream.
    """
    for message in consumer:
        print(message.key, message.value, message.offset)