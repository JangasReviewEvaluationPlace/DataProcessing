from confluent_kafka.avro import AvroConsumer


class KafkaConsumer:
    def __init__(self):
        self.stop = False

    def __enter__(self):
        self.consumer = AvroConsumer({
            "bootstrap.servers": "localhost:9092",
            "group.id": "pythonprocessing",
            "schema.registry.url": "http://localhost:8081",
            "auto.offset.reset": "earliest"
        })
        # value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        return self

    def __exit__(self, *args, **kwargs):
        self.consumer.close()

    def consume_topic(self, topic: str):
        self.consumer.subscribe(topics=[topic])
        while not self.stop:
            message = self.consumer.poll(timeout=1000)
            if message:
                print(message.value())
                self.consumer.commit()

    def stop_consuming(self):
        self.stop = True


def main():
    with KafkaConsumer() as kafka_consumer:
        kafka_consumer.consume_topic(topic="twitter-etl")


if __name__ == "__main__":
    main()
