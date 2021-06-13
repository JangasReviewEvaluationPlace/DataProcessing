from confluent_kafka.avro import AvroConsumer
from typing import Callable

import configs


class KafkaConsumer:
    def __init__(self):
        # Stop flag is mostly used for test purposes.
        # This class is using an infinity while loop with an callback inside.
        # The stop flag can be raised any time for comming out of that method.
        self.stop = False

    def __enter__(self):
        self.consumer = AvroConsumer({
            "bootstrap.servers": configs.KAFKA_BOOTSTRAP_SERVER,
            "group.id": configs.KAFKA_CONSUMER_GROUP_ID,
            "schema.registry.url": configs.KAFKA_SCHEMA_REGISTRY_URL,
            "auto.offset.reset": configs.KAFKA_AUTO_OFFSET_RESET
        })
        return self

    def __exit__(self, *args, **kwargs):
        self.consumer.close()

    def consume_topic(self, topic: str, message_processing: Callable):
        self.consumer.subscribe(topics=[topic])
        while not self.stop:
            message = self.consumer.poll(timeout=250)
            if message:
                message_processing(message)
                self.consumer.commit()

    def stop_consuming(self):
        self.stop = True
