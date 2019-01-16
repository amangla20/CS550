
'''
This Monte Carlo simulator makes a guess at how many calories you will consume in cookies at holiday parties. It assumes that you will attend somewhere from 1-10 parties, and that you will eat 2-8 cookies, and that each cookie will contain anywhere from 40-200 calories. It then charts the possible outcomes using matplotlib.
'''

import random
from collections import Counter
import matplotlib.pyplot as plt

calories_results = []

for k in range(10000):
	num_parties = random.randint(1,10)
	total_calories = 0
	for j in range(num_parties):
		num_cookies = random.randint(2,8)
		for i in range(num_cookies):
			calories_per_cookie = random.randint(40,200)
			total_calories += calories_per_cookie
	calories_results.append(total_calories)

results = sorted(Counter(calories_results).items())
print(results)
graph_data = []
x_data = []
for tuples in results:
	graph_data.append(tuples[1])
	x_data.append(tuples[0])

plt.plot(x_data,graph_data)
plt.show()

