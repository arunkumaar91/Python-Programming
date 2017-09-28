import turtle

window = turtle.Screen()

# To Draw Square
def drawing_square(some_art):
    for i in range(0,4):
        some_art.forward(100)
        some_art.right(90)

# To draw SquareCircle
def drawing_sqrCircle():
    window.bgcolor("blue")
    sqr = turtle.Turtle()
    sqr.shape("arrow")
    sqr.color("black")
    sqr.speed(50)
    for i in range(1,37):
        drawing_square(sqr)
        sqr.right(10)

    for i in range(37,38):
        sqr.right(90)
        sqr.forward(300)

# To Draw Circle
##def drawing_circle():
##    
##    cir = turtle.Turtle()
##    cir.shape("turtle")
##    cir.color("yellow")
##    cir.circle(50)
##    cir.speed(2)
##
### To Draw Triangle
##def drawing_triangle():
##    count = 0
##    tri = turtle.Turtle()
##    tri.shape("arrow")
##    tri.color("red")
##    tri.speed(2)
##    while (count < 3):
##        tri.right(60)
##        tri.forward(90)
##        tri.right(60)
##        count = count + 1

drawing_sqrCircle()
##drawing_square()
##drawing_circle()
##drawing_triangle()
window.exitonclick()
