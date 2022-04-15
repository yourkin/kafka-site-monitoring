import json

from kafka import KafkaConsumer

import db

consumer = KafkaConsumer(
    "users",
    group_id="my-group",
    bootstrap_servers=["kafka:9092"],
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)
writer = db.Writer()
writer._create_table()


def read_stream():
    """
    Reads Kafka stream.
    """
    for message in consumer:
        print(message.key, message.value, message.offset)
