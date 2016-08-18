import re


#  def words(string, count=None):
#    string = string.split()
#    if count:
#        return count == len(string)
#    for item in string:
#        return word(item)


#def phone_number(num_string):
#    return re.search(r"(\(?[0-9]{3}\))?\.?\s?[0-9]{3}\-?\.?[0-9]{4}", num_string)


#def money(currency_str):
#    return re.search(r"^\$(?:0|[1-9]\d{0,2}(?:,?\d{3})*)(?:\.?\d{2})?$", currency_str)


#def zipcode(num_string):
#    return re.search(r"^\d{5}(\-?\d{4})?$", num_string)


def date(date):
    date_dict = {}
    try:
        groups = re.match(r'(\d{4})[/-](\d{0,2})[/-](\d{0,2})|(\d{0,2})[/-](\d{0,2})[/-](\d{4})', date).groups()
        if groups[0]:
            date_dict["year"] = int(groups[0])
            date_dict["month"] = int(groups[1])
            date_dict["day"] = int(groups[2])
        else:
            date_dict["month"] = int(groups[3])
            date_dict["day"] = int(groups[4])
            date_dict["year"] = int(groups[5])
        return date_dict
    except:
        return None   



#if re.search(r"^\d{1,4}[/-]\d{1,2}[/-]\d{1,4}", string)
    
#possible_emails = ["clinton", "clinton@dreisbach.us", "beanguy@example.org", 
 #                  "Email help@example.org for more information",
#                   "terry@example.org", "@carmen", "what@what", "hi@example.org"]
#[possibility 
# for possibility in possible_emails 
# if re.search("\A\w+@\w+\.\w{2,3}\Z", possibility)]
