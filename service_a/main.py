from shard.config import ServiseAConfig
from shard.kafka.kafka_consumer import KafkaConsumer
from shard.kafka.kafka_producer import KafkaProducer
from shard.database.mongodb_connection import MongoManager


from service_a.process_manager import ManagerServiceA

def run():
    config = ServiseAConfig()
    producer = KafkaProducer(bootstrap_servers=config.BOOTSTRAP_SERVERS)
    consumer = KafkaConsumer("intel",'service_a', config.BOOTSTRAP_SERVERS)
    db = MongoManager(db_name="bank_goals", collection_name="i" , mongo_uri=config.MONGO_URL)



    ManagerServiceA(producer,consumer,db)
    





if __name__=="__main__":
    run()