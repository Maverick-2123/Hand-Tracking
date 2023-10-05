from tkinter import *
from tkinter import messagebox
from handGestures import hand_function

def start_application():
    response = messagebox.askyesno("Start Camera","Do you want to show the camera output?\n Note:- Click No, to save power")
    if response == True:
        hand_function(1)
        root.destroy()
    else:
        hand_function(0)
        root.destroy()
root = Tk()
root.geometry("500x500")
root.config(bg = "#f29b0f")
start_label = Label(root, text = "HAND TRACKING APPLICATION")
start_label.place(x = 70, y = 50)
start_label.config(font = ("Verdana 15 bold"),bg = "#f29b0f",fg = "blue")
start_button = Button(root, text = "Start Application")
start_button.config(font = ("Verdana 10 bold"))
start_button.place(x = 70, y = 300)
start_button.config(width=40, command = start_application)
root.mainloop()