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

rectanglegrid = RectangleAsset(50, 50, noline, white)
rectangleblk = RectangleAsset(50,50, blkline, black)

#---------------------------------------------------------------------------
#Grid
for x in range(0, 21):
    for y in range(0, 11):
        Sprite(rectanglegrid, (50*x, 50*y))


class Wall(Sprite):
    pass




#---------------------------------------------------------------------------
#Player
player = RectangleAsset(15,30, blkline, red)
player1 = Sprite(player,(20,20))


#When mouse clicks, it will place a black rectangle on the screen where clicked.
def mouseClick(event):
    rectangleblk.x = event.x
    rectangleblk.y = event.y
    x = floor(event.x/50)*50 #floor rounds down to the nearest whole number
    y = floor(event.y/50)*50
    Wall(rectangleblk,(x,y))


#Listening for a Click
myapp.listenMouseEvent('click',mouseClick)

#---------------------------------------------------------------------------
#
def keypress(event):
    player

#super().__init__(rectangle1, (0,0))
myapp.run()


