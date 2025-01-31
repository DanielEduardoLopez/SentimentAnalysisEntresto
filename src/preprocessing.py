"""
Collection of functions for text preprocessing.
"""

# Libraries importation
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
nltk.download('stopwords')


# Functions

def clean_text(text: str) -> str:
    """
    Removes non-alphabetical characters such as special characters and numbers, and 
    spaces at the beginning and at the end of the string.  

    Parameters:
    text (str): Input string.

    Returns:
    text_cleaned (str): Processed string.

    """

    text_cleaned = re.sub('[^A-Za-z]+', ' ', text).strip()
    
    return text_cleaned



def tokenize_text(text: str) -> list[str]:
    """
    Tokenize input text and returns a list of words in lower case with only alphabetical characters and without stop words.

    Parameters:
    text (str): Input text.

    Returns:
    words (list[str]): List of words in lower case with only alphabetical characters and without stop words.

    """

    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))

    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    return words
