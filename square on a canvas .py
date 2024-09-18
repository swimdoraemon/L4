import turtle


turtle.Screen().bgcolor("orange")

sc = turtle.Screen()
sc.setup(400,300)

turtle.title("Welcome to turtule window")


t = turtle.Turtle()


for i in range(4):
    t.fd(100)
    t.left(90)
    i =i+1