from graphics import*
from Button import*

def converter(value, currency):
    x=0
    cny = {"Canadian": 1.28,
           "Euro": 0.82,
           "Japanese yen": 115.20,
           "New Taiwan dollar": 27.82,
           "South Korean won": 1198.39,
           "Pound sterling": 0.74
           }
    if currency == "Canadian":
        x = 1.00*value*cny["Canadian"]
        return round(x,2)
    if currency == "Euro":
        x= 1.00*value*cny["Euro"]
        return round(x,2)
    if currency == "Japanese yen":
        return int(1*value*cny["Japanese yen"])
    if currency == "New Taiwan dollar":
        return int(1*value*cny["New Taiwan dollar"])
    if currency == "South Korean won":
        return int(1*value*cny["South Korean won"])
    if currency == "Pound sterling":
        x= 1.00*value*cny["Pound sterling"]
        return round(x,2)
    
def main():
    
    win = GraphWin("Currency Converter", 800, 600)
    textEntry = Entry(Point(350, 350),50)
    textEntry.draw(win)
    # click the mouse to signal done entering text
    Cadm = Button(win, "white", "Canadian dollar", Point(720, 50), 75)
    Eurom = Button(win, "white", "Euro", Point(720, 150), 75)
    Japm = Button(win, "white", "Japanese yen", Point(720, 250), 75)
    NTDm = Button(win, "white", "New Taiwan dollar", Point(720, 350), 75)
    Korm = Button(win, "white", "South Korean won", Point(720, 450), 75)
    Engm = Button(win, "white", "Pound sterling", Point(720, 559), 75)
    Inp = Text(Point(350, 310), "Input a value in dollars\n wait for a few seconds and click the currency")
    Inp.setSize(20)
    Inp.draw(win)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)


    win.getMouse()
    value = float(textEntry.getText())
    var=value

    '''text = textEntry.getText()
    testText = Text(Point(150,15), text)
    testText.draw(win)'''
    
    '''testText = Text(Point(150,15), text)
    testText.draw(win)

    win.getMouse()
    win.close()'''

    m = win.getMouse()
    cur=""
    curOutpt = Text(Point(320,400),'')
    curOutpt.setSize(24)
    curOutpt.draw(win)
    while True:
        if close.isClicked(m):
            break
        if Cadm.isClicked(m):
            curOutpt.undraw()
            cur = "Canadian"
            output= str(converter(var, cur))
        if Eurom.isClicked(m):
            curOutpt.undraw()
            cur = "Euro"
            output= str(converter(var, cur))
        if Japm.isClicked(m):
            curOutpt.undraw()
            cur = "Japanese yen"
            output= str(converter(var, cur))
        if NTDm.isClicked(m):
            curOutpt.undraw()
            cur = "New Taiwan dollar"
            output= str(converter(var, cur))
        if Korm.isClicked(m):
            curOutpt.undraw()
            cur = "South Korean won"
            output= str(converter(var, cur))
        if Engm.isClicked(m):
            curOutpt.undraw()
            cur = "Pound sterling"
            output= str(converter(var, cur))
        
        curOutpt = Text(Point(320,400),output)
        Out = Text(Point(310, 375), "The value after converting is: ")
        Out.setSize(24)
        Out.draw(win)
        curOutpt.setSize(24)
        curOutpt.draw(win)
        value = float(textEntry.getText())
        var=value

        m = win.getMouse()
            
    



    win.close()


if __name__ == "__main__":
    main()
