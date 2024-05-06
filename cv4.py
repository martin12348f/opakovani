import random

def generuj_cisla_s_nahodnou_delkou():
    delka = random.randint(1, 100)  
    cisla = [random.randint(1, 100) for _ in range(delka)]  
    return cisla

cisla = generuj_cisla_s_nahodnou_delkou()

print("Vygeneroval jsi čísla s náhodnou délkou:", cisla)
