from turtle import *
import time

up()
goto(-100,90)
down()

fillcolor('firebrick')
begin_fill()
right(90)
for i,j in zip([190,190],[90,90]):
    forward(i)
    left(j)
    forward(35)
    left(j)
end_fill()

up()
goto(-22,90)
down()

begin_fill()
for i,j in zip([190,190],[90,90]):
    forward(i)
    left(j)
    forward(35)
    left(j)
end_fill()

up()
goto(-100,90)
down()
left(23)

fillcolor('red')
begin_fill()
for i in range(2):
    forward(205)
    left(67)
    forward(35)
    left(113)
end_fill()
bgcolor('black')
time.sleep(5)
    
