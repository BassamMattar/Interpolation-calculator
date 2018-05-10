from Model import Interpolation
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 2.25, 3.75, 4.25, 10, 5.81, 5.81, 5.81, 5.81, 5.81, 5.81]
xQueries = [1.5, 2.5, 3.5]
m = 1
newInterpolation = Interpolation.MyClass(newX = x, newY = y, newXQueries = xQueries,newMethod = m)
newInterpolation.interpolate();

newInterpolation.interpolate();