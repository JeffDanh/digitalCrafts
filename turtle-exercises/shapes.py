# Draw a square
from turtle import *
def square(s, c):
    begin_fill()
    color(c)
    forward(s)
    right(90)
    forward(s)
    right(90)
    forward(s)
    right(90)
    forward(s)
    end_fill() 
square(100, 'red')

# Draw a circle
from turtle import *
def cir(s, c):
    begin_fill()
    color(c)
    pencolor(c)
    width(5)
    circle(s)
    end_fill()
cir(100, 'Olivedrab')

# Draw a star
from turtle import *
def star(s, c):
    begin_fill()
    color(c)
    for i in range(5):
        forward(s)
        right(144)
    end_fill()
star(100, 'Blue')

# Draw an octagon
from turtle import *
def octa(s, c):
    begin_fill()
    color(c)
    for i in range(8):
        left(45)
        forward(s)
    end_fill()
octa(100, 'Pink')


# Triangle
from turtle import *
def triangle(s, c):
    begin_fill()
    color(c)
    forward(s)
    right(120)
    forward(s)
    right(120)
    forward(s)
    right(120)
    end_fill()
triangle(100, 'Green')

# Pentagon
from turtle import *
def pentagon(s, c):
    begin_fill()
    color(c)
    for i in range(5):
        left(72)
        forward(s)
    end_fill()
pentagon(100, 'Gold')

# Hexagon
from turtle import *
def hexagon(s, c):
    begin_fill()
    color(c)
    for i in range(6):
        left(60)
        forward(s)
    end_fill()
    mainloop()
hexagon(100, 'DarkOrchid')
