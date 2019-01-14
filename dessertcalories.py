import random
from collections import Counter
import matplotlib.pyplot as plt

trials = 1000000


calories_results = []

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

