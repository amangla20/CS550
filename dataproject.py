# Anjali Mangla
# 1/16/2019
# Sources are given below.
# On my honor, I have neither given nor received unauthorized aid.
import random
import math
import matplotlib.pyplot as plt
from collections import Counter

# How much time would it take to lose 20-50 pounds for a female following a strict calorie counting diet?

# one pound is 3,500 calories
# using the formula online, Harris-Benedict Formula: https://www.google.com/search?q=calculating+bmr+formula&oq=calculating+bmr+formula&aqs=chrome..69i57j0l5.4805j0j1&sourceid=chrome&ie=UTF-8
# activity level: https://www.livestrong.com/article/146691-calorie-calculator-for-your-ideal-weight/
# account for the fact that it gets harder and harder to lose weight as you lower in weight because you have to continue to eat less and less
# Women: BMR = 655 + ( 4.35 x weight in pounds ) + ( 4.7 x height in inches ) - ( 4.7 x age in years )

trials = 10000

time_results = []
days = 0
calories_lost = 0
for i in range(trials):
	days = 0
	calories_cut_per_day = 0
	calories_lost = 0
	# current weight can be between 130 pounds and 500 pounds
	current_weight = random.randint(130, 500)
	starting_weight = current_weight
	desired_weight = current_weight - random.randint(20, 50)
	# heights of 4 feet 8 inches to 6 feet 6 inches
	height = random.randint(56, 78)
	# weight loss of 40 pounds should only be happening in women of a substantial age, like a normal ten year-old wouldn't worry about nor probably be able to lose 40 pounds.
	# women usually gain weight until age 65, and afterwards begin to lose weight (naturally) so the upper limit of age will be 65, and the younger limit be a teen.
	age = random.randint(13, 65)
	# different activity levels, randomized.
	activity = random.randint(0, 4)
	if activity == 0:
		# sedentary
		activity_factor = 1.2
	elif activity == 1:
		# lightly active
		activity_factor = 1.375
	elif activity == 2:
		# moderately active
		activity_factor = 1.55
	elif activity == 3:
		# very active
		activity_factor = 1.725
	elif activity == 4:
		# extra active
		activity_factor = 1.9
	bmr = 655 + (4.35 * desired_weight) + (4.7 * height) - (4.7 * age)
	calories_desired = bmr * activity_factor
	while current_weight > desired_weight + 10:
		# calculate bmr of current weight to get the number of calories needed to maintain your current weight
		bmr = 655 + (4.35 * current_weight) + (4.7 * height) - (4.7 * age)
		calories_maintaining = bmr * activity_factor
		# assume the woman will go on a strict diet of eating only up to the calories needed to maintain the desired weight every day (one way of doing)
		#calories_per_day = calories_maintaining - random.randint(500, 1000)
		#calories_lost += random.randint(500, 1000)
		calories_cut_per_day = calories_maintaining - calories_desired
		
		calories_lost += calories_cut_per_day
		days += 1
		# increment days and change current weight
		current_weight = starting_weight - (calories_lost/3500)

		# 1 pound is 3500 calories. 
		# pounds = calories_lost / 3500
		# if pounds >= 1:
		# 	current_weight -= pounds
		# 	calories_lost = 0
		"""
		if pounds >= 1:
			current_weight -= pounds
			calories_lost = 0
		"""
	# days/30 is how many months, approximately.
	time_results.append(days/30)
results = sorted(Counter(time_results).items())
# create y axis and x axis ranges
graph_data = []

x_data = []

for tuples in results:
	graph_data.append(tuples[1])
	x_data.append(tuples[0])

# Info on manipulating matplotlib: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.xlabel.html and Matplotlib documentation
plt.plot(x_data, graph_data, color="purple", linestyle = '--')
plt.xlabel("Months")
plt.ylabel("Frequency")
plt.title("Amount of Time in Months Required For a Woman to Lose 20-50 Pounds")
plt.show()


"""
Multiply your BMR by the appropriate activity factor, as follows:
Sedentary (little or no exercise): BMR x 1.2
Lightly active (light exercise/sports 1-3 days/week): BMR x 1.375
Moderately active (moderate exercise/sports 3-5 days/week): BMR x 1.55
Very active (hard exercise/sports 6-7 days a week): BMR x 1.725
Extra active (very hard exercise/sports & physical job or 2x training): BMR x 1.9
"""





