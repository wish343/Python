"""
    typography.py
    Author: vishalgarg(vg3660@cs.rit.edu)
    Author: shobhitgarg(sg3639@cs.rit.edu)
    This program prints a Tree on the screen
"""
import turtle
import random
import math

MAX = 0
"""
	This function prints the tree according to the Depth(n) Bushiness(b) Leafiness(l) and Height(size)
	: pre : On the bottom of the tree, heading (north) Down
	: post : On the bottom of the tree, heading (north) Down
"""
def draw_tree(n, b, l, size):
	if n < 0:						#base-case
		return
	elif n == 0:					#Draw Leaves
		turtle.color("green")							#Color of leaves
		turtle.width(1)
		numberOfLeaves = random.randint(5, 15)			#Random number of leaves ranging from 5 to 15
		angle = int(270 / numberOfLeaves)				#Angle Range between leaves determined by number of leaves
		for i in range(numberOfLeaves):
			if (randomB(l)):
				angle2 = random.randint(0 + (i * angle), 0 + ((i + 1) * angle))	#Angle between different leaves can be different given the Angle Range
				angle2-=135
				turtle.right(angle2)
				turtle.forward(5)
				turtle.back(5)
				turtle.left(angle2)
		return
	else:							#Draw Tree
		turtle.color("brown")						#Color of Tree
		turtle.forward(size)
		b1 = math.floor(5 * b)						#Using Bushiness to calculate number of branches: Max branchess are 5
		angle = int(270 / b1);						#Angle Range between branches determined by Number of Branches
		for i in range(b1):
			if randomB(b1):
				angle2 = random.randint(0 + (i * angle), 0 + ((i + 1) * angle))	#Angle between different branches can be different given the Angle Range
				angle2-=135
				turtle.right(angle2)
				draw_tree(n - 1, b, l, size * random.uniform(0.4, 0.7))			#Recursion step: size of sub-tree is random
				turtle.left(angle2)
		turtle.color("brown")
		turtle.back(size)
	return

"""
	This function generates a number z between 0 to 1 and returns true if z less than or equal to given number
"""
def randomB(x):
	z = random.random()
	if z <= x:
		return True
	else:
		return False

"""
	This is the main function for taking inputs and calling DrawTree function
"""

def enhanced():
	depth = int(input("Please enter the recursion depth"))
	MAX = depth
	x=0
	y=1
	for i in range(depth):										#For calculating height of a sub tree according to the number of steps and Total height inputted
		x+=y
		y*=0.5
	height = int(input("Please enter the expected height of tree"))
	if height>0:
		size=height/x												#Height being passed to the DrawTree function
		print("First Size is ",size)
		bushiness = float(input("Please enter the bushiness for the tree"))
		leafiness = float(input("Please enter the leafiness for the tree"))
		turtle.speed(0)
		turtle.left(90)
		draw_tree(depth, bushiness, leafiness, size)
		turtle.done()
		return
	else:
		print("Please input correct height next time :)")
		return


if __name__ == '__main__':
	enhanced()
