import logging
from consumer import KafkaConsumer
from nlp import fake_nlp, language_detection
from database import Postgres
from models import Tweet, TweetManager


logger = logging.getLogger()
logger.setLevel(logging.getLevelName("INFO"))


def processing(message):
    value = message.value()
    logging.info("Message received.", value["Text"])
    language = language_detection(text=value["Text"])
    if language != "en":
        return

    feedback_type = fake_nlp(value["Text"])
    tweet = Tweet(
        id=value["Id"],
        created_at=value["CreatedAt"],
        text=value["Text"],
        feedback_type=feedback_type,
        language=language
    )
    with Postgres() as db:
        TweetManager.insert_tweet(cursor=db.cur, tweet=tweet)
    logging.info("Message proceed. It was detected as", language)


def main():
    try:
        logging.info("Start Kafka Connection")
        with KafkaConsumer() as kafka_consumer:
            kafka_consumer.consume_topic(topic="twitter-etl", message_processing=processing)
    except Exception as e:
        logging.error("Error - restart main.", str(e))
        return main()


if __name__ == "__main__":
    main()
