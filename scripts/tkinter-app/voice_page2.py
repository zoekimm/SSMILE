from tkinter import *
import tkinter
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import cv2

HEIGHT = 800
WIDTH = 800

window = Tk()
window.title("SSMILE")

frame = Frame(window)
frame.pack()

canvas = Canvas(frame, bg = "white", width = WIDTH, height = HEIGHT)
canvas.pack()

def open_file():
        load_text.set("loading...")
        file = askopenfile(parent = window, mode='rb', title = "Choose a file", filetypes=[("Audio file",'.wav')])

canvas.create_text(WIDTH/2, 50, fill = "Black", font = "Roboto 35 bold", text = "Audio test")
canvas.create_text(WIDTH/2, 95, fill = "Black", font = "Roboto 20", text = "Browse your audio file below")

load_text = StringVar()

load_button = Button(window,
        textvariable = load_text,
        command = lambda:open_file(),
        highlightbackground = 'white',
        width=15)

load_text.set("Audio Load")

load_button.place(x = 400, y = 600, anchor = "center")

window.mainloop()

