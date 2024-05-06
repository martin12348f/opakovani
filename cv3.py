import random

def generuj_cisla_od_1_do_100():

    cisla = []

    for i in range(1, 100):
        cisla.append(i)
    return cisla

cisla_od_1_do_100 = generuj_cisla_od_1_do_100()

print("vygeneroval jsi cisla od 1 do 100", cisla_od_1_do_100)

