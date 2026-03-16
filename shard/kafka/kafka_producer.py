from shard.utils.logger import *

from confluent_kafka import Producer , KafkaException
import socket



class KafkaProducer:
    def __init__(self, bootstrap_servers:str = 'localhost:9092' ) -> None:
        self.conf = {
                'bootstrap.servers': bootstrap_servers, 
                'client.id':socket.gethostname()
                }
        
        try:
            self.producer :Producer = Producer(self.conf)
            log_event("INFO", "kafka DEBUG create")
        except KafkaException as e:
            log_event("ERROR", f"failed to create kafka producer: {e}")
            raise

    def kafka_colbak(self, err, msg):
        if err is not None:
            log_event("ERROR", f"failed to deliver msg: {str(msg)} the error:{str(err)}")
        else:
            log_event("INFO",f"masege product {str(msg)}")
    

        
    def produce(self, topic:str, kay:str, value:str):
        try:
            byts_kay = kay.encode()
            byts_value = value.encode()

            self.producer.produce(
                topic=topic,
                key=byts_kay,
                value= byts_value,
                callback=self.kafka_colbak
            )
            self.producer.poll(0)

        except Exception as e:
            log_event("ERROR", "Failed to send message to Kafka... error: {e}")

            
    def close_kafka_producer(self):
        self.producer.flush()
        log_event("INFO", "close_kafka_producer!")
