import random
import os
os.system("clear")

#   Variables start

#   Paragraph 1 start

time = str(random.randint(500, 1500))
age = str(random.randint(11, 18))

location_1 = ["Hill", "Bear", "Ghost", "Emerald", "Lake", "River", "Sun", "Wind", "Dark", "Moon", "New", "Heaven", "South"]
selected_location_1 = random.choice(location_1)

location_2 = ["dale", "wood", " Ville", "land", " Springs"]
selected_location_2 = random.choice(location_2)

environment = ["tall mountains", "windy hills", "magnificent sunrises", "rainy climate", "blue skies", "gloomy weather", "high temperatures in the summer", "majestic lakes", "picturesque sunsets", "deep rivers", "fragrant fields", "fragrant lavender fields", "dark forests", "sunny beaches"]
selected_environment = random.choice(environment)

era = ["Tiger", "Snake", "Dragon", "Silence", "Shadows", "Pyramids"]
selected_era = random.choice(era)

character = ["Krios", "Tavros", "Didimoi", "Karkinos", "Parthenos", "Zigos", "Skorpios", "Toksotis", "Aigokeros", "Idrochoos", "Ichthis"]
selected_character = random.choice(character)

profession = ["wizard", "sorcerer", "fortuneteller", "hypnotist", "astrologer", "occultist"]
selected_profession = random.choice(profession)

gender = ["he", "she"]
selected_gender = random.choice(gender)

if selected_gender == "he":
        pronoun1 = "him"
        pronoun2 = "his"
elif selected_gender == "she":
        pronoun1 = "her"
        pronoun2 = "her"

kingdom = ["Ares", "Athena", "Zaus", "Aphrodite", "Hephaestus", "Demeter", "Enyo", "Hebe", "Heracles", "Vulcan", "Juventas", "Abraxas", "Aether", "Aion", "Typhon", "Zephyrus"]
selected_kingdom = random.choice(kingdom)

ability = ["teleport", "read minds", "be invisible", "levitate", "read memories", "see spirits", "stop time", "control the weather", "time travel", "", ""]
selected_ability = random.choice(ability)

#   Paragraph 1 end

#   Paragraph 2 start

direction1 = ["South", "North"]
selected_direction1 = random.choice(direction1)

direction2 = ["west", "east"]
selected_direction2 = random.choice(direction2)

continent = ["Asia", "Europe", "South America", "North America", "Australia", "Africa"]
selected_continent = random.choice(continent)

place = [" on the top of a mountain", " near a lake", " in a valley"]
selected_place = random.choice(place)

dependency = ["independent", "dependent from UK", "dependent from Albania"]
selected_dependency = random.choice(dependency)
if selected_dependency == "independent":
    story_9 = "It is independent from any other country and has its own governing and justice system."
elif selected_dependency == "dependent from UK":
    story_9 = "However, it is one of the Commonwealth Realms ruled over by the British monarchy."
elif selected_dependency == "dependent from Albania":
    story_9 = "It is considered a part of Albania, even though it has its own governing and justice system."

language = ["Elvish", "Klingon", "Minionese", "Na'vi", "Dothraki", "Valyrian", "Quenya", "Sindarin","Lapine", "Atlantean", "Vulcan", "Huttese", "Kryptonian", "Dovahzul", "Goa'uld", "Trigedasleng", "D'ni", "Tenctonese"]
selected_language = random.choice(language)

if selected_language == "Klingon":
    story_11 = "In this dialect of the Klingon language, a phrase 'bIpIv'y'?' means mean 'How are you?'"
elif selected_language == "Na'vi":
    story_11 = "'Kaltxì' would mean 'Hello' and 'nga jawne lu oer' means 'I love you' in this dialect of Na'vi."
elif selected_language == "Sindarin":
    story_11 = "If you would want to ask someone if they speak Elvish, you could say 'Pedil edhellen?' in this dialect of Sindarin."
elif selected_language == "Quenya":
    story_11 = "'Man esselya ná?' would mean 'What's your name' in this dialect of Quenya."
elif selected_language == "Valyrian":
    story_11 = "In this dialect of Valyrian, to say 'I love you,' you could say 'Avy yorrāelan.'"
elif selected_language == "Dothraki":
    story_11 = "To say 'Thank you,' you could say 'San athhomari yerân!' in this dialect of Dothraki."
else:
    story_11 = "Unfortunately, the language has been cursed by the native species so it cannot be translated into English."

#   source for fictional languages and phrases: https://www.berlitz.com/blog/fictional-fantasy-languages-conlangs

human_language = ["Italian", "English", "Spanish", "Finnish", "Greek", "Latin", "Turkish", "Irish", "Tagalog"]
selected_human_language = random.choice(human_language)

religion = {
    1: "believes in many Gods.", 
    2: "believes in one God, to whom they pray at least twice a day.", 
    3: "does not believe in any Gods.",
    4: "lost their faith over time.",
    5: "considers itself believers but not practicioners.",
    6: "does not believe in God but there are many minorities that do.",
    7: "believes in five dieties, whom they often pray to.",
    8: "does not believe in any dieties.",
    9: "believes in four dieties, whom they often pray to.",
    10: "believes in three dieties, whom they often pray to."
}
selected_religion = random.choice(list(religion.values()))

if selected_religion == "believes in many Gods.":
    selected_conjunction = ", however"
elif selected_religion == "believes in one God, to whom they pray at least twice a day.":
    selected_conjunction = ", however"
elif selected_religion == "believes in five dieties, whom they often pray to.":
    selected_conjunction = ", however"
elif selected_religion == "does not believe in any Gods.":
    selected_conjunction = " so"
elif selected_religion == "their faith faded over time.":
    selected_conjunction = " because"
