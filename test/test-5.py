from regularexpression5 import email

adresse = "exemple@domaine.com"

if email(adresse):
    print(f"L'adresse e-mail {adresse} est au format attendu.")
else:
    print(f"L'adresse e-mail {adresse} n'est pas au format attendu.")