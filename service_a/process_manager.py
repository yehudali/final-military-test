from shard.kafka.kafka_consumer import KafkaConsumer
from shard.database.mongodb_connection import MongoManager

class ManagerServiceA:
    def __init__(self, consumer:KafkaConsumer, database:MongoManager) -> None:
        pass