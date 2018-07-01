# Stars in a night sky
from turtle import *
import random
bgcolor('DeepSkyBlue4')
def star(s, c):
    x, y = random.randint(-100, 100), random.randint(-100, 100)
    penup()
    goto(x, y) # goto() creates black line at the start so we have to lift pen up
    begin_fill()
    color(c)
    pendown()
    for i in range(5):
        forward(s)
        right(144)
    end_fill()
    

for s in range(20):
    star(10, 'white')

mainloop()
