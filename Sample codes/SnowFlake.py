import turtle

def newSnow(size,n):
	x=size/2
	y=.4
	if n<=0 or size<10:
		return
	else:
		for i in range(2):
			if n%2==0:
				turtle.color("#0099CC")
			elif n%3==0:
				turtle.color("#B2DFEE")
			else:
				turtle.color("#00B2EE")
			turtle.forward(y*size/2)
			turtle.left(60)
			newSnow(x,n-1)
			turtle.right(120)
			newSnow(x,n-1)
			turtle.left(60)
			x/=2
			y+=.2
		if n%2==0:
				turtle.color("#0099CC")
		elif n%3==0:
			turtle.color("#B2DFEE")
		else:
			turtle.color("#00B2EE")
		turtle.forward(.4*size/2)
		turtle.up()
		turtle.back(1.4*size/2)
		turtle.down()
	return
def drawBase(size,n,widthh):
	turtle.width(widthh)
	widthh+=.5
	if n<0:
		return
	else:
		turtle.forward(size)
		turtle.left(120)
		for i in range(6):
			turtle.forward(size)
			turtle.left(60)
		turtle.right(120)
		turtle.back(size)
		drawBase(.8*size,n-1,widthh)
	return


def newFlake():
	widthh=5
	for i in range(6):
		turtle.left(60)
		newSnow(400,3)
	turtle.color("#BFEFFF")
	drawBase(.4*400/2,10,widthh)
	return
turtle.speed(0)
newFlake()
turtle.hideturtle()
input("Press anything")