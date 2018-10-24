def moves(n, left):
	print("here " + str(n))
	if n  == 0:
		return #return tells the function to go back and do what it put on 'pause'
	moves(n-1,not left)
	print("here1 " + str(n))
	if left:    
		print(str(n)+' left')
	else:    
		print(str(n)+' right')
	print("here2 " + str(n))
	moves(n-1,not left)

print(moves(3, True))
#moves(3,True) moves(2,False) moves(1, True)