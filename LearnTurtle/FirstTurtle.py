import turtle


x = turtle.Turtle()

# makes a square
def square():
  x.forward(100)
  x.right(90)
  x.forward(100)
  x.right(90)
  x.forward(100)
  x.right(90)
  x.forward(100)

# makes a 4-square
square()
x.forward(1)
square()
x.forward(1)
square()
x.forward(1)
square()