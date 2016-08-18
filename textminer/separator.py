import re


def words(string):
    string = string.split()
    results = [word for word in string if re.search(r"^\w*\-?[a-z]+$", word)]
    if results != []:
        return results
    else:
        return None


def phone_number(num_string):
    phone_numbers = {}
    try:
        groups = re.search(r"\(?([0-9]{3})\)?\.?\s?-?([0-9]{3})\-?\.?([0-9]{4})", num_string).groups()
        phone_numbers["area_code"] = groups[0]
        phone_numbers["number"] = '-'.join(groups[1:])
        return phone_numbers
    except AttributeError:
        return None


def money(currency_str):
    currency = {}
    try:
        groups = re.search(r"(^\$)((?:0|[1-9]\d{0,2}(?:,?\d{3})*)(?:\.?\d{2})?$)", currency_str).groups()
        currency["currency"] = groups[0]
        amount = groups[1].replace(',', '')
        currency["amount"] = float(amount)
        return currency
    except AttributeError:
        return None


def zipcode(num_string):
    zipcode = {}
    try:
        groups = re.search(r"^(\d{5})\-?(\d{4})?$", num_string).groups()
        zipcode["zip"] = groups[0]
        if groups[1]:
            zipcode["plus4"] = groups[1]
        else:
            zipcode["plus4"] = None
        return zipcode
    except AttributeError:
        return None


def date(date_string):
    dates = {}
    try:
        groups = re.search(r"(\d{1,4})[/-](\d{1,2})[/-](\d{1,4})", date_string).groups()
        if len(groups[0]) < 4:
            dates["month"] = int(groups[0].lstrip('0'))
            dates["day"] = int(groups[1].lstrip('0'))
            dates["year"] = int(groups[2])
        else:
            dates["year"] = int(groups[0])
            dates["month"] = int(groups[1].lstrip('0'))
            dates["day"] = int(groups[2].lstrip('0'))
        return dates
    except AttributeError:
        return None


def email(address):
    email = {}
    try:
        groups = re.search(r"([a-z0-9.]+)@([a-z]+\.[a-z]{2,4})", address).groups()
        email["local"] = groups[0]
        email["domain"] = groups[1]
        return email
    except AttributeError:
        return None


def address(text):
    address = {}
    try:
        groups = re.search(r"(\d+[\w\s]+)[\n,]([\w\s]+), ([A-Z]{2}) (\d{5})\-?(\d{4})?", text).groups()
        address["address"] = groups[0]
        address["city"] = groups[1].strip()
        address["state"] = groups[2]
        address["zip"] = groups[3]
        if groups[4]:
            address["plus4"] = groups[4]
        else:
            address["plus4"] = None
        return address
    except AttributeError:
        return None
