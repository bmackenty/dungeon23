# this is a quest generator for a RPG game
# it generates a quest based on the player's level
# it generates a quest based on the player's class
# every quest has a reward
# every quest has a penalty
# every quest has a time limit
# every quest has a difficulty level
# every quest has a location
# every quest has a quest giver
# every quest has a quest taker
# every quest has a quest description
# every quest has a quest objective
# every quest has a consequence for failure
# every quest has a consequence for success




import random
import os
import time
import sys
os.system("clear")

# this is the player's level
player_level = 1

# this is the player's class
player_class = "warrior"

quest_category = ["fetch","escort","kill","rescue","retrieve","return","defend","protect","find","learn","deliver","steal","destroy","capture","investigate","gather","craft","collect"]
selected_quest_category = random.choice(quest_category)

quest_target = ["item","person","location","creature","object","artifact","animal","monster"]
selected_quest_target = random.choice(quest_target)

quest_reward = ["gold","item","artifact","information","knowledge","experience","reputation","favor","power","magic","spell","skill","ability","status","title","position","rank","honor","respect","praise","recognition","fame","infamy","glory","wealth","riches","treasure","jewels","gems","money","currency","coins","loot","reward","prize","award","bounty","bonus","gift","favor","gratitude","thanks","appreciation","recognition","reciprocity","reciprocation","return","exchange","trade","barter","deal","transaction","exchange","compensation","payment","donation","contribution","concession","conveyance","transfer","delivery","handover","handing over","giving","granting","bestowal","bestowment"]
selected_quest_reward = random.choice(quest_reward)



