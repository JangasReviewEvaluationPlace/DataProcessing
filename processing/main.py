from consumer import KafkaConsumer
from nlp import fake_nlp


def processing(message):
    feedback_type = fake_nlp(message.value())
    print(message.value(), feedback_type)


def main():
    with KafkaConsumer() as kafka_consumer:
        kafka_consumer.consume_topic(topic="twitter-etl", message_processing=processing)


if __name__ == "__main__":
    main()
