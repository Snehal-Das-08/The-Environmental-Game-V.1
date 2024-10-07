import turtle as t
import tkinter as tk
from tkinter import ttk
import time
import random

#setup of turtle
t.hideturtle()          #hides original turtle
screen = t.Screen()     #opens up a new window
screen.setup(800,500)   #sets geometric size of screen
screen.title("The Environment Game") # sets name of window
pen = t.Turtle()        #creates new turtle under variable pen
pen.hideturtle()        #hides the turtle
pen.speed(0)              #sets turtle's speed to be instant (no animations)

#functions
def draw_btn(text,x,y): #uses 3 paramaters for location and conteants of button
    pen.pensize(1)
    pen.goto(x-50,y+15) #starts at top left
    pen.pendown()
    pen.setheading(0)
    pen.forward(100)
    pen.setheading(270)
    pen.forward(30)
    pen.setheading(180)
    pen.forward(100)
    pen.setheading(90)
    pen.forward(30)
    pen.penup()
    pen.pos()
    pen.goto(x,y-8) #due to nature of writing the y-position has to go a bit lower to fit
    pen.write(text,align = "center",font = ("Arial",12,"normal"))
    return 

# pen customisation
pen.pensize(5)
pen.penup()
pen.goto(0,200)
pen.write("The Environment Game",
          False,
          align="center",
          font = ("Calibri Bold",20,"normal"))
#button = ttk.Button(master = screen, text = "convert")
#button.pack()
time.sleep(1) # give time for the game to really load
screen.mainloop()
#location = 

