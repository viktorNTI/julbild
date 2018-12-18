from turtle import *
import time

speed(0)

colormode(255)
bgcolor(255,0,0)
pencolor(255,255,255)

pensize(4)

for i in range(50):
    forward(50)
    right(144)

left(90)
forward(200)

write("Finaste Julstjärnan i hela universum", font=("Georgia", 16, "normal"))
time.sleep(4)

left(90)
forward(270)

pencolor(255,247,0)

for i in range(20):
    forward(i * 10)
    right(144)

pencolor(90,255,0)

write("Nej, jag är bättre.", font=("Georgia", 16, "normal"))
time.sleep(4)

back(100)
right(90)
right(90)
right(90)
forward(300)

pencolor(0,255,235) 

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

forward(50)
left(90)

pencolor(11,0,255)

write("Fyrkant är bättre än stjärna", font=("Georgia", 16, "normal"))
time.sleep(4)

done()





