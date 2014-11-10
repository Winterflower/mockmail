"""
The text_adapter module contains functions
for preprocessing mock "emails" to create a Numpy
array suitable for usage with scikit-learn
Author: Camilla Montonen (2014)
"""

import numpy as np



def dictionary_builder(textdata):
    """
    Returns a dict object of all unique words in text training data
        -key: string
        -value: integer (initialised to 0)
    Argument: list of strings
    Returns: dict
    """
    email_dictionary={}
    for email in list_of_strings:
        email_word=email.split()
        for word in email_word:
            if word not in email_dictionary.keys():
                email_dictionary['word']
            else:
                pass
    return email_dictionary
