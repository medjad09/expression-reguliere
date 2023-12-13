from regularexpression4 import telephone

numero_a_verifier = "12-345-6789"

if telephone(numero_a_verifier):
    print(f"Le numéro de téléphone {numero_a_verifier} est au format attendu.")
else:
    print(f"Le numéro de téléphone {numero_a_verifier} n'est pas au format attendu.")
