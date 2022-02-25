from graphics1 import *

class Cat():

    def __init__(self, win, x, y):

        self.x = x
        self.y = y
        self.pos = (x, y)
        self.start = Point(110 + x*15, 110 + y*15)
        self.image = Image(self.start, "Cat.png")
        self.image.draw(win)

    def changePos(self, x, y):
        self.pos = (x, y)
    
    def redraw(self, cX, cY):
        self.image.move(cX*15, cY*15)
        
    #Rules for cat movement:
    #Can move diagonally and up to 2 squares
        
    def move(self, food, tlt, mir):
        
        x = self.pos[0]
        y = self.pos[1]

        foodX = foodpos[0]
        foodY = foodpos[1]
        tltX = tltpos[0]
        tltY = tltpos[1]
        mirX = mirpos[0]
        mirY = mirpos[1]
        
        ItemL = []
        ItemL.append((f1X, f1Y))
        ItemL.append((f2X, f2Y))
        ItemL.append((f3X, f3Y))

        ItemDis = []
        ItemDis.append(abs(x - f1X) + abs(y - f1Y))
        ItemDis.append(abs(x - f2X) + abs(y - f2Y))
        ItemDis.append(abs(x - f3X) + abs(y - f3Y))

        minDist = 1000
        fX = 0
        fY = 0
        for i in range(3):
            if fDistances[i] < minDist:
                minDist = fDistances[i]
                fX = fList[i][0]
                fY = fList[i][1]
        
        #create a list to hold all of the potential movements
        potentialMove = []
        potentialMove.append((x + 1, y))
        potentialMove.append((x - 1, y))
        potentialMove.append((x, y + 1))
        potentialMove.append((x, y - 1))

        #check to see if any of the movements would go "off the grid"
        for m in potentialMove:
            if m[0] > 19 or m[0] < 0 or m[1] > 19 or m[1] < 0:
                potentialMove[potentialMove.index(m)] = (x, y)

        #create a list for all calculated distances
        distances = []

        #calculate all distances between potential movements and the fish position
        for m in potentialMove:
            diff = abs(fX - m[0]) + abs(fY - m[1])
            distances.append(diff)

        #evaluate which of the distances is the shortest
        minDist = 1000
        theMove = 0
        for dis in distances:
            if dis < minDist:
                minDist = dis
                theMove = distances.index(dis)

        #determine how far to move the shark image
        changeX = potentialMove[theMove][0] - x
        changeY = potentialMove[theMove][1] - y

        #change the position of the shark and the image
        self.pos = potentialMove[theMove]
        self.redraw(changeX, changeY)

        
        
                
        
        
    










