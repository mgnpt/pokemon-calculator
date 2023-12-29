# main.py

from collections import OrderedDict
from valores import (
    Normal, Fire, Water, Electric, Grass, Ice, Fighting,
    Poison, Ground, Flying, Psychic, Bug, Rock, Ghost,
    Dragon, Dark, Steel, Fairy
)

types = ('normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting',
         'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost',
         'dragon', 'dark', 'steel', 'fairy')
T1 = ''
T2 = ''
weak = OrderedDict()
strong = OrderedDict()
immune = OrderedDict()
neutral = OrderedDict()


def classify_types(type1, type2=None):
    # Get weaknesses for type1
    weaknesses_T1 = eval(type1.capitalize())

    # If type2 is specified, combine the weaknesses with type2
    if type2:
        weaknesses_T2 = eval(type2.capitalize())
        combined_weaknesses = {k.lower(): v * weaknesses_T2.get(k, 1) for k, v in weaknesses_T1.items()}
    else:
        combined_weaknesses = {k.lower(): v for k, v in weaknesses_T1.items()}

    # Classify based on effectiveness
    for k, v in combined_weaknesses.items():
        if v < 1 and v > 0:
            weak[k] = v
        elif v == 1:
            neutral[k] = v
        elif v > 1:
            strong[k] = v
        elif v == 0:
            immune[k] = v

    # Handle cases where type is not explicitly mentioned in weaknesses dictionary
    for t in types:
        if t.lower() not in combined_weaknesses and t.lower() not in neutral:
            neutral[t.lower()] = 1.0
while True:
    Q1 = input('Qual é o primeiro type? ').lower()
    if Q1 in types:
        T1 = Q1
        print(f"Type 1: {T1.capitalize()}")
    else:
        print('Tipo Inválido')
        continue

    Q2 = input('Qual é o segundo type? (Deixa em branco se não houver segundo tipo) ').lower()
    if Q2 in types:
        T2 = Q2
        print(f"Type 2: {T2.capitalize()}")
        classify_types(T1, T2)
    elif Q2 == '':
        T2 = None
        print("Sem segundo tipo.")
    else:
        print('Tipo Inválido')
        continue

    # Print the classifications
    print("\nWeaknesses:")
    for k, v in weak.items():
        print(f"{k.capitalize()}: {v}x")

    print("\nNeutral:")
    for k, v in neutral.items():
        print(f"{k.capitalize()}: {v}x")

    print("\nStrong:")
    for k, v in strong.items():
        print(f"{k.capitalize()}: {v}x")

    print("\nImmune:")
    for k, v in immune.items():
        print(f"{k.capitalize()}: {v}x")

    # Reset the dictionaries for the next iteration
    weak.clear()
    strong.clear()
    immune.clear()
    neutral.clear()

    Q3 = input('\nQueres continuar? 1-SIM 2-NÃO ')
    if Q3 == '2':
        break
    elif Q3 != '1':
        print('Resposta Inválida. Por favor, escolhe 1-SIM ou 2-NÃO.')
        continue