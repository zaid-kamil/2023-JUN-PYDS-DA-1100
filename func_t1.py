from turtle import *

# function definition
def square(size, color='red'):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        fd(size)
        rt(90)
    end_fill()

def hexagon(size, color='green'):
    fillcolor(color)
    begin_fill()
    for i in range(6):
        fd(size)
        rt(60)
    end_fill()

hexagon(100)
square(100, 'blue') # calling
hexagon(50)
square(50,'green')
square(25,'yellow')

mainloop()

