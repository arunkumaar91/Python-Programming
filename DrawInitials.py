import turtle

window = turtle.Screen()

# Draw letter S

def draw_s():
    window.bgcolor("green")
    letter = turtle.Turtle()
    letter.shape("arrow")
    letter.color("black")
    letter.speed(50)
    #letter.up()
    #letter.setpos(0,0)
    #letter.down()
    letter.goto(20,50)
    
draw_s()
