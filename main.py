import ast
import turtle

varInput = ''
verify = False
database = {}

def getAllRecords():
    global database
    with open('database.txt') as data:
        f = data.read()
        database = ast.literal_eval(f)

def getInput():
    global varInput
    varInput = input() # input

def verifyShape(shape):
    global verify
    if shape in database.keys():
        print('Shape found')
        verify = True
        return verify
    else:
        print('Not found')
        verify = False
        return verify

def printShape(isTrue):
    global varInput
    if isTrue:
        if varInput == 'Triangle':
            drawTriangle()
        elif varInput == 'Square':
            drawSquare()
        elif varInput == 'Hexagon':
            drawHexagon()
        else:
            print('Finish')
    else:
        print('Shape not found')

def drawHexagon():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(20)
        turtle.right(720/laturi)
    turtle.Screen().exitonclick()

def drawTriangle():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(20)
        turtle.right(180/laturi)
    turtle.Screen().exitonclick()

def drawSquare():
    laturi = database.get(varInput)
    for i in range(laturi):
        turtle.forward(20)
        turtle.right(360 / laturi)
    turtle.Screen().exitonclick()


if __name__ == '__main__':
    getAllRecords()
    getInput()
    verifyShape(varInput)
    printShape(verify)
