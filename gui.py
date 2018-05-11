from appJar import gui

def styleButton(btn):
    app.setButtonBg(btn, "#337ab7")
    app.setButtonFg(btn, "white")
    app.setButtonCursor(btn,"hand2")
    app.setButtonRelief(btn,"groove")

def addSamplePoint():
    global samplePointsTable
    x = app.getEntry("x =")
    y = app.getEntry("y =")
    newPoint = [x,y]
    samplePointsTable.append(newPoint)
    app.addTableRow("samplePointsTable",newPoint)
    print("add sample point")

def addQuery():
    global queriesTable
    xQuery = app.getEntry("x (query) =")
    newQuery = [xQuery]
    queriesTable.append(newQuery)
    app.addTableRow("queriesTable",newQuery)
    print("add Query")

def readFile():
    print("read from file")

def interpolate():
    print("interploate")

def deleteQuery(rowNumer):
    queriesTable.remove(float(rowNumer)+1)
    app.deleteAllTableRows("queriesTable")
    app.addTableRows("queriesTable",queriesTable)

def deleteSamplePoint(rowNumer):
    app.deleteTableRow("samplePointsTable", rowNumer)

samplePointsTable = [["x", "y"]]
queriesTable = [["x"]]
# setup GUI
app = gui("Root Finder")
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
app.stopLabelFrame()

app.startLabelFrame("Queries",0,1)
app.setPadding([10,5])
app.addLabelNumericEntry("x (query) =",0,0)
app.addButton("add query",addQuery,0,1)
styleButton("add query")
app.addTable("queriesTable",
             queriesTable,1,colspan=3,action=deleteQuery,actionButton="delete query",border="sunken")
app.stopLabelFrame()

app.startLabelFrame("Interploation Method",0,2)
app.setPadding([10,5])
app.addLabelNumericEntry("Polynomial Order",colspan=2)
app.addLabelOptionBox("Method", ["Newton","Lagrange"],colspan=2)
app.addLabel("Or")
app.addFileEntry("file",4,0)
app.addButton("load",readFile,4,1)
styleButton("load")
app.addButton("Interploate",interpolate)
styleButton("Interploate")
app.stopLabelFrame()

app.startLabelFrame("Interploation Result",1,0,colspan=3)
app.addLabel("plot","Plot will be here",0,0)
app.addMessage("result", """You can put a lot of text in this widget.
The text will be wrapped over multiple lines.
It's not possible to apply different styles to different words.""",0,1)
app.addTable("queriesResultTable",
    [["x", "y"],
    [2, 45],
    [3, 37],
    [4, 28],
    [5, 51]],0,2)
app.stopLabelFrame()
app.go()
