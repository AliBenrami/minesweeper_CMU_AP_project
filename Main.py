from cmu_graphics import *
from math import floor
import random
###################################################################################################
#end
#functions 
def button(value,uiposx,uiposy,uiposw,uiposh):
    button = {"rect" :centeralrect(uiposx,uiposy,uiposw,uiposh,"white"),
          "label" : Label(value,uiposx,uiposy,size = uiposw*.1)}
    return button
def centeralrect(x:int,y:int,w:int,h:int,color):
    return Rect(x-(w/2),y-(h/2),w,h,fill = color)
def grid(gridsize:int,xpos:int,ypos:int):
    picesize = (400 - (xpos + ypos))/gridsize 
    gridopject = makeList(gridsize,gridsize)
    for x in range(gridsize):
        for y in range(gridsize):  
            gridopject[x][y] = {
                "rect":(Rect(xpos+(x*picesize),ypos+(y*picesize),picesize,picesize,fill = "white",border='gray',opacity=100)),
                "pos":(x,y),
                "label": Label(" ",(xpos+(x*picesize))+(picesize/2),(ypos+(y*picesize))+(picesize/2))
                }
    return gridopject
def gridcalc(gridsize:int,xpos:int,ypos:int,boomprob:int):
    picesize = (400 - (xpos + ypos))/gridsize 
    gridopject = makeList(gridsize,gridsize)
    testvalue = 0
    for x in range(gridsize):
        for y in range(gridsize):
            
            tilevalue = 0
            if random.randint(0,boomprob) in range(floor(boomprob*.2)):
                tilevalue = "X"

            gridopject[x][y] = {
               "rect" : (Rect(xpos+(x*picesize),ypos+(y*picesize),picesize,picesize,fill = "green",border='gray')),
               "label": Label(tilevalue,(xpos+(x*picesize))+(picesize/2),ypos+(y*picesize)+(picesize/2))
            }
    for x in range(gridsize):
        for y in range(gridsize):

            
            bombnum = 0
            if gridopject[x][y]["label"].value == "X":
                for i in range(-1,2):
                    for c in range(-1,2): 
                        try:
                            
                            if x+i >= 0 and y+c >= 0:
                                if gridopject[x+i][y+c]["label"].value != "X":
                                    gridopject[x+i][y+c]["label"].value += 1 
                        except:
                            continue
    
    for x in range(gridsize):
        for y in range(gridsize):
            if gridopject[x][y]["label"].value == 0:
                gridopject[x][y]["label"].value = " "

            if gridopject[x][y]["label"].value != "X":
                app.emptycount += 1 

    




    return gridopject
def isValid(x, y, prevC, newC,gridbot):
    if x<0 or x>= app.gridsize\
       or y<0 or y>= app.gridsize or\
       gridbot[x][y]["label"].value != prevC\
       or gridbot[x][y]["label"].value == newC:
        return False
    return True
def floodfill(x, y, prevC, newC,gridbot,gridcover):
    que = []

    que.append((x,y))

    gridbot[x][y]["label"].value = newC

    while que:
        currPixel = que.pop()

        posX = currPixel[0]
        posY = currPixel[1]

        if isValid(posX + 1, posY, prevC, newC,gridbot):
            gridbot[posX + 1][posY]["label"].value = newC
            gridcover[posX + 1][posY]["rect"].opacity = 0 
            que.append([posX + 1, posY])

        if isValid(posX-1, posY, prevC, newC,gridbot):
            gridbot[posX-1][posY]["label"].value = newC
            gridcover[posX-1][posY]["rect"].opacity = 0 
            que.append([posX-1, posY])

        if isValid(posX, posY + 1, prevC, newC,gridbot):
            gridbot[posX][posY + 1]["label"].value = newC
            gridcover[posX][posY + 1]["rect"].opacity = 0 
            que.append([posX, posY + 1])

        if isValid(posX, posY-1, prevC, newC,gridbot):
            gridbot[posX][posY-1]["label"].value = newC
            gridcover[posX][posY-1]["rect"].opacity = 0 
            que.append([posX, posY-1])
        pass
    
    return 
    pass
