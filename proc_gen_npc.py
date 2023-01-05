import random
import os
os.system("clear")

# procedural generation of npc
# these characteristics are used from Generating Knowledge Graphs using GPT-J for Automated Story Generation Purposes
# by Samihan Dani
# https://smartech.gatech.edu/bitstream/handle/1853/66753/DANI-UNDERGRADUATERESEARCHOPTIONTHESIS-2022.pdf?isAllowed=y&sequence=1

# LIVE: Where does the {} live?,
# KNOWN: What is the {} known for?,
# NAME: What is {}s name?,
# LIKE: What does the {} like to do?,
# DISLIKE: What does the {} not like to do?,
# FROM: Where is the {} from?,
# GOING: Where is the {} going?,
# DESIRE: What does the {} desire?,
# MOTIVATED: What is {} motivated by?,
# DOING: What is {} doing right now?,
# UNIQUE: What is unique about the {}?,
# DESCRIBE: How is the {} described?

fantasy_city_names = ["Aargrin", "Sraveja", "Bleracht", "Copstron", "Dorvyn", "Eldor", "Ferndale", "Glenhaven", "Haven", "Ivory", "Jorvik", "Korvyn", "Lorvyn", "Mithril", "Narvyn", "Orryn", "Pyr", "Quarvyn", "Rorvyn", "Sarvyn", "Tyr", "Urryn", "Vorvyn", "Wyr", "Xorvyn", "Yorvyn", "Zorvyn"]
select_city = random.choice(fantasy_city_names)

fantasy_character_names = ["Aar", "Bler", "Cop", "Dor", "Eld", "Fern", "Glen", "Hav", "Iv", "Jor", "Kor", "Lor", "Mith", "Nar", "Orr", "Pyr", "Quar", "Ror", "Sar", "Tyr", "Urr", "Vor", "Wyr", "Xor", "Yor", "Zor"]
select_character = random.choice(fantasy_character_names)

fantasy_character_traits = ["adventurous", "aggressive", "ambitious", "amusing", "brave", "calm", "careful", "charming", "clever", "confident", "courageous", "creative", "curious", "daring", "determined", "diligent", "dramatic", "energetic", "enthusiastic", "friendly", "funny", "generous", "gentle", "good", "helpful", "honest", "humorous", "imaginative", "independent", "intelligent", "kind", "loyal", "modest", "neat", "nice", "optimistic", "outgoing", "patient", "persistent", "pioneering", "polite", "powerful", "practical", "quiet", "reliable", "resourceful", "romantic", "self-confident", "self-disciplined", "sensible", "sensitive", "shy", "sincere", "sociable", "straightforward", "sympathetic", "thoughtful", "tidy", "tough", "unassuming", "understanding", "versatile", "warmhearted", "willing", "witty"]
select_character_trait = random.choice(fantasy_character_traits)

fantasy_character_traits_negative = ["aggressive", "ambitious", "arrogant", "bossy", "brave", "calm", "careful", "charming", "clever", "confident", "courageous", "creative", "curious", "daring", "determined", "diligent", "dramatic", "energetic", "enthusiastic", "friendly", "funny", "generous", "gentle", "good", "helpful", "honest", "humorous", "imaginative", "independent", "intelligent", "kind", "loyal", "modest", "neat", "nice", "optimistic", "outgoing", "patient", "persistent", "pioneering", "polite", "powerful", "practical", "quiet", "reliable", "resourceful", "romantic", "self-confident", "self-disciplined", "sensible", "sensitive", "shy", "sincere", "sociable", "straightforward", "sympathetic", "thoughtful", "tidy", "tough", "unassuming", "understanding", "versatile", "warmhearted", "willing", "witty"]
select_character_trait_negative = random.choice(fantasy_character_traits_negative)

fantasy_known_for = ["adventuring", "alcohol", "art", "books", "brawling", "brewing", "cooking", "crafting", "dancing", "drinking", "fighting", "gambling", "gardening", "hunting", "jewelry", "music", "painting", "poetry", "reading", "singing", "sleight of hand", "smuggling", "theater", "writing"]
select_known_for = random.choice(fantasy_known_for)

