import re

def telephone(numero_telephone):

    pattern = re.compile(r'^\d{2}-\d{3}-\d{4}$')
    return bool(pattern.match(numero_telephone))

