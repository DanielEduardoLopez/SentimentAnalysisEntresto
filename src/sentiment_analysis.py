"""
Collection of functions for sentiment analysis using TextBlob.
"""

# Libraries importation
from textblob import TextBlob

# Functions
def get_polarity(text: str) -> float:
    """
    Returns the polarity of a text within a range [-1.0, 1.0] using TextBlob, where:    
       -1.0: Negative
        0.0: Neutral
        1.0: Positive

    Parameters:
    text (str): Input text.

    Returns:
    polarity (float): Polarity of the text within the range [-1.0, 1.0].

    """

    polarity = TextBlob(text).sentiment.polarity

    return polarity


def get_subjectivity(text: str) -> float:
    """
    Returns the subjectivity of a text within a range [0.0, 1.0] using TextBlob, where:       
        0.0: Objective
        1.0: Subjective

    Parameters:
    text (str): Input text.

    Returns:
    subjectivity (float): Polarity of the text within the range [-1.0, 1.0], where:


    """

    subjectivity = TextBlob(text).sentiment.subjectivity

    return subjectivity


def get_sentiment(polarity: float) -> str:
    """
    Returns the sentiment of a given text based on the polarity thereof as follows:
        Negative: polarity < 0 
        Neutral: polarity = 0
        Positive: polarity > 0

    Parameters:
    polarity (float): Score within a range [-1.0, 1.0] obtained.

    Returns:
    sentiment (str): Interpretation of polarity score.

    """

    if polarity < 0:
        return "Negative"
    
    elif polarity == 0:
        return "Neutral"
    
    else:
        return "Positive"


def get_subjectivity_interpretation(subjectivity: float) -> str:
    """
    Returns the subjectivity interpretation of a given text based on the subjectivity score thereof as follows: 
        0.0: Objective
        1.0: Subjective

    Parameters:
    text (str): Input text.

    Returns:
    subjectivity (float): Polarity of the text within the range [-1.0, 1.0], where:


    """

    if subjectivity <= 0.5:
        return "Objective"
    
    else:
        return "Subjective"