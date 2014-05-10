import turtle 

sat = turtle.Turtle()

sat.hideturtle()
sat.speed(20)

for i in range(10, 100):
	sat.right(100)
	sat.forward(i)
