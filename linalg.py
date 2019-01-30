import numpy

array1 = numpy.array([[1, 2], [4, 5], [7, 8]])
array2 = numpy.array([[1, 2, 3], [4, 5, 6]])

# calculates the dot product of two arrays, outputting as one array with the dot products
dot_product = numpy.dot(array1, array2)
print(dot_product)

# multiplies arrays as matrices
mat_mul = numpy.matmul(array1, array2)
print(mat_mul)

# dot product and matrix multiplication yield the same result

# calculates the determinant of an array
array3 = numpy.array([[3, 6], [17, 89]])
determinant = numpy.linalg.det(array3)
print("determinant of array1:", determinant)

