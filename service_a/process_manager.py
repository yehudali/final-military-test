from shard.kafka.kafka_consumer import KafkaConsumer
from shard.database.mongodb_connection import MongoManager

class ManagerServiceA:
    def __init__(self, consumer:KafkaConsumer, database:MongoManager) -> None:
        self.consumer = consumer
        self.database = database
    



    def listening_to_data(self):
        while True:
            data = self.consumer.consume_to_message()
            
            print(data)