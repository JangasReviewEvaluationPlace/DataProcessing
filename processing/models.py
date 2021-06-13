from dataclasses import dataclass
from datetime import datetime
from psycopg2 import


@dataclass
class Tweet:
    id: int
    created_at: datetime
    text: str
    feedback_type: str
    language: str


class TweetManager:
    def insert_tweet(self, cursor: "psycopg2.cursor", tweet: Tweet):
        statement = """
            INSERT INTO tweet (id, created_at, text, feedback_type, language)
            VALUES (%s, %s, %s, %s, %s);
        """
        cursor.execute(
            statement, (
                tweet.id,
                tweet.created_at,
                tweet.text,
                tweet.feedback_type,
                tweet.language
            )
        )
