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
#    return re.search(r"^\d{5}(\-?\d{4})?$", num_string)


#def date(date):
#    date_dict = {}
#    try:
#        groups = re.match(r'(\d{4})[/-](\d{0,2})[/-](\d{0,2})|(\d{0,2})[/-](\d{0,2})[/-](\d{4})', date).groups()
#        if groups[0]:
#            date_dict["year"] = int(groups[0])
#            date_dict["month"] = int(groups[1])
#            date_dict["day"] = int(groups[2])
#        else:
#            date_dict["month"] = int(groups[3])
#            date_dict["day"] = int(groups[4])
#            date_dict["year"] = int(groups[5])
#        return date_dict
#    except:
#        return None



#if re.search(r"^\d{1,4}[/-]\d{1,2}[/-]\d{1,4}", string)

#possible_emails = ["clinton", "clinton@dreisbach.us", "beanguy@example.org",
 #                  "Email help@example.org for more information",
#                   "terry@example.org", "@carmen", "what@what", "hi@example.org"]
#[possibility
# for possibility in possible_emails
# if re.search("\A\w+@\w+\.\w{2,3}\Z", possibility)]
