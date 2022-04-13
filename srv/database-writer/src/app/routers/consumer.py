from fastapi import APIRouter
from kafka import KafkaConsumer

router = APIRouter()

consumer = KafkaConsumer("users", group_id="my-group", bootstrap_servers=["kafka:9092"], auto_offset_reset='earliest')


@router.get("/read-stream")
async def read_stream():
    """
    Reads Kafka stream.
    """
    for message in consumer:
        print(message.key, message.value, message.offset)
    return None