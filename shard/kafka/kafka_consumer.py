from shard.utils.logger import log_event
from confluent_kafka import Consumer, KafkaException
import json
from typing import Any

class KafkaConsumer:
    def __init__(self, topic:str, grup_id:str, bootstrap_servers:str = "localhost:9092") -> None:
        self.consumer_conf = {
            "bootstrap.servers":bootstrap_servers,
            "group.id":grup_id, 
            "auto.offset.reset": "earliest",
            "enable.auto.commit": True}
        
        try:
            self.consumer = Consumer(self.consumer_conf)
            self.consumer.subscribe([topic])
            log_event("INFO", F"kafka consumer subscribe to {topic} topic")

        except KafkaException as e:
            log_event("ERROR", f"{e}")
            print(e)
            raise
    

    def consume_to_message(self)-> Any:
        try:
            while True:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    log_event("ERROR", f"error in msg {msg.error()}")
                    continue

                key = json.loads(msg.key().decode('utf-8')) if msg.key() else None # type: ignore
                value = json.loads(msg.value().decode('utf-8')) if msg.value() else None # type: ignore
                

                return key,value
        except Exception as e:
            log_event("ERROR", F"{e}")
            print(e)

    def close_consumer(self):
        self.consumer.close()