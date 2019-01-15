# Anjali Mangla
import random
import math
import matplotlib.pyplot as plt
from collections import Counter

# simulation WITH colorful graphs? combining options 1 and 2?

# simulation ideas: what is the chance that based on how many times you travel and where you travel that you will catch a certain disease? and then also graph the data set really colorfully? or child slavery data set?

# how much time would it take to lose 40 pounds for a female?

# one pound is 3,500 calories, and you should be pacing yourself to lose about 1-2 pounds a week. This means you should burn 3,500 calories a week
# using the formula online: https://www.google.com/search?q=calculating+bmr+formula&oq=calculating+bmr+formula&aqs=chrome..69i57j0l5.4805j0j1&sourceid=chrome&ie=UTF-8
# activity level: https://www.livestrong.com/article/146691-calorie-calculator-for-your-ideal-weight/
# Harris-Benedict Formula
# account for the fact that it gets harder and harder to lose weight as you lower in weight because you have to continue to eat less and less
# Women: BMR = 655 + ( 4.35 x weight in pounds ) + ( 4.7 x height in inches ) - ( 4.7 x age in years )
trials = 100

results = []
cal = 0
days = 0
pound = 3500*cal
week = 7*days
month = 4 * week
desired_weight = current_weight - 40
bmr = 655 + (4.35 * current_weight) + (4.7 * height) - (4.7 * age)
for i in range(trials):



"""
for i in range(trials):
	party = random.randint(1, 13)
	total_calories = 0
	for j in range(party):
		servings = random.randint(1, 8)
		for k in range(servings):
			calories = random.randint(40, 500)
			total_calories += calories
	calories_results.append(total_calories)
	total_calories = 0

results = sorted(Counter(calories_results).items())
print(results)

graph_data = []

x_data = []

for tuples in results:
	graph_data.append(tuples[1])
	x_data.append(tuples[0])

plt.plot(x_data, graph_data)
plt.show()
"""





