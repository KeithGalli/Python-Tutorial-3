import turtle

def draw_pentagon(turtle,x,y):
	turtle.penup()
	turtle.goto((x,y))
	turtle.pendown()

	turtle.begin_fill()
	turtle.setheading(0)
	turtle.forward(50)
	turtle.left(72)
	turtle.forward(50)
	turtle.left(72)
	turtle.forward(50)
	turtle.left(72)
	turtle.forward(50)
	turtle.left(72)
	turtle.forward(50)
	turtle.end_fill()	

bob = turtle.Turtle()

bob.speed(4)

bob.color("blue", "cyan")

draw_pentagon(bob,-250,100)
draw_pentagon(bob,-100,100)
draw_pentagon(bob,50,100)
draw_pentagon(bob,200,100)
draw_pentagon(bob,-250,-50)
draw_pentagon(bob,-100,-50)
draw_pentagon(bob,50,-50)
draw_pentagon(bob,200,-50)

turtle.done()