import re


def clean_str(string: str) -> str:
    return re.sub('[^0-9]', '', string)
