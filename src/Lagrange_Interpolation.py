import matplotlib.pyplot as plt
from sympy import *
from numpy import *
from builtins import str
import time


def getInterpolationValue(value=0.0, x=[0.0], y=[0.0]):
    result = 0.0
    for i in range(0, len(y), 1):
        result += getValueOfP(value, x, y, i)
    return result


def getValueOfP(value=0.0, x=[0.0], y=[0.0], i=0.0):
    result = y[i]
    for j in range(0, len(y), 1):
        if j is i:
            continue
        result *= (value - x[j]) / (x[i] - x[j])
    return result


def getFunction(x=[0.0], y=[0.0]):
    result = 0
    for i in range(0, len(y), 1):
        result += getValueOfMultiplyingOuts(x, y, i)
    return result


def getValueOfMultiplyingOuts(x=[0.0], y=[0.0], i=0.0):
    value = Symbol('x')
    result = y[i]
    for j in range(0, len(y), 1):
        if j is i:
            continue
        result *= (value - x[j]) / (x[i] - x[j])
    return result


startTime = time.time()
xT = []
yT = []
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 2.25, 3.75, 4.25, 10, 5.81, 5.81, 5.81, 5.81, 5.81, 5.81]
xQueries = [1.5, 2.5, 3.5]
yQueries = []

sym = Symbol('x')
r = getFunction(x, y)
poly = Poly(r, sym)

coef = []
for i in poly.coeffs():
    prec = math.log(math.fabs(i))
    if prec > 0:
        coef.append(i.__format__(".2f"))
    else :
        coef.append(i.__format__("." + str(int(math.fabs(prec)) + 1) + "f"))
        
poly = Poly(coef, sym)

step = .00001 * (x[len(x) - 1] - x[0])
val = x[0] + step;
while val <= x[len(x) - 1]:
    xT.append(val);
    yT.append(getInterpolationValue(val, x, y))
    val = val + step
#============================================getting queries================================

for i in range(0, xQueries.__len__(), 1):
    yQueries.append(getInterpolationValue(xQueries[i], x, y))

fig, ax = plt.subplots()
ax.plot(xT, yT,'gold')
ax.plot(x, y, 'ro')
ax.plot(xQueries, yQueries, 'k*')

for i in range(0, xQueries.__len__(), 1):
    bbox_props = dict(boxstyle="round", fc="cyan", alpha=.1)
    ax.text(xQueries[i], yQueries[i], "\n(" + str(xQueries[i]) + ", " + str(yQueries[i].__format__(".2f")) + ")", horizontalalignment='center', verticalalignment='top', fontsize=7, color="black", bbox=bbox_props)

ax.text((min(x) + max(x)) / 2, min(yT), "P(x) = " + str(poly)[5:-17], horizontalalignment='center', verticalalignment='top', fontsize=10, color="blue")
ax.text((min(x) + max(x)) / 2, max(yT), "Lagrange", horizontalalignment='center', verticalalignment='bottom', fontsize=15, color="blue")

plt.xlabel("x")
plt.ylabel("f(x)")  
print("Execution Time: " + str((time.time() - startTime)) + " S")
plt.show()
