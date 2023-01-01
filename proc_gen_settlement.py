# This code procedurally generates a settlement description
# for #dungeon23

import random
import os
os.system("clear")

settlement_culture = ["Dwarven", "Elvish", "Human", "Infernal", "Gnomish", "Orcish"]
selected_settlement_culture = random.choice(settlement_culture)

settlement_age = ["Peace", "War", "Tranquility", "Sundering", "Rage", "Destruction", "Terror", "Doom", "Despair", "Glory", "Victory", "Darkeness", "Light", "Discovery"]
selected_settlement_age = random.choice(settlement_age)

settlement_size = ["small", "medium", "large", "huge"]
selected_settlement_size = random.choice(settlement_size)

settlement_type = ["village", "town", "city", "metropolis"]
selected_settlement_type = random.choice(settlement_type)

settlement_prefix = ["peaceful", "warlike", "tranquil", "sundered", "raging", "destructive", "terrifying", "doomed", "despairing", "glorious", "victorious", "dark", "light", "discovering"]
selected_settlement_prefix = random.choice(settlement_prefix)

settlement_description = "The settlement is a " + selected_settlement_size + " " + selected_settlement_type + " of " + selected_settlement_culture + " origin. It was first founded during the age of " + selected_settlement_age

print(settlement_description)
