import matplotlib.pyplot as plt
from sympy import *
from numpy import *
from builtins import str
dif = []
#=================================== X = Segma(dif[j] * PI(x[i + 1] - X[i])) =========================================
def getDifferences(x = [0.0],y = [0.0]):
    it = int((len(y) * (len(y) - 1)) /2);
    length = len(y)
    j = 0
    i = 0;
    k = 1
    l = 0
    for _ in range (0,it,1):
        y.append((y[j+1] - y[j]) / (x[i + k] - x[i]))
        j += 1
        i += 1
        l += 1
        if l is length - k:
            j += 1
            l = 0
            i = 0
            k += 1
            
    differences = []
    j = 1
    i = length
    differences.append(y[0])
    while i < len(y):
        differences.append(y[i])
        i += length - j
        j += 1
    return differences

def getInterpolationValue(value = 0.0 ,x = [0.0]):
    result = 0.0;
    for i in range(0,len(dif),1):
        result += getProperFactor(dif[i], i, value, x)
    return result;

def getProperFactor(differences = 0.0,noMul = 0,value = 0.0,x = [0.0]):
    result = differences
    for i in range(0,noMul,1):
        result *=  (value - x[i])
    return result;

def getFunction(x = [0.0]):
    result = 0.0;
    for i in range(0,len(dif),1):
        result += getProperFactorFunc(dif[i], i, x)
    return result;

def getProperFactorFunc(differences = 0.0,noMul = 0,x = [0.0]):
    result = differences
    value = Symbol('x')
    for i in range(0,noMul,1):
        result *=  (value - x[i])
    return result;
#================================================== Debuging ============================================================
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 2.25, 3.75, 4.25, 10, 5.81, 5.81, 5.81, 5.81, 5.81, 5.81]
yC = y.copy()
dif = getDifferences(x,yC)
xT = []
yT = []
xQueries = [1.5,2.5,3.5]
yQueries = []

sym = Symbol('x')
r = getFunction(x)
poly = Poly(r,sym)

coef = []
for i in poly.coeffs():
    prec = math.log(math.fabs(i))
    if prec > 0:
        coef.append(i.__format__(".2f"))
    else :
        coef.append(i.__format__("."+str(int(math.fabs(prec)) + 1)+"f"))
        
poly = Poly(coef,sym)


step = .00001*(x[len(x) - 1] - x[0])
val = x[0] + step;

#=====================================getting curve========================================
while val <= x[len(x) - 1]:
    xT.append(val)
    yT.append(getInterpolationValue(val, x))
    val = val + step
#============================================getting queries================================

for i in range(0,xQueries.__len__(),1):
    yQueries.append(getInterpolationValue(xQueries[i], x))
#===========================================================plotting all================================
fig, ax = plt.subplots()
ax.plot(xT,yT)
ax.plot(x,y,'ro')
ax.plot(xQueries,yQueries,'k*')

for i in range(0,xQueries.__len__(),1):
    bbox_props = dict(boxstyle="round", fc="cyan",alpha = .1)
    ax.text(xQueries[i], yQueries[i] + .2 * (max(y) - min(y)), r"(" + str(xQueries[i]) + ", " + str(yQueries[i].__format__(".2f")) + ")", horizontalalignment='center',verticalalignment='center', fontsize=7, color="black",bbox = bbox_props)

ax.text((min(x) + max(x) )/2,min(yT),"P(x) = " + str(poly)[5:-17],horizontalalignment='center',verticalalignment='top',fontsize = 10,color="blue")
ax.text((min(x) + max(x) )/2,max(yT),"Newton",horizontalalignment='center',verticalalignment='bottom',fontsize = 15,color="blue")

plt.xlabel("x")
plt.ylabel("f(x)")  
plt.show()
