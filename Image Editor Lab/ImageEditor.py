from graphics import*
from Button import*

def brighten(cats):
    for i in range(cats.getWidth()):
        for j in range(cats.getHeight()):
            color=cats.getPixel(i,j)
            r,g,b=color[0]+25, color[1]+25, color[2]+25
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            cats.setPixel(i,j,color_rgb(r,g,b))
def darken(cats):
    for i in range(cats.getWidth()):
        for j in range(cats.getHeight()):
            color=cats.getPixel(i,j)
            r,g,b=color[0]-25, color[1]-25, color[2]-25
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            cats.setPixel(i,j,color_rgb(r,g,b))

def blurr(cats):
    for i in range(1,cats.getWidth()-1):
        for j in range(1,cats.getHeight()-1):
            r=int((cats.getPixel(i,j)[0]+cats.getPixel(i+1,j)[0]+cats.getPixel(i-1,j)[0]+cats.getPixel(i,j+1)[0]+cats.getPixel(i,j-1)[0])/5)
            g=int((cats.getPixel(i,j)[1]+cats.getPixel(i+1,j)[1]+cats.getPixel(i-1,j)[1]+cats.getPixel(i,j+1)[1]+cats.getPixel(i,j-1)[1])/5)
            b=int((cats.getPixel(i,j)[2]+cats.getPixel(i+1,j)[2]+cats.getPixel(i-1,j)[2]+cats.getPixel(i,j+1)[2]+cats.getPixel(i,j-1)[2])/5)

            cats.setPixel(i,j,color_rgb(r,g,b))
            
def contrast(cats):
    for i in range(cats.getWidth()):
        for j in range(cats.getHeight()):
            color=cats.getPixel(i,j)
            r,g,b=color[0], color[1], color[2]
            if (r+g+b > (225*3/2)):
                r,g,b=color[0]+20, color[1]+20, color[2]+20
                if r > 255:
                    r = 255
                if g > 255:
                    g = 255
                if b > 255:
                    b = 255
            else:
                r,g,b=color[0]-20, color[1]-20, color[2]-20
                if r < 0:
                    r = 0
                if g < 0:
                    g = 0
                if b < 0:
                    b = 0
            cats.setPixel(i,j,color_rgb(r,g,b))
            
def specialFilter(cats):
    for i in range(cats.getWidth()):
        for j in range(cats.getHeight()):
            color=cats.getPixel(i,j)
            r,g,b=255-color[0], 255-color[1], 255-color[2]
            cats.setPixel(i,j,color_rgb(r,g,b))
def s(cats):
    org=cats.getPixel(cats.getWidth(),cats.getHeight()-1)
    for i in range(cats.getHeight()):
        cats.getPixel(cats.getWidth(),cats.getHeight()-i-1)=cats.getPixel(cats.getWidth(),cats.getHeight()-i)
        
    
def main():

    win = GraphWin("Image Editor", 800, 600)
    sh = Button(win, "white", "Show", Point(100, 40), 45)
    hi = Button(win, "white", "Hide", Point(200, 40), 45)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    bright = Button(win, "white", "Brighten", Point(720, 50), 45)
    dark = Button(win, "white", "Darken", Point(720, 150), 45)
    blur = Button(win, "white", "Blur", Point(720, 250), 45)
    cont = Button(win, "white", "Contrast", Point(720, 350), 45)
    filt = Button(win, "white", "Filter", Point(720, 450), 45)
    rest = Button(win, "white", "Reset", Point(300, 40), 45)

    cats = Image(Point(400,300), "Cats.png")
    org = cats.clone()

    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if sh.isClicked(m):
            cats.undraw()
            cats.draw(win)
        if hi.isClicked(m):
            cats.undraw()
        if dark.isClicked(m):
            darken(cats)
        if bright.isClicked(m):
            brighten(cats)
        if blur.isClicked(m):
            blurr(cats)
        if cont.isClicked(m):
            contrast(cats)
        if filt.isClicked(m):
            specialFilter(cats)
        if rest.isClicked(m):
            cats=org.clone()
            cats.undraw()
            cats.draw(win)
            
        m = win.getMouse()

    win.close()
    
if __name__ == "__main__":
    main()
