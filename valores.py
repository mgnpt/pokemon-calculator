# valores.py

# Define default value for types not explicitly mentioned
default_value = 1

# Define individual type dictionaries
Normal = {'Fighting': 2, 'Ghost': 0}
Fire = {'Fire': 0.5, 'Water': 2, 'Grass': 0.5, 'Ice': 0.5, 'Ground': 2,
        'Bug': 0.5, 'Rock': 2, 'Steel': 0.5, 'Fairy': 0.5}
Water = {'Fire': 0.5, 'Water': 0.5, 'Electric': 2, 'Grass': 2, 'Ice': 0.5,
         'Steel': 0.5}
Electric = {'Electric': 0.5, 'Ground': 2, 'Flying': 2, 'Steel': 0.5}
Grass = {'Fire': 2, 'Water': 0.5, 'Electric': 0.5, 'Grass': 0.5, 'Ice': 2,
         'Poison': 2, 'Ground': 0.5, 'Flying': 2, 'Bug': 2}
Ice = {'Ice': 0.5, 'Fire': 2, 'Fighting': 2, 'Rock': 2, 'Steel': 2}
Fighting = {'Bug': 0.5, 'Rock': 0.5, 'Dark': 0.5, 'Flying': 2, 'Psychic': 2,
            'Fairy': 2}
Poison = {'Grass': 0.5, 'Fighting': 0.5, 'Poison': 0.5, 'Bug': 0.5, 'Fairy': 0.5,
          'Ground': 2, 'Psychic': 2}
Ground = {'Electric': 0, 'Poison': 0.5, 'Rock': 0.5, 'Water': 2, 'Grass': 2,
          'Ice': 2}
Flying = {'Ground': 0, 'Grass': 0.5, 'Fighting': 0.5, 'Bug': 0.5, 'Electric': 2,
          'Ice': 2, 'Rock': 2}
Psychic = {'Fighting': 0.5, 'Psychic': 0.5, 'Bug': 2, 'Ghost': 2, 'Dark': 2}
Bug = {'Grass': 0.5, 'Fighting': 0.5, 'Ground': 0.5, 'Fire': 2, 'Flying': 2,
       'Rock': 2}
Rock = {'Normal': 0.5, 'Fire': 0.5, 'Poison': 0.5, 'Flying': 0.5, 'Water': 2,
        'Grass': 2, 'Fighting': 2, 'Ground': 2, 'Steel': 2}
Ghost = {'Normal': 0, 'Fighting': 0, 'Poison': 0.5, 'Bug': 0.5, 'Ghost': 2,
         'Dark': 2}
Dragon = {'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Grass': 0.5, 'Ice': 2,
          'Dragon': 2, 'Fairy': 2}
Dark = {'Psychic': 0, 'Ghost': 0.5, 'Dark': 0.5, 'Fighting': 2, 'Bug': 2,
        'Fairy': 2}
Steel = {'Poison': 0, 'Normal': 0.5, 'Grass': 0.5, 'Ice': 0.5, 'Flying': 0.5,
         'Psychic': 0.5, 'Bug': 0.5, 'Rock': 0.5, 'Dragon': 0.5, 'Steel': 0.5,
         'Fairy': 0.5, 'Fire': 2, 'Fighting': 2, 'Ground': 2}
Fairy = {'Dragon': 0, 'Fighting': 0.5, 'Bug': 0.5, 'Dark': 0.5, 'Poison': 2,
         'Steel': 2}

# Update all types with default value for types not explicitly mentioned
for type_var in ['Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
    globals()[type_var] = {k: v if k in globals()[type_var] else default_value for k, v in globals()[type_var].items()}
