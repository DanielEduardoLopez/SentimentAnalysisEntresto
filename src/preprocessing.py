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
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')


# Functions

def clean_text(text: str) -> str:
    """
    Removes non-alphabetical characters such as special characters and numbers, and 
    spaces at the beginning and at the end of the string.  

    Parameters:
    ----------
    text (str): Input string.

    Returns:
    -------
    text_cleaned (str): Processed string.

    """

    text_cleaned = re.sub('[^A-Za-z]+', ' ', text).strip()
    
    return text_cleaned



def tokenize_text(text: str) -> list[str]:
    """
    Tokenize input text and returns a list of words in lower case with only alphabetical characters and without stop words.

    Parameters:
    ----------
    text (str): Input text.

    Returns:
    -------
    words (list[str]): List of words in lower case with only alphabetical characters and without stop words.

    """

    words = word_tokenize(text)

    stop_words = set(stopwords.words('english'))

    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    return words


def lemmatize_text(pos_text: list[tuple[str, str]]) -> str:
    """
    Get the lemma from a set of POS tagged text.

    Parameters:
    ----------
    pos_text (list[tuple[str, str]]): POS tagget text.

    Returns:
    -------
    lemma_text (str): Lemmatized text.

    """
    
    lemmatizer = nltk.WordNetLemmatizer()

    lemma_text = " "

    for word, pos in pos_text:

        if not pos:
            lemma = word
            lemma_text = lemma_text + " " + lemma

        else:
            lemma = lemmatizer.lemmatize(word)
            lemma_text = lemma_text + " " + lemma

    return lemma_text