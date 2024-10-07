import turtle as t
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import random
import threading #allows code to multitask

#vars
moves = False
game_start = False
pos = 1
image_holder = 0 # holds current character image in canvas
object_selected = ""
msg = 0
textbox = 0
hold = True
score = 0
scoret = 0
wrongs = 0
#character movement check:
#functions


def character_movement(): #function for character movement
    global moves
    global pos
    while True: #while loop checks if character needs to move
        if moves == True:
            time.sleep(0.5) # updates every half second
            if pos == 1:
                pos = 2 #tells the system character position changed
                print(pos) # checks if it is running since while loop could crash
                canvas.itemconfig(image_holder, image = c_move_tk2) #changes the character position
            elif pos == 2:
                pos = 1 #tells the system character position changed
                print(pos) # checks if it is running since while loop could crash
                canvas.itemconfig(image_holder, image = c_move_tk) #changes the character position
b = threading.Thread(name='background', target=character_movement) #variable threads the function, so it runs in background

def bin1_command():
    global msg
    global hold
    global score
    global scoret
    global wrongs
    if object_selected == "Glass" or object_selected == "Jar":
        print("Correct!") #terminal outputs answer to see if works
        msg.config(text = "         Correct!") # Tells player they are correct
        score = score+30
        scoret.config(text = "Score: "+str(score))
        time.sleep(1)
        hold = False
    else:
        msg.config(text = "     Wrong Anwer!") # Tells player they are incorrect
        time.sleep(1)
        wrongs = wrongs+1
        hold = False

def bin2_command():
    global msg
    global hold
    global score
    global scoret
    global wrongs
    if object_selected == "Tissue" or object_selected == "Foil":
        print("Correct!") #terminal outputs answer to see if works
        msg.config(text = "         Correct!") # Tells player they are correct
        score = score+30
        scoret.config(text = "Score: "+str(score))
        time.sleep(2)
        hold = False
    else:
        msg.config(text = "     Wrong Anwer!") # Tells player they are incorrect
        time.sleep(2)
        wrongs = wrongs+1
        hold = False

def bin3_command():
    global msg
    global hold
    global score
    global scoret
    global wrongs
    if object_selected == "Plastic" or object_selected == "Card":
        print("Correct!") #terminal outputs answer to see if works
        msg.config(text = "         Correct!") # Tells player they are correct
        score = score+30
        scoret.config(text = "Score: "+str(score))
        time.sleep(2)
        hold = False
    else:
        msg.config(text = "     Wrong Anwer!") # Tells player they are incorrect
        time.sleep(2)
        wrongs = wrongs+1
        hold = False

def texting_command():
    global textbox
    global hold
    global score
    global scoret
    global wrongs
    print(textbox.get("1.0","end"))
    if object_selected == "Battery" or object_selected == "Clothes" or object_selected == "Paper":
        if textbox.get("1.0","end-1c") == "yes": #gets text typed by user
            print("said yes")
            msg.config(text = "         Correct!")
            score = score+30
            scoret.config(text = "Score: "+str(score))
            time.sleep(2)
            hold = False
        else:
            msg.config(text = "     Wrong Anwer!")
            time.sleep(2)
            wrongs = wrongs+1
            hold = False
    elif object_selected == "Nappy" or object_selected == "Styrofoam" or object_selected == "Wipes":
        if textbox.get("1.0","end-1c") == "no": #gets text typed by user
            print("said no")
            msg.config(text = "         Correct!")
            score = score+30
            scoret.config(text = "Score: "+str(score))
            time.sleep(2)
            hold = False
        else:
            msg.config(text = "     Wrong Anwer!")
            time.sleep(2)
            wrongs = wrongs+1
            hold = False

