import random as r

# empty list
a = []

# add something to list
# .append() adds to the end, only takes one argument
a.append(4)
a.append(5)
a.append(6)

# ways to append at the front
a.insert(0,1)
a = [1] + a

print(a[0], a[4])

# a[7] wouldn't work, list index error

# print(a)

b = [1,1,4,5,3]
# remove function looks for the integer, not the position
# b.remove(2)
# print(b)

del b[0] # deletes the first position list item
print(b)

# pop grabs the last thing in the list
print(b.pop())
print(b)

# last thing in the list
print(b[len(b)-1])
print(b[2])
print(b[-1]) # same thing as b[2] in a three item list

c = 5
d = 7

c, d = 5, 7
c, d = d, c # swap

# other solution of switching the values
# swap
temp = c
c = d
d = temp

e = [1, 2, 3, 7, 5, 6, 4]

e[3], e[6] = e[6], e[3]

print(e)

# make a list of first 100 numbers evenly divisible by 7

f = []
for x in range(7,707,7):
	f.append(x)
print(f)
print(len(f))

g = []
for x in range(10):
	g.append(r.randrange(100))
# sort from ascending order
# g.sort()
# print(sorted(g))
# print(g)
# g.sort() actually changes the g list, but sorted is just a momentary function that sorts it

g = sorted(g)
print(g)




