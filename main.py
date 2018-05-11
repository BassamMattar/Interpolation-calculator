from model import FileReader, Interpolation

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 2.25, 3.75, 4.25, 10, 5.81, 5.81, 5.81, 5.81, 5.81, 5.81]
xQueries = [1.5, 2.5, 3.5]
#reader = FileReader.MyClass("C:\\Users\\ecc\\Desktop\\interpolation.txt")
#m,x,y,xQueries = reader.getResult()
generalInterpolation = Interpolation.MyClass(newX = x, newY = y, newXQueries = xQueries,newMethod = 1)
print(generalInterpolation.interpolate())