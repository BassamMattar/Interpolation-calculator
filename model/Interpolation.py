import copy

from sympy import Symbol
from sympy import Poly
import matplotlib.pyplot as plt
import time
import math

class MyClass(object):
    y = []
    x = []
    
    xQueries = []
    yQueries = []
    
    xCurve = []
    yCurve = []
    
    
    newton_Differences = []
    
    method = 0
    exeTime = 0
    
    polynomialFunction = 0;
    
    lagranges = []
    ax = 0
    def __init__(self, newX = [], newY = [], newXQueries = [],newMethod = 0):
        self.x = newX
        self.y = newY
        self.xQueries = newXQueries
        self.method = newMethod
        if self.method == 2:
            print("Lagarange");
        else:
            self.newton_Differences = self.getNewtonDifferences(self.x, copy.deepcopy(self.y))
            
            
    
    def interpolate(self):
        self.exeTime = time.time()
        fig, self.ax = plt.subplots()
        tempSym = Symbol('x')
        tempFuncSymbol = self.getFunction(self.x,self.y);
        self.polynomialFunction = Poly(tempFuncSymbol, tempSym)
        self.polynomialFunction = Poly(self.getProberFormat(self.polynomialFunction.coeffs()),tempSym)
        self.getCurvePoints();
        self.getQueries()
        self.plot()
            
    def getInterpolationValue(self,value=0.0 , x=[0.0], y=[]):
        result = 0.0;
        if self.method == 2:
            for i in range(0, len(x), 1):
                result += self.getValueOfP(value, x, y, i)
        else:
            for i in range(0, len(self.newton_Differences), 1):
                result += self.getProperFactor(self.newton_Differences[i], i, value, x)
        return result;
       
    def getNewtonDifferences(self,x=[0.0], y=[0.0]):
        it = int((len(y) * (len(y) - 1)) / 2)
        length = len(y)
        j = 0
        i = 0;
        k = 1
        l = 0
        for _ in range (0, it, 1):
            y.append((y[j + 1] - y[j]) / (x[i + k] - x[i]))
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
    
    
    
    def getProperFactor(self,differences=0.0, noMul=0, value=0.0, x=[0.0]):
        result = differences
        for i in range(0, noMul, 1):
            result *= (value - x[i])
        return result;
    
    def getFunction(self,x=[0.0],y=[]):
        result = 0.0;
        if self.method == 2:
            for i in range(0, len(x), 1):
                result += self.getValueOfMultiplyingOuts(x,y, i)
        else:  
            for i in range(0, len(self.newton_Differences), 1):
                result += self.getProperFactorFunc(self.newton_Differences[i], i, x)
        return result;

    def getProperFactorFunc(self,differences=0.0, noMul=0, x=[0.0]):
        result = differences
        value = Symbol('x')
        for i in range(0, noMul, 1):
            result *= (value - x[i])
        return result;
    
    def getProberFormat(self, array=[]):
        formatedArray = []
        for i in array:
            prec = math.log10(math.fabs(i))
            if prec > 0:
                formatedArray.append(float(i).__format__(".2f"))
            else :
                formatedArray.append(float(i).__format__("." + str(int(math.fabs(prec)) + 1) + "f"))
        return formatedArray
        
        
    def getCurvePoints(self):
        self.xCurve = []
        self.yCurve = []
        step = .00001 * (self.x[len(self.x) - 1] - self.x[0])
        val = self.x[0] + step;
        while val <= self.x[len(self.x) - 1]:
            self.xCurve.append(val)
            self.yCurve.append(self.getInterpolationValue(val, self.x, self.y))
            val = val + step
    
    def getQueries(self):
        self.yQueries = []
        for i in self.xQueries:
            self.yQueries.append(self.getInterpolationValue(i, self.x, self.y))  
            
    def getValueOfP(self,value=0.0, x=[0.0], y=[0.0], i=0.0):
        result = y[i]
        for j in range(0, len(y), 1):
            if j is i:
                continue
            result *= (value - x[j]) / (x[i] - x[j])
        return result
    def getValueOfMultiplyingOuts(self,x=[0.0], y=[0.0], i=0.0):
        value = Symbol('x')
        result = y[i]
        for j in range(0, len(y), 1):
            if j is i:
                continue
            result *= (value - x[j]) / (x[i] - x[j])
        return result
    def getValueOfLagrange(self,x=[0.0], i=0.0):
        result = 1
        value = Symbol('x')
        for j in range(0, len(x), 1):
            if j is i:
                continue
            result *= (value - x[j]) / (x[i] - x[j])
        return result
    def getAllLagranges(self):
        sym = Symbol('x')
        self.lagranges = []
        for i in range(0,len(self.x),1):
            l = self.getValueOfLagrange(self.x, i)
            lPoly = Poly(l, sym)
            cLpoly = self.getProberFormat(lPoly.coeffs())
            self.lagranges.append("L"+str(i)+"(x)= "+str(Poly(cLpoly,sym))[5:-17])
    
    def plot(self):
        self.ax.plot(self.xCurve, self.yCurve,'gold')
        self.ax.plot(self.x, self.y, 'ro')
        print(self.xQueries)
        print(self.yQueries)
        self.ax.plot(self.xQueries, self.yQueries, 'k*')
        
        bbox_props = dict(boxstyle="round", fc="cyan", alpha=.1)    
        for i in range(0, self.xQueries.__len__(), 1):
            self.ax.text(self.xQueries[i], self.yQueries[i], "\n(" + str(self.xQueries[i]) + ", " + str(self.yQueries[i].__format__(".2f")) + ")", horizontalalignment='center', verticalalignment='top', fontsize=7, color="black", bbox=bbox_props)
      
        self.ax.text((min(self.x) + max(self.x)) / 2, min(self.yCurve), "P(x) = " + str(self.polynomialFunction)[5:-17], horizontalalignment='center', verticalalignment='top', fontsize=10, color="blue")
        
        if self.method == 2:
            self.getAllLagranges()
            #print(self.lagranges)
            plt.title('Lagrange')
            plt.figure(1).canvas.set_window_title('Interpolation fig - Lagrange')
        else:
            tempDiff = self.getProberFormat(self.newton_Differences);
           # self.ax.text((min(self.x) + max(self.x)) / 2, min(self.yCurve), "\nDivided Differences: "+ str(tempDiff), horizontalalignment='center', verticalalignment='top', fontsize=10, color="blue")
            plt.title('Newton')
            plt.figure(1).canvas.set_window_title("Interpolation fig - Newton")
            
            
        self.exeTime = time.time() - self.exeTime
        print("Execution Time: " + str(self.exeTime) + " S")
        plt.xlabel("x")
        plt.ylabel("f(x)") 
        #plt.show()
        
    def getDif(self):
        return self.newton_Differences
    
    def getLag(self):
        return self.lagranges
    def getTime(self):
        return self.exeTime
    def showplt(self):
        plt.show()