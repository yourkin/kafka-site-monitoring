import json

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["kafka:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


class SendData:
    @staticmethod
    def send_data(topic, data):
        producer.send(topic, data)
