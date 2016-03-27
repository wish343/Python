__author__ = 'Shobhit Garg'
__author__ = 'Vishal Garg'

import random
import turtle
import math
# global constants for window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

def draw_space():
    """
    Draw space between two elements to be drawn
    : pre: (relative) pos (0,0), heading (east), up
    : post: (relative) pos (100,0), heading (east), up
    : return: None
    """
    turtle.up()
    turtle.setheading(0)
    turtle.forward(100)

    
def init():
    """
    Initialize for drawing in the night. (-WINDOW_WIDTH/2, -WINDOW_HEIGHT/2) is in
    the lower left and(WINDOW_WIDTH/2, WINDOW_HEIGHT/2) is in the
    upper right.
    : pre: (relative) pos (0,0), heading (east), down
    : post:(relative) pos (-333.33,0), heading (east), up
    : return: None
    """

    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_HEIGHT / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.hideturtle()
    turtle.setx(-WINDOW_WIDTH / 3)
    #turtle.setheading(0)
    turtle.showturtle()
    
def init_for_day():
    """
    Initialize for drawing in the day. (-WINDOW_WIDTH/2, -WINDOW_HEIGHT/2) is in
    the lower left and(WINDOW_WIDTH/2, WINDOW_HEIGHT/2) is in the
    upper right.
    : pre: (relative) pos (0,0), heading (east), up
    : post:(relative) pos (-500,-333.33), heading (east), up
     heading (east), up
    : return: None
    """
    turtle.up()
    turtle.hideturtle()
    turtle.setx(-WINDOW_WIDTH/2)
    turtle.sety(-WINDOW_HEIGHT/3)
    turtle.setheading(0)
    turtle.showturtle()

    
def draw_tree(tree_type):
    """
    Draw the trees. Takes tree type as a parameter and draws that tree type.
    : pre: (relative) pos (0,0), heading (east), up
    : post:(relative) pos (0,0), heading (east), up
    : return: wood used for making the tree, height of the tree.
    """

    if tree_type == "pine":
        tree_height = random.randint(50, 200)
    elif tree_type == "maple":
        tree_height = random.randint(50, 150)
    else:
        tree_height = random.randint(50, 200)
    # drawing the trunk
    turtle.down()
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(tree_height)

    if tree_type == "pine":

        turtle.left(90)
        turtle.up()
        turtle.back(tree_height / 4)
        turtle.down()
        for _ in range(0,3):
            turtle.forward(tree_height/2)
            turtle.right(120)    
        turtle.forward(tree_height / 4)
        turtle.up()
        turtle.left(90)
        turtle.forward(tree_height)
        turtle.left(90)
        total_height = abs(math.cos(60)) * tree_height/2 + tree_height

    elif tree_type == "maple":
        turtle.right(90)
        turtle.circle(tree_height / 3)
        turtle.up()
        turtle.right(90)
        turtle.forward(tree_height)
        turtle.setheading(0)
        total_height = tree_height * 2 / 3 + tree_height
    else:
        turtle.up()
        turtle.left(90)
        turtle.forward(tree_height / 4)
        turtle.right(120)
        turtle.down()
        for _ in range(2):
            turtle.forward(tree_height / 2)
            turtle.right(120)
        turtle.up()
        turtle.forward(tree_height / 4)
        turtle.left(90)
        turtle.forward(tree_height)
        turtle.left(90)
        total_height = abs(math.cos(60)) * tree_height/2 + tree_height

    turtle.up()    
    #turtle.forward(100)
    return tree_height, total_height

    

def draw_house(size):
    """
    Draw the House.
    : pre: (relative) pos (0,0), heading (east), up
    : post:(relative) pos (0,size) where size is the parameter passed, heading (east), up
    : return: wood used for making the tree, height of the tree.
    """
    turtle.down()
    turtle.setheading(0)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(45)
    incline = size / math.sqrt(2)
    turtle.forward(incline)
    turtle.left(90)
    turtle.forward(incline)
    turtle.left(45)
    turtle.forward(size)
    turtle.up()
    turtle.left(90)
    turtle.forward(size)
    #turtle.forward(100)
    total_lumber = 2 * size + 2 * incline
    height = size + incline
    return total_lumber, height

   

def draw_star(height):
    """
    Draw the Star.
    : pre: (relative) pos (0,0), heading (east), up
    : post:(relative) pos (-100,0), heading (east), up
    : return: none.
    """
    #turtle.up()
    turtle.back(100)
    turtle.left(90)
    turtle.forward(height + 10)
    turtle.forward(15)
    for _ in range(12):
        turtle.down()
        turtle.left(30)
        turtle.forward(15)
        turtle.up()
        turtle.back(15)
    turtle.back(15 + height + 10)
    turtle.setheading(0)

def draw_sun():
    """
    Draw the Sun.
    : pre: (relative) pos (0,0), heading (east), up
    : post:(relative) pos (0,693), heading (east), up
     heading east, up
    : return: none.
    """
    turtle.up()
    turtle.left(90)
    turtle.forward(333 + 360)
    turtle.right(90)
    turtle.down()
    turtle.circle(50)


def draw_night():
    """
    Draw the night.
    : pre:  pos (-333.33,0), heading (east), up
    : post: pos(-333.33 + (no of trees-1)*100 + 200(if house is there),0 ) bottom of the star, up
    : return: total lumber from trees and house
    """
    
    init()
    max_height = 0
    total_lumber = 0
    current_height = 0
    no_of_trees = int(input("Specify the no of trees: "))
    house = input("Do you want a house as well (y/n): ")

    if no_of_trees > 0 and house == 'y' or house == 'Y':
        if no_of_trees > 1:
            house_no = random.randint(1, no_of_trees - 1)
        else:
            house_no = 1
            
        
        for count in range(0, no_of_trees + 1):
            if count == house_no:
                lumbar, current_height = draw_house(100)
                if current_height > max_height:
                    max_height = current_height
                total_lumber += lumbar

            else:
                trees = ["pine", "maple", "random"]
                tree_type = random.choice(trees)
                tree_height, current_height = draw_tree(tree_type)
                if current_height > max_height:
                    max_height = current_height
                total_lumber += tree_height
            draw_space()
    else:
        for _ in range(0, no_of_trees):
            trees = ["pine", "maple", "random"]
            tree_type = random.choice(trees)
            tree_height, current_height = draw_tree(tree_type)
            if current_height > max_height:
                max_height = current_height
            total_lumber += tree_height
            draw_space()
            
    draw_star(max_height)
    return total_lumber

def draw_day(total_lumber):
    """
    Draw the day.
    : pre:  pos(-333.33 + (no of trees-1)*100 + 200(if house is there),0 ) bottom of the star, up
    : post: pos(-400 ,360 )
    : return: none.
    """
    day = input("Night is done , press enter for day ")
    print("We have ",total_lumber," units of lumber for building")
    turtle.reset()
    house_size = total_lumber/ (2 + math.sqrt(2))
    print("We will build a house with walls ",house_size, " tall")
    init_for_day()
    total_lumber, current_height = draw_house(house_size)
    draw_space()
    draw_sun()
    x=input("Day is done, house is done, press Enter to quit")
    turtle.bye()

if __name__=="__main__":
    total_lumber=draw_night()
    draw_day(total_lumber)
