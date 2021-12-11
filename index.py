from tkinter import *

root = Tk() #Referance to TK()

#Width x Height
root.geometry("644x434")

#width, height
root.minsize(300,100) # min size of window
root.maxsize(1200,988) # max size of window

#label 
label = Label(text="Hello ji")
label.pack() #must do else not work

root.mainloop() # main window tk