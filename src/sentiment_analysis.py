"""
Collection of functions for sentiment analysis using TextBlob.
"""

from textblob import TextBlob

def get_polarity(text: str) -> float:
    """
    Returns the polarity of a text within a range [-1.0, 1.0] using TextBlob.

    Parameters:
    text (str): Input text.

    Returns:
    polarity (float): Polarity of the text within the range [-1.0, 1.0], where:
        -1.0: Negative
        0.0: Neutral
        1.0: Positive

    """

    polarity = TextBlob(text).sentiment.polarity

    return polarity