elif selected_religion == "considers itself believers but not practicioners.":
    selected_conjunction = " and"
elif selected_religion == "does not believe in God but there are many minorities that do.":
    selected_conjunction = " and"
elif selected_religion == "does not believe in any dieties.":
    selected_conjunction = " and therefore"
elif selected_religion == "believes in four dieties, whom they often pray to.":
    selected_conjunction = " but now"
elif selected_religion == "believes in three dieties, whom they often pray to.":
    selected_conjunction = " but now"

decision = ["is very", "is relatively", "is not very", "is not"]
selected_decision = random.choice(decision)

technology = [""]
selected_technology = random.choice(technology)

if selected_decision == "is very":
    story_14 = "The most popular "
elif selected_decision == "is relatively":
    story_14 = "miejscoość"
elif selected_decision == "is not very":
    story_14 = "wieś"
elif selected_decision == "is not": 
    story_14 = "las"

values = [""]
selected_values = random.choice(values)

law = [""]
selected_law = random.choice(law)

custom_one = [""]
selected_custom_one = random.choice(custom_one)

custom_two = [""]
selected_custom_two = random.choice(custom_two)

adj_one = [""]
selected_adj_one = random.choice(adj_one)

adj_two = [""]
selected_adj_two = random.choice(adj_two)

adj_three = [""]
selected_adj_three = random.choice(adj_three)

#   Paragraph 2 end

#   Paragraph 3 start

magic_type = ["necromancy", "transmutation", "astrology", "alchemy", "enchantment", "animancy"]
selected_magic_type = random.choice(magic_type)

transformation = {
    1: "can only be inherited from the mother's side.", 
    2: "can only be inherited from the father's side.", 
    3: "can be inherited or acquired through consumption of a potion that can be made by only two people in the entire world.",
    4: "can inherited from even one of the parents but there are many exceptions.",
    5: "is obtained at birth, no matter the family history.",
    6: "can be inherited or achieved by practicing sorcery and consuming a specific type of poison.",
    7: "can be inherited or earned.",
    8: "can only be inherited.",
    9: "is passed down from generation to generation."
}
selected_transformation = random.choice(list(transformation.values()))

if selected_magic_type == "necromancy":
    story_101 = "Necromancy allows one to manipulate the forces of death, for example by reanimating corpses."
elif selected_magic_type == "transmutation":
    story_101 = "Transmutation is the power to turn living things into non-living things and vice-versa."
elif selected_magic_type == "astrology":
    story_101 = "Astrology, the study of astronomical concepts and a type of celestial magic, allows one to cast spells based on horoscopes."
elif selected_magic_type == "alchemy":
    story_101 = "Alchemy is actually not science nor magic, because it is about transformation by making potions, magical items, or making permanent changes on the state of matter."
elif selected_magic_type == "Enchantment":
    story_101 = "Enchantment is used to control the feelings or remotions of other human beings."
elif selected_magic_type == "animancy":
    story_101 = "Animancy allows one to manipulate living forces."

magic_limitations = [""]
selected_magic_limitations = random.choice(magic_limitations)

magic_rules = [""]
selected_magic_rules = random.choice(magic_rules)

#   Paragraph 3 end

#   Variables end



#   Story start

story_1 = "The legend has it that " + time + " years ago, in the land of " + selected_location_1 + selected_location_2 + " known for its " + selected_environment + ", happened something that would be remembered for years to come."

story_2 = "It is said that the new Age of " + selected_era + " began with the arrival of " + selected_character + ", a well-known and respected " + selected_profession + "."

story_3 = "As a child, " + selected_gender + " was very fortunate to have a big, loving family and a happy childhood. However, " + selected_gender + " was raised in a very secular environment in the Kingdom of " + selected_kingdom + ", so after discovering " + pronoun2 + " ability to " + selected_ability + " at the young age of " + age +  ", " + selected_gender + " got disowned by " + pronoun2 + " own family and was forced to move away."

story_4 = "With no place to live, " + selected_gender + " traveled around the world and practiced " + pronoun2 + " magical skills to become one of the most powerful " + selected_profession + "s to ever exist. It was " + selected_gender + ", who introduced the revolutionary idea of using magic powers for good at the time when witches were burned at the stake."

story_5 = "Staying true to " + pronoun2 + " beliefs, " + selected_gender + " founded the first school of magic on land that belonged to the town that was later called " + selected_location_1 + selected_location_2 + "."

story_6 = time + " years later, the once small village known for its beautiful surroundings and " + selected_environment + " is the most populous town inhabited by magical creatures, spirits, and " + selected_profession + "s."

story_7 = "The Academy, the school of magic founded by " + selected_character + ", is still considered the most prestigious school of magic in the world."

story_8 = "The town is located in the " + selected_direction1 + selected_direction2 + " of " + selected_continent + selected_place + " and is unlike any other town in this region." 

story_10 = "Inhabited by many magical creatures, its official language is a " + selected_direction1 + selected_direction2 + "ern dialect of " + selected_language + " but creatures that are considered government officials can also speak " + selected_human_language + " to communicate with the governments of other countries."

story_12 = "When it comes to faith, the town was not always very religious" + selected_conjunction + " the majority of the polulation " + selected_religion

story_13 = selected_location_1 + selected_location_2 + selected_decision + " technologically developed."

story_15 = "values" 

story_16 = "Strange customs" 

story_17 = "" 

story_18 = "" 

story_100 = "The primary type of magic practiced in " + selected_location_1 + selected_location_2 + " is " + selected_magic_type + ", which " + selected_transformation

#   Story end

print()

print(story_1, story_2, story_3, story_4, story_5, story_6, story_7) 

print()

print(story_8, story_9, story_10, story_11, story_12, story_13, story_14, story_15, story_16, story_17)

print()

print(story_100, story_101)
