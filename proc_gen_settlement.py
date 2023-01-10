# This code procedurally generates a settlement description
# for #dungeon23

import random
import os
os.system("clear")

settlement_culture = ["Dwarven", "Elvish", "Human", "Infernal", "Gnomish", "Orcish"]
selected_settlement_culture = random.choice(settlement_culture)

cardinal_directions = ["north", "south", "east", "west"]
selected_cardinal_directions = random.choice(cardinal_directions)

settlement_geographical_features = ["mountains", "forests", "swamps", "deserts", "oceans", "lakes", "rivers", "plains", "hills"]
selected_settlement_geographical_features = random.choice(settlement_geographical_features)

settlement_terrain = ["mountainous", "forested", "swampy", "deserted", "oceanic", "lakish", "riverish", "plained", "hilly"]
selected_settlement_terrain = random.choice(settlement_terrain)

settlement_age = ["Peace", "War", "Tranquility", "Sundering", "Rage", "Destruction", "Terror", "Doom", "Despair", "Glory", "Victory", "Darkeness", "Light", "Discovery"]
selected_settlement_age = random.choice(settlement_age)

settlement_size = ["small", "medium", "large"]
selected_settlement_size = random.choice(settlement_size)

settlement_type = ["village", "town", "city", "metropolis"]
selected_settlement_type = random.choice(settlement_type)

settlement_prefix = ["peaceful", "warlike", "tranquil", "sundered", "raging", "destructive", "terrifying", "despairing", "glorious", "victorious", "dark", "light", "discovering"]
selected_settlement_prefix = random.choice(settlement_prefix)

settlement_interesting_building = ["a large spice market every fortnight", "an ancient and abandoned temple to a long-lost diety", "a large library protected by a powerful wizard guild", "a large theatre, with unusually specific acoustics", "a large and beautiful park with exotic and tame birds roaming around", "a large pub - one of the oldest in the area",  "a spa with hot baths"]
selected_settlement_interesting_building = random.choice(settlement_interesting_building)

settlement_infrastructure = ["a large and well-kept market square", "a large and well-kept temple", "a large and well-kept theatre", "a large and well-kept park", "a large and well-kept pub", "a large and well-kept spa"]
selected_settlement_infarstructure = random.choice(settlement_infrastructure)

settlement_roads = ["A large and well-kept road", "A large and well-kept path", "A large and well-kept bridge", "A large and well-kept tunnel"]
selected_settlement_roads = random.choice(settlement_roads)

settlement_description_1 = "The settlement is a " + selected_settlement_size + " " + selected_settlement_type + " of " + selected_settlement_culture + " origin. It was first founded during the age of " + selected_settlement_age
settlement_description_2 = "and is located in a " + selected_settlement_terrain + " region. The settlement is " + selected_settlement_prefix + " and is known for a large " + selected_settlement_geographical_features + " to the " + selected_cardinal_directions + "."
settlement_description_3 = "The settlement is also known for " + selected_settlement_interesting_building + ". " + selected_settlement_roads + " connects the settlement to the rest of the world. "
settlement_description_4 = "Before entering the settlement, you notice " + selected_settlement_infarstructure + " to the " + selected_cardinal_directions + "."


print(settlement_description_1, settlement_description_2, settlement_description_3, settlement_description_4)
