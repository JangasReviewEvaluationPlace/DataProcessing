from random import choice


def fake_nlp(text: str) -> str:
    """
    Returns just randomly positive or negative
    Model is not well enough trained.
    Accuracy will be higher by using 50/50 ... sad.
    """
    return choice(["positive", "negative"])


def language_detection(text: str) -> str:
    return "en"