def maingame(): #main game logic
    global moves
    global object_selected
    global msg
    global hold
    global textbox
    global wrongs
    print("game started")
    while wrongs < 1:
        hold = True
        time.sleep(0.2)
        if game_start == True:
            rand_num = random.randint(1,15) #anywhere between 1 and 30 seconds
            rand_obj1 = random.randint(0,1) # there are 2 types of questions to chose from: 0="click the correct bin", 1="yes/no question"-
                                            #this adds more interactivity to the game
            rand_obj2 = random.randint(0,5) #there are 6 objects to chose from either side
            objects = ["Jar","Glass","Plastic","Card","Tissue","Foil"], ["Battery","Clothes","Paper","Nappy","Styrofoam","Wipes"] #array of possible items
            print(objects[rand_obj1][rand_obj2])
            object_selected = str(objects[rand_obj1][rand_obj2])
            time.sleep(rand_num)
            msg = tk.Label(master=window,
                            text="Oh, you found: " + str(objects[rand_obj1][rand_obj2]),
                            font="Helvetica 20 bold",
                            foreground="Black",
                            background="#0ab5ff")
            message_box = canvas.create_window(290,142,anchor="nw",window=msg)
            moves = False #stops character
            if rand_obj1 == 0:
                binx1 = tk.Button(master = window,
                       activebackground="#0ab5ff",
                       background="#0ab5ff",
                       border=0,
                       borderwidth=0,
                       image= bin1_tk,
                       relief="solid",
                       command = bin1_command)
                binx2 = tk.Button(master = window,
                       activebackground="#0ab5ff",
                       background="#0ab5ff",
                       border=0,
                       borderwidth=0,
                       image= bin2_tk,
                       relief="solid",
                       command = bin2_command)
                binx3 = tk.Button(master = window,
                       activebackground="#0ab5ff",
                       background="#0ab5ff",
                       border=0,
                       borderwidth=0,
                       image= bin3_tk,
                       relief="solid",
                       command = bin3_command)
                binbut1 = canvas.create_window(220,180,anchor="nw",window=binx1)
                time.sleep(0.1) #makes the entry of bins more dramatic
                binbut2 = canvas.create_window(390,180,anchor="nw",window=binx2)
                time.sleep(0.1)
                binbut3 = canvas.create_window(560,180,anchor="nw",window=binx3)
                while hold == True:
                    time.sleep(1.5)
                canvas.delete(binbut1)
                canvas.delete(binbut2)
                canvas.delete(binbut3)
                canvas.delete(message_box)
                moves = True
            if rand_obj1 == 1:
                question = tk.Label(master=window,
                                    background="#0ab5ff",
                                    text="Can This Be Recycled?",
                                    font="Helvetica 20 bold")
                textbox = tk.Text(master=window,
                                  #border=0,
                                  borderwidth=1,
                                  background="white",
                                  width=20,
                                  height=1,
                                  foreground="black")
                confirmbutton = tk.Button(master = window,
                       activebackground="light green",
                       background="light green",
                       #border=0,
                       borderwidth=1,
                       relief="solid",
                       text="Confirm",
                       command = texting_command)
                questionbox = canvas.create_window(278,200,anchor="nw",window=question)
                textbut = canvas.create_window(330,310,anchor="nw",window=textbox)
                confirm = canvas.create_window(510,310,anchor="nw",window=confirmbutton)
                while hold == True:
                    time.sleep(0.1)
                time.sleep(1.5)
                canvas.delete(questionbox)
                canvas.delete(textbut)
                canvas.delete(confirm)
                canvas.delete(message_box)
                moves = True
    moves = False
    game_over = tk.Label(master=window,
                         text="GAME OVER!",
                         background="#0ab5ff",
                         font="Helvetica 30 bold") 
    game_over_screen = canvas.create_window(300,240,anchor="nw",window=game_over)

m = threading.Thread(name='maingame', target=maingame) #variable threads the function, so the main game runs in background

def game_initialise(): #start up game page
    global moves
    global image_holder
    global b
    global game_start
    global score
    global scoret
    time.sleep(1) #gives time for the player to get ready
    canvas.delete(back)
    canvas.delete(playbuttonwindow)
    canvas.create_image(0,0,image = backimg_tk,anchor = "nw")
    image_holder = canvas.create_image(20,145,image = c_move_tk,anchor = "nw")
    moves = True #allows the character to start moving
    b.start() #thread runs in background as soon as we start the game - allowing the character to move nonetheless
    m.start() #this allows the game logic to start running along with everything else
    scoret = tk.Label(master=window,
                     text="Score: "+str(score),
                     bg = "white",
                     font="Arial 20",
                     borderwidth=0)
    scorewindow = canvas.create_window(340,42,anchor="nw", window=scoret)
    game_start = True
    

#window setup

window = tk.Tk()
window.title("The Environment Game")
window.geometry("800x500")
#image imports and setup
backimg = Image.open("backgroundgame.png").resize((800,500))
backimg_tk = ImageTk.PhotoImage(backimg)
titleimg = Image.open("titlebackground.png").resize((800,500))
titleimg_tk = ImageTk.PhotoImage(titleimg)
buttonimg = Image.open("Play.png")#.resize((500,300))
buttonimg_tk = ImageTk.PhotoImage(buttonimg)
c_move = Image.open("c_move.png")
c_move_tk = ImageTk.PhotoImage(c_move)
c_move2 = Image.open("c_move_2.png")
c_move_tk2 = ImageTk.PhotoImage(c_move2)
bin1 = Image.open("Bin1.png").resize((100,200))
bin1_tk = ImageTk.PhotoImage(bin1)
bin2 = Image.open("Bin2.png").resize((100,200))
bin2_tk = ImageTk.PhotoImage(bin2)
bin3 = Image.open("Bin3.png").resize((100,200))
bin3_tk = ImageTk.PhotoImage(bin3)

canvas = tk.Canvas(window,width=800,height=500)
canvas.pack()
#loading title screen
back = canvas.create_image(0,0,image = titleimg_tk,anchor = "nw")
#play button
playbutton = tk.Button(master = window,
                       activebackground="#0ab5ff",
                       #text = "PLAY",
                       #font="Calibri 14",
                       background="#0ab5ff",
                       #foreground="white", --these are additional parameters required for button previously but now they are replaced by the image
                       #width=15,
                       #height=1,
                       border=0,
                       borderwidth=0,
                       image= buttonimg_tk,
                       command=game_initialise)
playbuttonwindow = canvas.create_window(305,325,anchor="nw",window=playbutton)
window.mainloop()