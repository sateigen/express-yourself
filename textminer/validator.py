import re


def binary(num_str):
    return re.search(r"^[01]+$", num_str)


def binary_even(num_str):
    if binary(num_str):
        return re.search(r"0$", num_str)


def hex(string):
    return re.search(r"^[A-F0-9]+$", string)


def word(string):
    return re.search(r"^\w*\-?[a-z]+$", string)


def words(string, count=None):
    string = string.split()
    results = [item for item in string if word(item)]
    if count:
        return count == len(results)
    else:
        return results != []


def phone_number(num_string):
    return re.search(r"(\(?[0-9]{3}\))?\.?\s?[0-9]{3}\-?\.?[0-9]{4}", num_string)


def money(currency_str):
    return re.search(r"^\$(?:0|[1-9]\d{0,2}(?:,?\d{3})*)(?:\.?\d{2})?$", currency_str)


def zipcode(num_string):
    return re.search(r"^\d{5}(\-?\d{4})?$", num_string)


def date(string):
    return re.search(r"^\d{1,4}[/-]\d{1,2}[/-]\d{1,4}", string)


def email(text):
    return re.search(r"[a-z0-9.]+@[a-z]+\.[a-z]{2,4}", text)


def address(text):
    return re.search(r"(\d+[\w\s]+)[\n,]([\w\s]+), ([A-Z]{2}) (\d{5})\-?(\d{4})?", text)
