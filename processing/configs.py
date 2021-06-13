import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER", "localhost:9092")
KAFKA_SCHEMA_REGISTRY_URL = os.getenv("KAFKA_SCHEMA_REGISTRY_URL", "http://localhost:8081/")
KAFKA_CONSUMER_GROUP_ID = os.getenv("KAFKA_CONSUMER_GROUP_ID", "pythonprocessing")
KAFKA_AUTO_OFFSET_RESET = os.getenv("KAFKA_AUTO_OFFSET_RESET", "latest")
TWITTER_TOPIC = os.getenv("TWITTER_TOPIC", "twitter-etl")


POSTGRES_CONFIGS = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", "postgres"),
    "database": os.getenv("POSTGRES_DATABASE", "tweet"),
}
