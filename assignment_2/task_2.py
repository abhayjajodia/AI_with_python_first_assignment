import numpy as numpy
import matplotlib.pyplot as pyplot


x = numpy.arrange(1, 10)

y = numpy.array([-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])

pyplot.figure()

pyplot.scatter(x, y, marker="+", label="Scatering points")
pyplot.title('Scater point')
pyplot.xlabel('x-axis')
pyplot.ylabel('y-axis')


pyplot.grid(True)
pyplot.show()