from graphics import*
from Button import*
from math import*

def calcy(f, num):
    total = 0

    if "+" in f:
        listNum = f.split("+")
        for i in listNum:
            total= total + calcy(i,num)
        return total

    elif "-" in f:
        listNum= f.split("-")
        total= calcy(listNum[0],num) - calcy(listNum[1],num)
        return total
    
    elif "*" in f:
        listNum= f.split("*")
        total= calcy(listNum[0],num) * calcy(listNum[1],num)
        return total

    elif "/" in f:
        listNum= f.split("/")
        if calcy(listNum[1],num) == 0:
            return 0
        total= calcy(listNum[0],num) / calcy(listNum[1],num)
        return total
    
    elif "sqrt(x)" in f and num >=0:
        return sqrt(num)
    elif "sqrt(x)" in f and num <0:
        return 1000
    elif "x^2" in f:
        return num**2
    elif "sin(x)" in f:
        return sin(num)
    elif "e^x" in f:
        return e**num
    elif "cos(x)" in f:
        return cos(num)
    elif "ln(x)" in f and num>0:
        return log(num)
    elif "ln(x)" in f and num<=0:
        return 1000
    elif "x" in f:
        return num
    else:
        return float(f)

def main():

    win = GraphWin("calc",800,800)
    title = Text(Point(400,50), "Welcome to the Graphing Calculator")
    title.setSize(32)
    title2 = Text(Point(400,110), "Enter a function you would like to graph")
    title2.setSize(20)
    title3 = Text(Point(400,80), "Need '0-'if you want to start with negative sign. (ex): -x => 0-x ")
    title3.setSize(15)
    title.draw(win)
    title2.draw(win)
    title3.draw(win)

    for i in range(1,6):
        XPnum = Text(Point(400+i*50,410),i)
        XNnum = Text(Point(400-i*50,410),"-"+str(i))
        YPnum = Text(Point(390,400-i*50),i)
        YNnum = Text(Point(390,400+i*50),"-"+str(i))
        XPnum.draw(win)
        XNnum.draw(win)
        YPnum.draw(win)
        YNnum.draw(win)
    Zero=Text(Point(410,410),"0")
    Zero.draw(win)

    yAxis = Line(Point(400,130), Point(400,670))
    yAxis.draw(win)
    xAxis = Line(Point(130,400), Point(670,400))
    xAxis.draw(win)

    funText = Text(Point(200,700), "Y  =  ")
    funText.setSize(24)
    funText.draw(win)

    fun = Entry(Point(340,700),30)
    fun.draw(win)

    graph = Button(win, 'white', "GRAPH", Point(550,700), 75)
    quitB = Button(win, 'red', "QUIT", Point(400,760), 50)

    while True:
        m1 = win.getMouse()
        if graph.isClicked(m1):
            f = fun.getText()
            scale = 50
            points = []
            
            listP=f.split("+")
            
            for i in range(-1000,1000):
                a=0
                n=i-170
                x=i+230
                y= 400-scale*calcy(f,n/scale)
                    
                if ((y>=130)and(y<=670))and((x>=130)and(x<=670)):
                    points.append(Point(x,y))
                    
            '''for i in range(1000):
                n=i-250
                x = i + 50
                y = 500 - scale*calcy(f,n/scale)
                if ((y>=200)or(y<=650))and((x>=50)or(x<=750)):
                    points.append(Point(x,y))'''

            for p in points:
                p.draw(win)

        if quitB.isClicked(m1):
            win.close()
            break



if __name__ == "__main__":
    main()
