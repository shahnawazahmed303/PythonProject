import os
from tkinter import *
from PIL import Image , ImageTk

root = Tk() #Referance to TK()

#Width x Height
root.geometry("404x428")

#title
title = "TKinyer ["+os.getcwd()+"] - Shah nawaz"
root.title(title)

#width, height
root.minsize(400,400) # min size of window
root.maxsize(800,800) # max size of window

#label 
label = Label(text="Hello ji")
label.pack() #must do else not work

#img

photo = Image.open("img/1.png")
img = ImageTk.PhotoImage(photo)
img_label = Label(image=img)
img_label.pack()

# main window tk
root.mainloop() 