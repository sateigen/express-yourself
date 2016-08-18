import re


def phone_numbers(text):
    return re.findall(r"\(?[0-9]{3}\)?\.?\s?-?[0-9]{3}\-?\.?[0-9]{4}", text)
