# author: cactapus
import turtle

t = turtle.Turtle()

t.shape("circle")

n = int(input("How many legs does should this sprite have?"))

angle = 360 / n 

for i in range (0, n):
	
	t.forward(200)
	t.stamp()
	t.backward(200)
	t.left(angle)
	