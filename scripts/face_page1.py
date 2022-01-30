from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

#face detection page (image)

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
        file = askopenfile(parent = window, mode='rb', title = "Choose a file", filetypes=[("Image File",'.jpg')])

canvas.create_text(WIDTH/2, 50, fill = "Black", font = "Roboto 35 bold", text = "Face Detection")
canvas.create_text(WIDTH/2, 95, fill = "Black", font = "Roboto 20 bold", text = "Type the full path for your image")

load_text = StringVar()

load_button = Button(window,
        textvariable = load_text,
        command = lambda:open_file(),
        highlightbackground = 'white',
        fg = "black",
        height=2,
width=15)

load_text.set("Load")

load_button.place(x = 400, y = 700, anchor = "center")

window.mainloop()
