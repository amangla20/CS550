''' Instructions:
   Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''
import random
''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''
faveNums = [3,4,5]
 
 
''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''
holidays = ["Christmas", "Diwali", "New Year's", "Hanukkah", "Kwanzaa", "Thanksgiving", "Easter", "Holi", "Halloween", "MLK Jr. Day", "Pi Day", "Mother's Day", "Father's Day", "St. Patrick's Day"]
 
 
''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''
grades = ['A', 'B', 'C', 'D', 'F']
 
 
''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
funny = []
for i in range(18):
   funny.append(True) 
 
 
''' 5. 
   Create a list of doubles, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''
salaries = [100000, 80000, 30000, 45000, 1000000]
numEmployees = len(salaries)
 
 
''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''
x = 100
y = 100
grayscale = []
for i in range (x*y):
   grayscale.append(random.randint(0,255)) 
 
 
''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''
noSiblings = 3
oneSibling = 1
twoSiblings = 2
threeSiblings = 0

names = ["","","","","",""] 

if len(names) == noSiblings + oneSibling + twoSiblings + threeSiblings:
   pass
else:
   print("Not enough names in the list!")
 
 
''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''
months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
 
 
''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
 
 
''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
booleanvariable = [True, False]
 
''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
dorms = ["Memorial House", "Nichols", "Pitman", "Squire"]
 
''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
randomnumbers = []

for i in range(3):
   randomnumbers.append(random.random())

print(randomnumbers)

''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spades), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['S', 'H', 'C', 'D']
deck = []
for c in cards:
   for s in suits:
      deck.append(c+s)
print(deck)
 
 
''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''
Yahtzee = []
for i in range(5):
   Yahtzee.append(random.randint(0,6))
if Yahtzee[0] ==  Yahtzee[1] and Yahtzee[0] ==  Yahtzee[2] and Yahtzee[0] ==  Yahtzee[3] and Yahtzee[0] ==  Yahtzee[4]:
   print ("Yahtzee")
else:
   print("Try again.")
 
 
''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''
numbers = [4, 6, 9, 19, 10, 3, 46, 27, 87]
for n in range(len(numbers)):
   if numbers[n]%3 == 0:
      if numbers[n-1]%2 == 0:
         if numbers[n+1]%2 == 1:
            print("position " + str(n) + ": " + str(numbers[n-1]) + ", " + str(numbers[n]) + ", " + str(numbers[n+1]))

 
 
''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''
saddlepoint = ["No saddlepoint"]
board=[[random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)] for i in range(5)]
for i in range(5):
   print(*board[i])
for x in range(5):
   for y in range(5):
      if board[x][0] <= board[x][y] and board[x][1] <= board[x][y] and board[x][2] <= board[x][y] and board[x][3] <= board[x][y] and board[x][4] <= board[x][y]:
         if board[x][y] <= board[0][y] and board[x][y] <= board[1][y] and board[x][y] <= board[2][y] and board[x][y] <= board[3][y] and board[x][y] <= board[4][y]:
            saddlepoint.append(board[x][y])
            saddlepoint.remove("No saddlepoint")
print(saddlepoint)
 
 
''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''
board = [[0]*8 for x in range(8)]

for i in range(2):
   x = random.randint(0,7)
   y = random.randint(0,7)
   board[y][x] = 1

for y in range(8):
   for x in range(8):
      print(board[y][x], end=" ")
   print("")
 
 
''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''
mylist = [3, 5, 9]
mylist.reverse()
print(mylist) 
 
''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''
doorknobs = ["string", "string2", "hi", "world", "what"]

doorknobs[1], doorknobs[3] = doorknobs[3], doorknobs[1]

print(doorknobs)
 
 
''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''
numbers = [3, 6, 9, 7]
greatest = numbers[0]
for i in range(len(numbers)):
   if greatest < numbers[i]:
      greatest = numbers[i]
numbers.remove(greatest)
numbers.append(greatest)
print(numbers)
 
 
 
''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''
w = 10
h = 10

board = [[0]*w for x in range(h)]
for y in range(h):
   for x in range(w):
      board[y][x] = random.randint(1,100)

for y in range(h):
   for x in range(w):
      if board[y][x]%2 == 1:
         if board[y][x] < 10:
            board[y][x] = 2
         else:
            board[y][x] = 22
      if board[y][x] < 10:
         print(board[y][x],end="  ")
      elif board[y][x] > 99:
         print(board[y][x],end="")
      else:
         print(board[y][x],end=" ")
   print("")
 
 
''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''

 
 
''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''
shifters = [1, 2, 3, 4, 5]
x = shifters[0]
for i in range(len(shifters)):
   if i < len(shifters) - 1:
      shifters.append(shifters[1])
   else:
      pass  
   shifters.remove(shifters[0])
   
shifters.append(x)
print(shifters)
 
 
''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''
 
  
 
''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''
rankings = [80, 30, 29, 18, 1, 99, 38, 50, 26, 67]
above_average = []
total = len(rankings)
rsum = 0
for r in rankings:
   rsum += r
average = rsum/total
for r in rankings:
   # in this case, the lower the ranking is, the better (so number 1 means you are the best in the school)
   if r < average:
      above_average.append(r)

print(len(above_average)/total)
 
 
''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''
 
 
 
'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''
nums = []
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
avecount = []
for y in range(100):
   for i in range(100):
      nums.append(random.randint(1,10))
   for n in nums:
      for x in range(1,11):
         if n == x:
            count[x - 1] += 1

for c in count:
   average = c/100
   avecount.append(average)

asum = 0
for a in avecount:
   asum += a
average = asum/len(avecount)
print(average)
# keep getting 505.0
 
''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/
'''