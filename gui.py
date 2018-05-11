from appJar import gui
from model import Interpolation


def styleButton(btn):
    app.setButtonBg(btn, "#337ab7")
    app.setButtonFg(btn, "white")
    app.setButtonCursor(btn,"hand2")
    app.setButtonRelief(btn,"groove")



def addSamplePoint():
    global samplePointsTable
    x = app.getEntry("x =")
    y = app.getEntry("y =")
    if x == None or y == None:
        app.errorBox("Empty Sample Point", "Please enter sample point")
    else :
        duplicateX = False
        for point in samplePointsTable:
            if x == point[0]:
                duplicateX = True
                break
        if duplicateX:
            app.errorBox("Duplicate Sample Point", "you can't enter duplicate sample point")
        else:
            newPoint = [x,y]
            samplePointsTable.append(newPoint)
            app.addTableRow("samplePointsTable",newPoint)
            print("add sample point")

def addQuery():
    global queriesTable
    xQuery = app.getEntry("x (query) =")
    if(xQuery == None):
        app.errorBox("Empty Query","Please enter query point")
    else:
        newQuery = [xQuery]
        if newQuery in queriesTable:
            app.errorBox("Duplicate Query","you can't enter duplicate query")
        else:
            queriesTable.append(newQuery)
            app.addTableRow("queriesTable",newQuery)
            print("add Query")

def readFile():
    print("read from file")

def generatePlot():
    if generalInterpolation.method == 0:
        app.errorBox("Plotting without interpolation","you must ruuning interpolation fisrt")
    else:
        generalInterpolation.showplt()
        print("plot")

def fillQueriesResultTable(xQueries, yQueries):
    data = []
    for x in xQueries:
        data.append([x])
    for i in range(0,len(yQueries),1):
        data[i].append(yQueries[i])
    app.deleteAllTableRows("queriesResultTable")
    app.addTableRows("queriesResultTable",data)
    print("fill queries result table")

generalInterpolation = Interpolation.MyClass()
def interpolate():
    xQueries = []
    xPoints = []
    yPoints = []
    for samplePoint in samplePointsTable:
        xPoints.append(float(samplePoint[0]))
        yPoints.append(float(samplePoint[1]))
    for query in queriesTable:
        xQueries.append(float(query[0]))
    polyOrder = app.getEntry("Polynomial Order")
    if not xPoints or not yPoints or not xQueries:
        app.errorBox("Empty data","Please, fill the required entries first")
    elif len(xPoints) == 1:
        app.errorBox("Required sample points", "you must enter at least 2 sample points")
    elif polyOrder == None:
        app.errorBox("Empty polynomial order","Please, specifiy the polynomial order")
    elif not(polyOrder < len(xPoints)):
        app.errorBox("Invalid polynomial order", "Polynomial order must be less than number of sample points")
    else:
        method = app.getOptionBox("Method")
        methodNum = 1 if method == "Newton" else 2
        print(xPoints,yPoints,xQueries,polyOrder,method,str(methodNum))    #debugging
        global generalInterpolation
        generalInterpolation = Interpolation.MyClass(newX=xPoints, newY=yPoints, newXQueries=xQueries, newMethod=methodNum)
        generalInterpolation.interpolate()
        app.setMessage("function","P(x) = " + str(generalInterpolation.getFunc())[5:-17])
        app.setMessage("time","execution time = " + str(generalInterpolation.getTime()) + " s")
        fillQueriesResultTable(*generalInterpolation.getQueryResult())
        if method == "Newton":
            app.setMessage("details",generalInterpolation.getDif())
        elif method == "Lagrange":
            app.setMessage("details", generalInterpolation.getLag())

def deleteQuery(rowNumber):
    print(rowNumber)
    del queriesTable[rowNumber]
    app.deleteAllTableRows("queriesTable")
    app.addTableRows("queriesTable",queriesTable)

def deleteSamplePoint(rowNumber):
    print(rowNumber)
    del samplePointsTable[rowNumber]
    app.deleteAllTableRows("samplePointsTable")
    app.addTableRows("samplePointsTable",samplePointsTable)

samplePointsTable = []
queriesTable = []
# setup GUI
app = gui("Interpolation Calculator",showIcon=True)
app.setResizable(False)
#app.setIcon("logo.ico")
app.setBg("#e2edff",override=True)
app.setFont(family="inherit")
app.setSticky("nesw")
app.setStretch("")


app.startLabelFrame("Sample Points",0,0)
app.setPadding([10,5])
app.addLabelNumericEntry("x =",0,0)
app.addLabelNumericEntry("y =",0,1)
app.addButton("add point",addSamplePoint,0,2)
styleButton("add point")
app.addTable("samplePointsTable",
    [["x", "y"]],1,colspan=3,action=deleteSamplePoint,actionButton="delete",border="sunken")
app.setTableHeight("samplePointsTable", 200)
app.stopLabelFrame()

app.startLabelFrame("Queries",0,1)
app.setPadding([10,5])
app.addLabelNumericEntry("x (query) =",0,0)
app.addButton("add query",addQuery,0,1)
styleButton("add query")
app.addTable("queriesTable",
             [["x"]],1,colspan=3,action=deleteQuery,actionButton="delete query",border="sunken")
app.setTableHeight("queriesTable", 200)
app.stopLabelFrame()

app.startLabelFrame("Interploation Method",1,0)
app.setPadding([10,5])
app.addLabelNumericEntry("Polynomial Order",colspan=3)
app.addLabelOptionBox("Method", ["Newton","Lagrange"],colspan=3)
app.addLabel("Or")
app.addFileEntry("file",4,0)
app.addButton("load",readFile,4,1)
styleButton("load")
app.addButton("Interploate",interpolate,5,0)
styleButton("Interploate")
app.addButton("generate plot",generatePlot,5,1)
styleButton("generate plot")
app.stopLabelFrame()

app.startLabelFrame("Interploation Result",1,1)
app.startScrollPane("resultPane")
app.setPadding([10,5])
app.addMessage("function","P(x) = ?")
app.setMessageBg("function","light blue")
app.setMessageWidth("function",350)
app.addMessage("time","execution time = ?")
app.setMessageBg("time","light blue")
app.setMessageWidth("time",350)
app.addMessage("details", "Interpolation Method details will be here.")
app.setMessageWidth("details",350)
app.addTable("queriesResultTable",
    [["x (query)", "y"]],border="sunken")
app.setScrollPaneWidth("resultPane", 400)

app.stopScrollPane()
app.stopLabelFrame()
app.go()
