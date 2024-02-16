import re


def is_operator(char) -> bool:
    return re.match(r'[+\-*/%]', char) is not None


def is_number(string):
    print(string)
    try:
        float(string)
        return True
    except ValueError:
        return False
