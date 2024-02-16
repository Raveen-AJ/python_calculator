import re


def is_operator(char) -> bool:
    return re.match(r'[+\-*/%]', char) is not None
