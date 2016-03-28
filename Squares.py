__author__ = 'wIsh'

import turtle
"""
	This function takes 3 inputs and prints recursive squares according to that
	pre: (relative) left-bottom of the square, heading(east) down
	post: (relative) left-bottom of the square, heading(east) down
"""
def drawSquare(size,depth,number):
	walk=0
	#Base condition
	if depth<1:
		return walk
	#Recursion to draw squares
	elif depth>=1:
		for _ in range(4):
			#Calculating how much turtle walked and drawing at the same time
			walk+=drawSquare(size/3,depth-1,number+1)
			if 0==(number%2):
				turtle.width(1)
			if 0!=(number%2):
				turtle.width(4)
			turtle.forward(size)
			walk+=size
			turtle.left(90)
		#return distance walked
		return walk
"""
This function takes input from the user and draws the figure according to that
"""
def Picture():
	walk=0
	turtle.speed(0)
	turtle.down()
	depth=int(input("Please enter the depth of recursion"))
	size=int(input("Please enter the size of largest square"))
	#Invalid size check
	if size<=0:
		print("Invalide size entered")
	#Invalid depth check
	elif depth<=0:
		print("Invalid recursion depth")
	else:
		walk=drawSquare(size,depth,1)
	print("Turtle moved:",walk)
	turtle.up()
	turtle.done()

"""
Calling the function
"""
if __name__=='__main__':
	Picture()