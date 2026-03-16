from shard.kafka.kafka_consumer import KafkaConsumer
from shard.kafka.kafka_producer import KafkaProducer
from shard.database.mongodb_connection import MongoManager
from shard.scema.pydentic_clases import IntelMesege
from shard.utils.haversine import haversine_km
import json
from shard.utils.logger import log_event

class ManagerServiceA:
    def __init__(self,producer:KafkaProducer, consumer:KafkaConsumer, database:MongoManager) -> None:
        self.producer = producer
        self.consumer = consumer
        self.database = database
    



    def listening_to_data(self):
        while True:
            massege = self.consumer.consume_to_message()
            
            try:
                massege_value = json.loads(massege[1])
                data_obg = IntelMesege(**massege_value)
                dict_data = data_obg.model_dump()

                # At this stage, a check must be performed against the database!
                # self.database.get_document_by_query({})
                self.database.insert_document(dict_data)

            # If the message did not pass validation
            except Exception as e:
                error_meseg = {
                    "Cause_of_the_error":e,
                    "meseg":massege[1]
                }
                str_error_meseg = json.dumps(error_meseg)
                self.producer.produce(topic="intel_signals_dlq",kay="abnormal", value=str_error_meseg)
            
