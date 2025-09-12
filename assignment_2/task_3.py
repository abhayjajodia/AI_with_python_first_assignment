import numpy as numpy
import matplotlib.pyplot as pyplot
import pandas as pd

data = pd.read_csv('weight-height.csv', skiprows=1, names=['x','y'])

height= data['x']
weight= data['y']

height_in_cm = height * 2.54
weight_in_kg = weight *0.453592

heigh_mean = numpy.mean(height_in_cm)
weight_mean = numpy.mean(weight_in_kg)


pyplot.hist(height_in_cm, bins=10, color='red',edgecolor='gray')

pyplot.title('Graph')
pyplot.legend()
pyplot.grid(True)
pyplot.show()