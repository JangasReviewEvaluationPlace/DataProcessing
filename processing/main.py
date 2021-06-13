from consumer import KafkaConsumer
from nlp import fake_nlp, language_detection
from database import Postgres
from models import Tweet, TweetManager


def processing(message):
    value = message.value()
    language = language_detection(text=value["text"])
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


def main():
    with KafkaConsumer() as kafka_consumer:
        kafka_consumer.consume_topic(topic="twitter-etl", message_processing=processing)


if __name__ == "__main__":
    main()
