import numpy as numpy

A = numpy.array([[1, 2, 3],  [0, 1, 4],   [5, 6, 0]])

A_inv = numpy.linalg.inv(A)
print("Inverse of A:    \n  ", A_inv)

I1 = numpy.dot(A, A_inv)
I2 = numpy.dot(A_inv, A)

print("A * A_inv:\n\n", numpy.round(I1, 2))
print("A_inv * A:\n\n\n", numpy.round(I2, 2))
