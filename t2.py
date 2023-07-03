from turtle import *

pencolor('yellow')
pensize(2)
bgcolor('black')
speed('fastest')

for i in range(6):
    fd(100)
    rt(360/6)
    for i in range(6):
        fd(50)
        rt(360/6)
for i in range(6):
    fd(100)
    lt(360/6)
    for i in range(6):
        fd(50)
        lt(360/6)



hideturtle()
mainloop()