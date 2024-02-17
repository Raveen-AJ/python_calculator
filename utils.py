import re


def is_operator(char) -> bool:
    return re.match(r'[+\-*/%]', char) is not None


def get_sections(expression) -> list[str]:
    return re.split(r'[+\-*/%]', expression)


def remove_leading_zeros(expression) -> str:
    return re.sub(r'(?<!\.)\b0+(\d+)', r'\1', expression)
