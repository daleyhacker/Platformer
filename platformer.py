"""
platformer.py
Author: Patrick Daley
Credit: Tristan, 
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
    
#-------------------------------------------------------------------------------
#Player

player = RectangleAsset(15,30, blkline, red)
playersprite = None

class Player(Sprite):
    
    
    def __init__(self, x, y):
        super().__init__(player, (x, y))
    
#----------------------
#Prints the player where the mouse is
mouse = None

def spacekey(event):
    global mouse
    global playersprite
    playersprite = Player(mouse[0], mouse[1])
    
def mousemove(event):
    global mouse
    mouse = (event.x, event.y)

myapp.listenKeyEvent('keydown', 'space', spacekey)
myapp.listenMouseEvent('mousemove', mousemove)
#--------------------------------
#Makes the player move to the left
def Akey(event):
    global playersprite
    if playersprite:
        playersprite.x -= 10
    wallcollisions = playersprite.collidingWithSprites(Wall)
    while wallcollisions:
        playersprite.x +=1
        wallcollisions = playersprite.collidingWithSprites(Wall)

myapp.listenKeyEvent('keydown', 'a', Akey)

#----------------------
#Makes the player move to the right
def Dkey(event):
    global playersprite
    if playersprite:
        playersprite.x += 10
    wallcollisions = playersprite.collidingWithSprites(Wall)
    while wallcollisions:
        playersprite.x -=1
        wallcollisions = playersprite.collidingWithSprites(Wall)

myapp.listenKeyEvent('keydown', 'd', Dkey)

#------------------------
#Makes the player move up
def Wkey(event):
    global playersprite
    if playersprite:
        playersprite.y -= 30
    wallcollisions = playersprite.collidingWithSprites(Wall)
    while wallcollisions:
        playersprite.y +=1
        wallcollisions = playersprite.collidingWithSprites(Wall)
    while wallcollisions:
        playersprite.y +=0
        else:
            playersprite.y +=10


myapp.listenKeyEvent('keydown', 'w', Wkey)

#Not needed because Gravity will do this
#Makes the player move down
"""
def Skey(event):
    global playersprite
    if playersprite:
        playersprite.y += 30
myapp.listenKeyEvent('keydown', 's', Skey)
"""

#-------------------------------------------------------------------------------
#Gravity
"""wallcollisions = Player.collidingWithSprites(Wall)
if wallcollisions:
    Player.y = y
else:
    Player.y +=10
"""




myapp.run()



"""
#When mouse clicks, it will place a black rectangle on the screen where clicked.
def mouseClick(event):
    rectangleblk.x = event.x
    rectangleblk.y = event.y
    x = floor(event.x/50)*50 #floor rounds down to the nearest whole number
    y = floor(event.y/50)*50
    Wall(event.x, event.y)
"""