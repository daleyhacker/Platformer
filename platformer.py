"""
platformer.py
Author: Patrick Daley
Credit: Tristan, Mr. Dennison, Class Resources
Assignment:
Write and submit a program that implements the sandbox platformer game:
https://github.com/HHS-IntroProgramming/Platformer
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

blue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, blue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)

myapp = App()

#-------------------------------------------------------------------------------
#Grid
"""
grid = RectangleAsset(50, 50, noline, white)

for x in range(0, 21):
    for y in range(0, 11):
        Sprite(grid, (50*x, 50*y))
"""
#-------------------------------------------------------------------------------
#Walls
rectangleblk = RectangleAsset(50,50, blkline, black)
rectanglewhite = RectangleAsset(50,50, blkline, white)
rectangleborder = RectangleAsset(1,40, blkline, black)
rectangleUp = RectangleAsset(50,1, blkline, black)

class Wall(Sprite):
    
    def __init__(self, x, y):
        x = floor(x/50)*50 #floor rounds down to the nearest whole number
        y = floor(y/50)*50
        super().__init__(rectangleblk, (x, y))



#When mouse clicks, it will place a black rectangle on the screen where clicked.
def mouseClick(event):
    Wall(event.x, event.y)

#Listening for a Click
myapp.listenMouseEvent('click',mouseClick)

class BorderRight(Sprite):
    
    def __init__(self, x1, y1):
        x1 = floor(x1/50)*50
        y1 = floor(y1/50)*50+10
        super().__init__(rectangleborder,(x1, y1))

def mouseClick(event):
    BorderRight(event.x, event.y)

#Listening for a Click
myapp.listenMouseEvent('click',mouseClick)
    
class BorderLeft(Sprite):
    def __init__(self, x2, y2):
        x2 = floor(x2/50)*50+49
        y2 = floor(y2/50)*50+10
        super().__init__(rectangleborder,(x2, y2))

def mouseClick(event):
    BorderLeft(event.x, event.y)

#Listening for a Click
myapp.listenMouseEvent('click',mouseClick)

class BorderUp(Sprite):
    def __init__(self, x3, y3):
        x3 = floor(x3/50)*50
        y3 = floor(y3/50)*50+50
        super().__init__(rectangleUp,(x3, y3))

def mouseClick(event):
    BorderUp(event.x, event.y)

#Listening for a Click
myapp.listenMouseEvent('click',mouseClick)
    
#-------------------------------------------------------------------------------
#Player

player = RectangleAsset(15,30, blkline, red)
playersprite = None

class Player(Sprite):
    
    
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(player, (x, y))
    
#----------------------
#Prints the player where the mouse is
mouse = None

def spacekey(event):
    global mouse
    global playersprite
    if playersprite:
        playersprite.destroy()
    playersprite = Player(mouse[0], mouse[1])
    
def mousemove(event):
    global mouse
    mouse = (event.x, event.y)

myapp.listenKeyEvent('keydown', 'space', spacekey)
myapp.listenMouseEvent('mousemove', mousemove)
#--------------------------------
#Spring
spring = RectangleAsset(15,5, blkline, blue)
springsprite = None
class Spring(Sprite):
    def __init__(self, x, y):
        self.vy = 0
        super().__init__(spring, (x, y))

def Skey(event):
    global mouse
    global springsprite
    if springsprite:
        springsprite.destroy()
    springsprite = Spring(mouse[0], mouse[1])
    
myapp.listenKeyEvent('keydown', 's', Skey)

SpringJump = playersprite.collidingWithSprites(Spring)
if SpringJump:
    playersprite.y-=10
    playersprite.vy +=.08

#-------------------------------------------------------------------------------

#Makes the player move to the left
def Akey(event):
    global playersprite
    if playersprite:
        playersprite.x -= 10
    wallcollisionsLeft = playersprite.collidingWithSprites(BorderLeft)
    while wallcollisionsLeft:
        playersprite.x +=1
        wallcollisionsLeft = playersprite.collidingWithSprites(BorderLeft)

myapp.listenKeyEvent('keydown', 'a', Akey)

#----------------------
#Makes the player move to the right

def Dkey(event):
    global playersprite
    if playersprite:
        playersprite.x += 10
    wallcollisionsRight = playersprite.collidingWithSprites(BorderRight)
    while wallcollisionsRight:
        playersprite.x -=1
        wallcollisionsRight = playersprite.collidingWithSprites(BorderRight)

myapp.listenKeyEvent('keydown', 'd', Dkey)

#------------------------
#Makes the player move up
def Wkey(event):
    global playersprite
    global wkeyPress
    wkeyPress = True
    if playersprite:
        wallcollisions = playersprite.collidingWithSprites(Wall)
        if wallcollisions:
            playersprite.y -=10
            playersprite.vy = -5
        wallcollisionsUp = playersprite.collidingWithSprites(Wall)
        while wallcollisionsUp:
            playersprite.y +=1
            wallcollisionsUp = playersprite.collidingWithSprites(Wall)

def WkeyUp(event):
    global playersprite
    global wkeyPress
    wkeyPress = False
    if playersprite:
        playersprite.y +=0

WkeyPress = False
myapp.listenKeyEvent('keydown', 'w', Wkey)
myapp.listenKeyEvent('keyup', 'w', WkeyUp)

#-------------------------------------------------------------------------------
#Gravity
def step():
    global playersprite
    if playersprite:
        wallcollisions = playersprite.collidingWithSprites(Wall)
        if wallcollisions:
            playersprite.y +=0
            if WkeyPress:
                playersprite.vy +=.1
                playersprite.y+=playersprite.vy
                wallcollisionsUp = playersprite.collidingWithSprites(Wall)
                if wallcollisionsUp:
                    playersprite.y +=1
                    playersprite.vy = .1
                    while wallcollisionsUp:
                        playersprite.y += 1
                        wallcollisionsUp = playersprite.collidingWithSprites(Wall)
                
        else:
            playersprite.vy +=0.1 
            playersprite.y+=playersprite.vy
    
    if springsprite:
        global springsprite
        if springsprite:
            wallcollisions = springsprite.collidingWithSprites(Wall)
            if wallcollisions:
                springsprite.y +=0
            else:
                springsprite.vy +=.1
                springsprite.y +=springsprite.vy
#-------------------------------------------------------------------------------
#Destroy Sprite

def QKey(event):
    global playersprite
    if playersprite:
        playersprite.visible = False
        playersprite.destroy()
        playersprite = None

myapp.listenKeyEvent('keydown', 'q', QKey)
#-------------------------------------------------------------------------------

myapp.run(step)



"""
#When mouse clicks, it will place a black rectangle on the screen where clicked.
def mouseClick(event):
    rectangleblk.x = event.x
    rectangleblk.y = event.y
    x = floor(event.x/50)*50 #floor rounds down to the nearest whole number
    y = floor(event.y/50)*50
    Wall(event.x, event.y)

#Not needed because Gravity will do this
#Makes the player move down
"""