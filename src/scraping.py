"""
Collection of functions to scrap and clean HTML files.
"""

from bs4 import BeautifulSoup
import re

def read_html(file_path: str, tag: str = 'div', id: str = '-post-rtjson-content') -> list[str]:
    """
    Read and parses a local HTML file and returns a list of comments according to the indicated tags and ids.

    Parameters
    file_path (str): Path of the local HTML file.
    tag (str): Tag of the element of interest in the HTML file.
    id (str): ID of the element of interest in the HTML file.

    Returns
    comments (list[str]): List of the retrieved elements.
    """

    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser', from_encoding='windows-1252')
            
    results = soup.find_all(tag, id=id)

    comments = []

    for result in results:
        comments.append(str(result))
    
    return comments

def remove_html_tags(input_list_str: list[str]) ->list[str]:
    """
    Returns strings with HTML tags removed.
    
    Parameters
    input_list_str (list[str]): Input list of strings

    Returns
    list_str_html_tags_removed (list[str]): List of strings with HTML tags removed.
    """
    list_str_html_tags_removed = []

    for str in input_list_str:
        str_html_tags_removed = re.sub("<.*?>", "", str).replace('\n', '')
        list_str_html_tags_removed.append(str_html_tags_removed)

    return list_str_html_tags_removed