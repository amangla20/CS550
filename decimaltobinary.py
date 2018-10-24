import math
import sys

binarynum = sys.argv[1]

def toDecimal(binarynum):
	i = 0
	number = 0
	binarynum = binarynum[::-1]
	for num in binarynum:
		number += int(num)*2**i
		i += 1
	print(number)

toDecimal(binarynum)


# with 1101 should answer 13