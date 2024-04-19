#This file purely exists for development purposes such that I can test methods and functions as they are implemented.

from linalgebralib import LinAlgebraLib as la

A = la.Matrix(content=[[1,0,0],[0,1,0],[0,0,1]])
b = la.Matrix(content=[[1],[2],[3]])
l = la.columnVector(contents=[1,2,3])
print((A*b+l).contents)


#TODO: Implement vector projections, unit vectors, cross product.

#Changlog: Fixed matrix multiplication with column vectors and row vectors where matrix is multiplied on the left.