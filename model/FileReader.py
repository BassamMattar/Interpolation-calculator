class MyClass(object):
    file = 0
    method = 0
    nPoints = 0
    x = []
    y = []
    xQueries = []
    def __init__(self, path = ""):
        self.file = open(path, "r")
        
    def getResult(self):
        self.x = []
        self.y = []
        self.xQueries = []

        lines = self.file.readlines()

        self.method = int(lines[0])
        self.nPoints = int(lines[1])
        
        Points = lines[2]
        
        Points = Points.replace("[","")
        Points = Points.replace("]","")
        
        array = Points.split(",")
        
        for i in array:
            self.x.append(float(i))
            
        Points = lines[3]
        Points = Points.replace("[","")
        Points = Points.replace("]","")
        array = Points.split(",")
        
        for i in array:
            self.y.append(float(i))    
               
        Points = lines[4]
        Points = Points.replace("[","")
        Points = Points.replace("]","")
        array = Points.split(",")
        
        for i in array:
            self.xQueries.append(float(i))
        return self.method,self.nPoints,self.x,self.y,self.xQueries
