#This file purely exists for development purposes such that I can test methods and functions as they are implemented.

from linalgebralib import LinAlgebraLib as la

A = la.Matrix(content=[[1,1,3],[-1,3,1],[1,2,4]])
b = la.columnVector(contents=[3,2,1])
x_bar = (la.columnVector(contents=[7/3,14/3,-7/3]))
y_bar = (la.columnVector(contents=[1,2,-1]))

print(la.magnitude(b-x_bar))
print(la.magnitude(b-y_bar))

#TODO: Implement vector projections, unit vectors, cross product.

#Changlog: Fixed matrix multiplication with column vectors and row vectors where matrix is multiplied on the left.