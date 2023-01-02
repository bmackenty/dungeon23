# this file will procedurally generate complex weather patterns for the game
# it will be called by the main game loop and will return a weather object

import random
import os
os.system("clear")



# weather types
weather_types = [["clear","clear"], ["rainy","rain"], ["snowy","snow"], ["hailing","hail"], ["stormy","storm"], ["foggy","fog"], ["windy","wind"]]
selected_weather = random.choice(weather_types)

# weather intensity
weather_intensity = random.randint(1, 10)
selected_intensity = weather_intensity
if selected_intensity == 1:
    selected_intensity_description = "light"
elif selected_intensity == 2:
    selected_intensity_description = "moderate"
elif selected_intensity == 3:
    selected_intensity_description = "heavy"
elif selected_intensity == 4:
    selected_intensity_description = "extreme"
elif selected_intensity == 5:
    selected_intensity_description = "severe"
elif selected_intensity == 6:
    selected_intensity_description = "violent"
elif selected_intensity == 7:
    selected_intensity_description = "catastrophic"
elif selected_intensity >= 8:
    selected_intensity_description = "apocalyptic"



# weather duration
weather_duration = random.randint(2, 10)
selected_duration = weather_duration

# weather temperature
weather_temperature = random.randint(-20, 40)
selected_temperature = weather_temperature

# weather wind
weather_wind = random.randint(1, 10)
selected_wind = weather_wind
if selected_weather[0] == "windy":
    selected_wind = random.randint(40, 90)


weather_description_1 = "For more than " + str(selected_duration) + " days, the weather has been " + str(selected_weather[0]) + " with a temperature of " + str(selected_temperature) + " degrees and a wind speed of " + str(selected_wind) + " kilometers per hour."

print(weather_description_1)
if selected_intensity > 2 and selected_weather[0] != "clear":
    print("The intestity of the " + str(selected_weather[1]) + " is " + str(selected_intensity_description) + ".  Many people have been injured and killed by the " + str(selected_weather[1]) + ", and few remember it ever being this bad.")


