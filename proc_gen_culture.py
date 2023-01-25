# this program procedurally generates Culture description of something fun or interesting about the local people. 
# Something to make them stand out
#
# This program is a work in progress. I am still working on it.

import random
import os
os.system("clear")
category_culture = ["food","language","religion","music","art","architecture","clothing","fashion","dance","literature","science","technology","medicine","sports","games","politics","economics","military","law","transportation","weather","geography","history","society","family","education","work","leisure","travel","food","language","religion","music","art","architecture","clothing","fashion","dance","literature","science","technology","medicine","sports","games","politics","economics","military","law","transportation","weather","geography","history","society","family","education","work","leisure","travel"]
selected_category_culture = random.choice(category_culture)

frequency_culture = ["always","often","sometimes","rarely","never"]
selected_frequency_culture = random.choice(frequency_culture)

food_culture = ["spicy","sweet","salty","sour","bitter","umami","savory","tangy","creamy","crunchy","crispy","juicy","soft","hard","smooth","rough","soggy","dry","fluffy","crumbly","crunchy","crispy","juicy","soft","hard","smooth","rough","soggy","dry","fluffy","crumbly","crunchy","crispy","juicy","soft","hard","smooth","rough","soggy","dry","fluffy","crumbly","crunchy","crispy","juicy","soft","hard","smooth","rough","soggy","dry","fluffy","crumbly"]
selected_food_culture = random.choice(food_culture)

language_characteristics =["slavic", "romantic", "tonal", "glyphic", "mostly physical"]
selected_language_characteristics = random.choice(language_characteristics)

religion_characteristics = ["polytheistic", "monotheistic", "pantheistic", "animistic", "atheistic", "agnostic", "deistic", "polytheistic", "monotheistic", "pantheistic", "animistic", "atheistic", "agnostic", "deistic"]
selected_religion_characteristics = random.choice(religion_characteristics)

musical_characteristics = ["precussive", "melodic", "harmonic", "rhythmic", "precussive", "melodic", "harmonic", "rhythmic"]
selected_musical_characteristics = random.choice(musical_characteristics)

art_characteristics = ["abstract", "realistic", "symbolic", "abstract", "realistic", "symbolic"]
selected_art_characteristics = random.choice(art_characteristics)

architecture_characteristics = ["organic", "geometric", "organic", "geometric"]
selected_architecture_characteristics = random.choice(architecture_characteristics)

clothing_characteristics = ["form fitting", "loose", "form fitting", "loose"]
selected_clothing_characteristics = random.choice(clothing_characteristics)

fashion_characteristics = ["form fitting", "loose", "form fitting", "loose"]
selected_fashion_characteristics = random.choice(fashion_characteristics)

dance_characteristics = ["precussive", "melodic", "harmonic", "rhythmic", "precussive", "melodic", "harmonic", "rhythmic"]
selected_dance_characteristics = random.choice(dance_characteristics)

literature_characteristics = ["poetry", "fiction", "non-fiction", "poetry", "fiction", "non-fiction"]
selected_literature_characteristics = random.choice(literature_characteristics)

science_characteristics = ["mathematics", "astronomy", "physics", "chemistry", "biology", "geology", "mathematics", "astronomy", "physics", "chemistry", "biology", "geology"]
selected_science_characteristics = random.choice(science_characteristics)

technology_characteristics = ["mechanical", "electrical", "mechanical", "electrical"]
selected_technology_characteristics = random.choice(technology_characteristics)

medicine_characteristics = ["herbal", "surgical", "herbal", "surgical"]
selected_medicine_characteristics = random.choice(medicine_characteristics)

sports_characteristics = ["team", "individual", "team", "individual"]
selected_sports_characteristics = random.choice(sports_characteristics)

games_characteristics = ["board", "card", "dice", "board", "card", "dice"]
selected_games_characteristics = random.choice(games_characteristics)

politics_characteristics = ["democratic", "monarchic", "oligarchic", "democratic", "monarchic", "oligarchic"]
selected_politics_characteristics = random.choice(politics_characteristics)

economic_characteristics = ["democratic", "monarchic", "oligarchic", "democratic", "monarchic", "oligarchic"]
selected_economic_characteristics = random.choice(economic_characteristics)

military_characteristics = ["martial", "decentralized", "regimented", "democratic", "monarchic", "oligarchic"]
selected_military_characteristics = random.choice(military_characteristics)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "red", "orange", "yellow", "green", "blue", "indigo", "violet"]
selected_colors = random.choice(colors)

pattern = ["striped", "plaid", "polka-dotted", "striped", "plaid", "polka-dotted"]
selected_pattern = random.choice(pattern)

fabric = ["cotton", "silk", "wool", "cotton", "silk", "wool"]
selected_fabric = random.choice(fabric)


cultural_event_1 = "Little known to those outside this culture is a decidely uncommon " + selected_category_culture + " tradition. "
cultural_event_2 = "Participants in this tradition " + selected_frequency_culture + " invoke strong " + selected_language_characteristics + " accent every other day!"
print(cultural_event_1)
print(cultural_event_2)