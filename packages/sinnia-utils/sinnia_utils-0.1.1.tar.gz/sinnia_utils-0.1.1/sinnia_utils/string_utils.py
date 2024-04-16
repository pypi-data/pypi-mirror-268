### Version 0.1
from typing import Literal
import logging, re, unicodedata
from datetime import time, timedelta, datetime, date, timezone

class StringUtils(object):
    
    DF      = "%Y-%m-%d"
    FULL_DF = "%Y-%m-%d %H:%M:%S"

    @staticmethod
    def remove_nonspacing_marks(s) -> str:
        "Normalizes the unicode string s and removes non-spacing marks (see https://www.compart.com/en/unicode/category/Mn)"
        return ''.join(c for c in unicodedata.normalize('NFKD', s)
                      if unicodedata.category(c) != 'Mn')

    @staticmethod
    def boolean_str_to_int(x) -> Literal[1, 0, -1]:
        "Converts [1, 1.0, 'true', 'True', True] to 1, and [0, 0.0, 'false', 'False', False] to 0. Other values produce a ValueError"
        as_int = -1
        if x == 1 or x == 1.0 or x == True or x == "True" or x == "true":
            as_int = 1 
        elif x == 0 or x == 0.0 or x == False or x == "False" or x == "false" or x == None:
            as_int = 0
        else:
            raise ValueError(f"Error: Could not parse input value as ~true=1 or ~false=0")
        return as_int

    @staticmethod
    def get_as_comma_separated_integers(s): 
        "Validates that the input is a series of comma-separated numbers (or a single number) and removes whitespaces and trailing commas."
        s = re.sub(' ', '', s)   # remove spaces
        s = re.sub(',$', '', s)  # remove final comma, if any
        pattern = re.compile(r"[\d+,?\d+]+")
        if pattern.fullmatch(s):
            return s  
        else:
            raise ValueError(f"Error: Could not parse input as comma-separated ints")

    @staticmethod
    def get_as_comma_separated_youtube_channel_ids(s):
        "Validates that the input is a series of comma-separated YouTube channel ids (or a single id) and removes whitespaces and trailing commas."
        s = re.sub(' ', '', s)   # remove spaces
        s = re.sub(',$', '', s)  # remove final comma, if any
        pattern = re.compile(r"(UC[-_0-9a-zA-Z]+)?")
        ids = s.split(',')
        matching = 0
        for id in ids:
            if pattern.fullmatch(id):
                matching = 1
            else:
                break
        if matching:
            return s
        else:
            raise ValueError(f"Error: could not parse input as comma-separated YouTube channel IDs")

    @staticmethod
    def camel_case_to_snake_case(camel) -> str:
        return ''.join(['_' + c.lower() if c.isupper() else c.lower() for c in camel]).lstrip('_')