def setgame(gridbot,gridcover,boomprob:int):
    app.emptycount = 0 

    for x in range(app.gridsize):
        for y in range(app.gridsize): 

            gridcover[x][y]["rect"].opacity = 100
            gridcover[x][y]["label"].value = " "
            gridbot[x][y]["label"].value = " "

    for x in range(app.gridsize):
        for y in range(app.gridsize):
    
            tilevalue = 0
            if random.randint(0,boomprob) in range(floor(boomprob*.2)):
                tilevalue = "X"
            gridbot[x][y]["label"].value = tilevalue

    
    for x in range(app.gridsize):
        for y in range(app.gridsize):

            
            bombnum = 0
            if gridbot[x][y]["label"].value == "X":
                for i in range(-1,2):
                    for c in range(-1,2): 
                        try:
                            
                            if x+i >= 0 and y+c >= 0:
                                if gridbot[x+i][y+c]["label"].value != "X":
                                    gridbot[x+i][y+c]["label"].value += 1 
                        except:
                            continue
    
    for x in range(app.gridsize):
        for y in range(app.gridsize):
            if gridbot[x][y]["label"].value == 0:
                gridbot[x][y]["label"].value = " "
            if gridbot[x][y]["label"].value != "X":
                app.emptycount += 1 


    app.gameover["rect"].toBack()
    app.gameover["label"].toBack()
    
    app.endbutton["rect"].toBack()
    app.endbutton["label"].toBack()
    
    app.value = "game over"   

    app.gamestate = "Start"
def endgame(gridbot,gridcover):
    app.gamestate = "End"
    app.gameover["label"].value = app.value
    
    
    app.gameover["rect"].toFront()
    app.gameover["label"].toFront()
    
    app.endbutton["rect"].toFront()
    app.endbutton["label"].toFront()
###################################################################################################
#end 
#
app.background = "black"
app.currentpress = None
app.gridsize = 9
app.gamestate = "Start"
app.endbutton = None
app.gameover = None
app.emptycount = 0 
app.value = "Gameover"
app.presscot = 0 
app.doneemptycount = 0 

app.gameover = {"rect" :centeralrect(200,100,200,200 / 2,"white"),
        "label" : Label(app.value ,200,100,size = 200*.1)}
app.endbutton = button("reset",200,250,200,100)

background = Rect(0,0,400,400,fill = app.background)
gridbot = gridcalc(app.gridsize,25,25,15)
gridcover = grid(app.gridsize,25,25)

###################################################################################################
#end
def onMousePress(mouseX, mouseY):
    # resetgame(gridbot,gridcover)
    if app.gamestate != "End":
        for gridP in gridcover:
            for griob in gridP:
                x = griob["pos"][0]
                y = griob["pos"][1]
                if griob["rect"].hits(mouseX,mouseY):
                    app.currentpress = griob["rect"]
                
    if app.gamestate == "End":
        if app.endbutton["rect"].hits(mouseX,mouseY):
            app.currentpress = app.endbutton["rect"]
        
        pass
def onMouseRelease(mouseX, mouseY):
    if app.gamestate != "End":
        for gridP in gridcover:
            for griob in gridP:
                x = griob["pos"][0]
                y = griob["pos"][1]
                if griob["rect"].hits(mouseX,mouseY):
                    if app.gamestate == "Start":
                        if app.currentpress == griob["rect"]:
                            if gridcover[x][y]["label"].value != "F":
                                griob["rect"].opacity = 0 

                                if gridbot[x][y]["label"].value == "X":
                                    app.value = "Gameover"
                                    endgame(gridbot,gridcover)
                                    pass
                                if gridbot[x][y]["label"].value == " ":
                                    floodfill(x, y, gridbot[x][y]["label"].value, "  ",gridbot,gridcover)
                    if app.gamestate == "flag" and gridcover[x][y]["rect"].opacity != 0:
                        if gridcover[x][y]["label"].value == "F":
                            gridcover[x][y]["label"].value = " " 
                        elif gridcover[x][y]["label"].value == " ":
                            gridcover[x][y]["label"].value = "F" 
                        

                    
                    pass
        for gridP in gridcover:
            for griob in gridP:     
                x = griob["pos"][0]
                y = griob["pos"][1]
                if gridbot[x][y]["label"].value == "  ":
                    for i in range(-1,2):
                        for c in range(-1,2):
                            if ((x,y) != (0,0)) and ((x+i >= 0 and app.gridsize > x+i) and (y+c >= 0 and app.gridsize > y+c)):
                                if gridbot[x+i][y+c]["label"].value != " ":
                                    gridcover[x+i][y+c]["rect"].opacity = 0  
                                    
    if app.gamestate == "End":
        if app.endbutton["rect"].hits(mouseX,mouseY):
            if app.currentpress == app.endbutton["rect"]:
                setgame(gridbot,gridcover,15)
    
    
    extradoneemptycount = 0 
    for gridP in gridcover:
        for griob in gridP:     
            x = griob["pos"][0]
            y = griob["pos"][1]
            if gridbot[x][y]["label"].value != "X":
                if gridcover[x][y]["rect"].opacity == 0: 
                    extradoneemptycount += 1 
    app.doneemptycount = extradoneemptycount
    if extradoneemptycount == app.emptycount:
        app.value = "you won"
        endgame(gridbot,gridcover)
        
        



    
    app.presscot += 1 
    








    app.currentpress = None
def onKeyPress(key):
    if key == "q":
        app.gamestate = "flag"
    if key == "w":
        app.gamestate = "Start"
###################################################################################################
cmu_graphics.run()
