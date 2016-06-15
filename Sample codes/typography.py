"""
    typography.py
    Author: Vishal Garg(vg3660@cs.rit.edu)
    This program prints name Vishal Garg using function hierarchy and promotes code reusability.
"""
import turtle
import math

t = turtle.Turtle()

# Global constants for windows dimensions
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

""" initializeSpace function moves the turtle to left-top corner of the screen so that we can write long names without going out of window
    : pre: pos(0,0), heading (east), right
    : post: pos(-200, 200), heading (east), right
    : return: None
"""
def initializeSpace():
    turtle.setworldcoordinates(-WINDOW_WIDTH/2,-WINDOW_HEIGHT/2,WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
    t.up()
    t.setpos(-200,200)
    t.down()
    return

""" changeSpace function moves the turtle to the second line so that you can write code clearly
    : pre: (relative) pos(0,0), heading (east), right          (pre positition turtle may point anywhere, east right in our case)
    : post: pos(-200, 200-(size*1.5)), heading (east), right   (post position will change according to the size of characters we draw)
    : return: None
"""
def changeSpace(size):
    t.up()
    t.setpos(-200,200-(size*1.5))
    t.down()
    return

""" giveSpace function provides space between two characters according to the size of the characters
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(size/3.3, 0), heading (east), right      (it may move in the y-coordinate also depending on the direction of turtle)
    : return: None
"""
def giveSpace(size):
    t.up()
    t.forward(size/3.3)
    t.down()
    return

""" moveUp function moves the turtle down to top(according to the size of characters) in case some characters are created top to down
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(0, size), heading (east), right
    : return: None
"""
def moveUp(size):
    t.up()
    t.left(90)
    t.forward(size)
    t.right(90)
    t.down()
    return

""" moveDown function moves the turtle top to down(according to the size of characters) in case some character is created down to top
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(0, -size), heading (east), right
    : return: None
"""
def moveDown(size):
    t.up()
    t.right(90)
    t.forward(size)
    t.left(90)
    t.down()
    return

""" drawV function creates the character V according to the size variable passed to it
    It uses maths.cos function to find the length of the slant line, but as it can be negative we used maths.fabs to convert it to a positive value
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(size2, 0), heading (east), right
    : return: None
"""
def drawV(size):
    size2=size/(math.fabs(math.cos(60)))
    t.right(60)
    t.forward(size2)
    t.left(120)
    t.forward(size2)
    t.right(60)
    return

""" drawI function creates the character I according to the size variable passed to it
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(size/3, -size), heading (east), right
    : return: None
"""
def drawI(size):
    t.forward(size/3)
    t.back(size/6)
    t.right(90)
    t.forward(size)
    t.left(90)
    t.back(size/6)
    t.forward(size/3)

""" drawS function creates the character S according to the size variable passed to it
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(size/2, size), heading (east), right
    : return: None
"""
def drawS(size):
    t.forward(size/2)
    t.left(90)
    t.forward(size/2)
    t.left(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/2)
    return

""" drawH function creates the character H according to the size variable passed to it
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(size/2, -size), heading (east), right
    : return: None
"""
def drawH(size):
    t.right(90)
    t.forward(size)
    t.back(size/2)
    t.left(90)
    t.forward(size/2)
    t.left(90)
    t.forward(size/2)
    t.back(size)
    t.right(90)
    return

""" drawA function creates the character A according to the size variable passed to it

    It uses maths.cos function to find the length of the slant line, but as it can be negative we used maths.fabs to convert it to a positive value
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(size2, 0), heading (east), right
    : return: None
"""
def drawA(size):
    size1=math.fabs(math.cos(60))
    size2=size/size1
    size3=0.6*size
    t.left(60)
    t.forward(size2)
    t.right(120)
    t.forward(size3)
    t.left(60)
    t.back(size3)
    t.forward(size3)
    t.right(60)
    t.forward(size2-size3)
    t.left(60)
    return

""" drawL function creates the character L according to the size variable passed to it
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(size/2, -size), heading (east), right
    : return: None
"""
def drawL(size):
    t.right(90)
    t.forward(size)
    t.left(90)
    t.forward(size/2)
    return

""" drawG function creates the character G according to the size variable passed to it
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(size/2, -size), heading (east), right
    : return: None
"""
def drawG(size):
    t.forward(size/2)
    t.back(size/2)
    t.right(90)
    t.forward(size)
    t.left(90)
    t.forward(size/2)
    t.left(90)
    t.forward(0.4*size)
    t.left(90)
    t.forward(0.3*size)
    t.left(90)
    t.forward(0.15*size)
    t.up()
    t.forward(0.25*size)
    t.left(90)
    t.forward(0.3*size)
    t.down()
    return

""" drawR function creates the character R according to the size variable passed to it

    It uses math.sqrt() function to calculate the length of the slanting line in R
    : pre: (relative) pos(0,0), heading (east), right
    : post: (relative) pos(size/2, 0), heading (east), right
    : return: None
"""
def drawR(size):
    t.left(90)
    t.forward(size)
    t.right(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/2)
    t.left(135)
    t.forward(math.sqrt(2)*(size/2))
    t.left(45)
    return

""" This function is used to print a name like my name VISHAL GARG
    It can be edited to print other things as well
    : pre: pos(0,0), heading (east), right
    : post: pos(-200+(1.5*size + 3*size/3.3 + size/math.fabs(math.cos(60))), 200-size*2.5), heading (east), right   (((approx.(-200+(3.65*size) , 200-(2.5*size))   )))
    : return: None
"""
def main():
    size=100
    initializeSpace()
    drawV(size)
    giveSpace(size)
    drawI(size)
    giveSpace(size)
    drawS(size)
    giveSpace(size)
    drawH(size)
    giveSpace(size)
    drawA(size)
    giveSpace(size)
    moveUp(size)
    drawL(size)
    changeSpace(size)
    drawG(size)
    giveSpace(size)
    drawA(size)
    giveSpace(size)
    drawR(size)
    giveSpace(size)
    moveUp(size)
    drawG(size)
    t.hideturtle()
    input("Press ENTER/RETURN")
    turtle.bye()
    return

if __name__=='__main__':
    main()
