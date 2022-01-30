from tkinter import *
import cv2

window = Tk()
window.title("SSMILE")
window.geometry('500x300')
window['bg'] = '#121c26'
f = ("Times bold", 14)
 
imageLabel = Label(window, 
        text = "Face Detection",
        font = ("Arial Bold", 20),
        bg = "#121c26",
        fg="white")
imageLabel.grid(column=1, row=0)

instructions = Label(window,
        text = "Type the full path for your image",
        font = f, 
        bg = "#121c26",
        fg="white")
instructions.grid(column=1, row=1)

def open_file():
    load_text.set("loading...")

load_text = StringVar()

load_button = Button(window,
        textvariable = load_text,
        command = lambda:open_file(),
        font = f, bg = "#121c26",
        fg = "black",
        height=2,
width=15)

load_text.set("Load")
load_button.grid(column=1, row=2)

window.mainloop()
