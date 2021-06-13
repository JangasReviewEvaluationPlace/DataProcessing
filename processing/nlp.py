from random import choice


def fake_nlp(test) -> str:
    """
    Returns just randomly positive or negative
    Model is not well enough trained.
    Accuracy will be higher by using 50/50 ... sad.
    """
    return choice(["positive", "negative"])