fantasy_desire = ["adventure", "alcohol", "art", "books", "brawling", "brewing", "cooking", "crafting", "dancing", "drinking", "fighting", "gambling", "gardening", "hunting", "jewelry", "music", "painting", "poetry", "reading", "singing", "sleight of hand", "smuggling", "theater", "writing"]
select_desire = random.choice(fantasy_desire)

fantasy_going_to = ["adventure", "alcohol", "art", "books", "brawling", "brewing", "cooking", "crafting", "dancing", "drinking", "fighting", "gambling", "gardening", "hunting", "jewelry", "music", "painting", "poetry", "reading", "singing", "sleight of hand", "smuggling", "theater", "writing"]
select_going_to = random.choice(fantasy_going_to)

fantasy_motivated_by = ["adventure", "alcohol", "art", "books", "brawling", "brewing", "cooking", "crafting", "dancing", "drinking", "fighting", "gambling", "gardening", "hunting", "jewelry", "music", "painting", "poetry", "reading", "singing", "sleight of hand", "smuggling", "theater", "writing"]
select_motivated_by = random.choice(fantasy_motivated_by)

fantasy_unique = ["adventure", "alcohol", "art", "books", "brawling", "brewing", "cooking", "crafting", "dancing", "drinking", "fighting", "gambling", "gardening", "hunting", "jewelry", "music", "painting", "poetry", "reading", "singing", "sleight of hand", "smuggling", "theater", "writing"]
select_unique = random.choice(fantasy_unique)

fantasy_describe_1 = ["tall", "not very tall", "especially not tall", "really, very not-at-all tall"]
select_describe_1 = random.choice(fantasy_describe_1)

fantasy_gender= ["male","female","unclear"]
selected_gender = random.choice(fantasy_gender)

fantasy_body_type = ["slender", "athletic", "stocky", "muscular", "overweight", "obese", "skinny", "thin", "fat", "chubby", "curvy", "petite", "large", "broad", "bony", "gaunt", "lean", "lanky", "lithe", "plump", "portly", "scrawny", "squat", "stout", "stringy", "thin", "willowy", "wiry"]
select_body_type = random.choice(fantasy_body_type)

fantasy_clothing_type =["common clothes", "rather elegant clothes", "pauper's clothes", "well-made and comfortable armor", "travelling robes"]
select_clothing_type = random.choice(fantasy_clothing_type)

fantasy_eye_color= ["amber", "blue", "brown", "gray", "green", "hazel", "red", "violet", "black", "white", "yellow", "orange", "purple", "pink", "gold", "silver", "bronze", "rainbow", "multicolored", "glowing", "glittering", "glowing rainbow", "glowing multicolored", "glittering rainbow", "glittering multicolored"]
select_eye_color = random.choice(fantasy_eye_color)

fantasy_carrying = ["large sack", "small sack", "large backpack", "large box that shakes and growls", "briefcase"]
select_carrying = random.choice(fantasy_carrying)

fantasy_age = ["young", "middle-aged", "old", "ancient"]
select_age = random.choice(fantasy_age)

fantasy_doing = ["sitting at a bar","quietly and peacfully watching", "haggling over some wares", "arguing with a friend", "trying to convince a friend", "eating very quickly"]
select_doing = random.choice(fantasy_doing)


npc_desc = "You observe a " + select_describe_1 + " " + select_body_type + " " + selected_gender + " " + select_doing + ".  " + "They seem " + select_age + " and upon a closer look, you notice " + select_eye_color + " eyes.  " + "They seem to be carrying a " + select_carrying + " and are wearing " + select_clothing_type + ". After a brief conversation, you learn they are very well known for " + select_known_for + ". A bit more conversation, and you learn they are motivated by " + select_motivated_by + ".  " + "In a few days, they plan on travelling to  " + select_city + " hoping to find some jobs or opportunities " + select_desire + ".  " + "You are suprised when you learn they are considered a world-expert in " + select_unique + ".  " + "You get a sense they might be a bit unreasonably " + select_character_trait_negative + "." 


print(npc_desc)
