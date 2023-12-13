import re

def email(adresse_email):
 
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    matches = re.findall(pattern, adresse_email)
    return bool(matches)

