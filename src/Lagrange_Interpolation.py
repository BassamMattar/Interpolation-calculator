import matplotlib.pyplot as plt



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


xT = []
yT = []
x = [0, 1, 2, 3, 4,5,6,7,8,9,10,11]
y = [1, 2.25, 3.75, 4.25, 5.81, 5.81, 5.81, 10, 5.81, 5.81, 5.81,5.81]
xQueries = [1.5, 2.5, 3.5]
yQueries = []

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
ax.plot(xT, yT)
ax.plot(x, y, 'ro')
ax.plot(xQueries, yQueries, 'k*')

for i in range(0, xQueries.__len__(), 1):
    bbox_props = dict(boxstyle="round", fc="cyan",alpha = .1)
    ax.text(xQueries[i], yQueries[i] + .2 * (max(y) - min(y)), r"(" + str(xQueries[i]) + ", " + str(yQueries[i].__format__(".2f")) + ")", horizontalalignment='center',verticalalignment='center', fontsize=7, color="black",bbox = bbox_props)

plt.xlabel("x")
plt.ylabel("f(x)")  
plt.show()
