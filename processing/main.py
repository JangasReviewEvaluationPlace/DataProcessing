from consumer import KafkaConsumer


def processing(message):
    print(message.value())


def main():
    with KafkaConsumer() as kafka_consumer:
        kafka_consumer.consume_topic(topic="twitter-etl", message_processing=processing)


if __name__ == "__main__":
    main()
