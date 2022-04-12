from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=["kafka:9092"])


class SendData:

    @staticmethod
    def send_data(topic):
        producer.send(topic, key=b"testing", value=b"hello")