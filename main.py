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

def classify_types(type1, type2=None):
    weak = OrderedDict()
    strong = OrderedDict()
    immune = OrderedDict()
    neutral = OrderedDict()

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

    return weak, strong, immune, neutral

while True:
    Q1 = input("What's the 1st Type? ").lower()
    if Q1 in types:
        T1 = Q1
        print(f"Type 1: {T1.capitalize()}")
    else:
        print('Invalid Type')
        continue

    Q2 = input("What's the 2nd Type? (If there isn't, leave it blank)").lower()
    if Q2 in types:
        T2 = Q2
        print(f"Type 2: {T2.capitalize()}")
    elif Q2 == '':
        T2 = None
        print("Without 2nd type")
    else:
        print('Invalid Type')
        continue

    # Call the classify_types function and capture the returned values
    weak, strong, immune, neutral = classify_types(T1, T2)

    # Print the classifications
    print("\nTakes 0.25x from:")
    for k in weak.keys():
        print(k.capitalize())

    print("\nTakes 1x from:")
    for k in neutral.keys():
        print(k.capitalize())

    print("\nTakes 2x from:")
    for k in strong.keys():
        print(k.capitalize())

    print("\nTakes 0x from:")
    for k in immune.keys():
        print(k.capitalize())

    Q3 = input('\nDo you wish to continue? 1-YES 2-NO ')
    if Q3 == '2':
        break
    elif Q3 != '1':
        print('Invalid response. Please choose between 1-YES or 2-NO.')
        continue
