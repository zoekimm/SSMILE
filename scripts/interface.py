from tkinter import *


window = Tk()
window.title("SSMILE")
window.geometry('500x300')
imageLabel = Label(window, text = "Type the full path for your image", font = ("Arial Bold", 20))
imageLabel.grid(column=0, row=0)

imagepath = Entry(window,width=10)
imagepath.grid(column=1, row=0)

def loadImage(): #button click
    imageLabel.configure(text= "Your image was successfully loaded")

clickButton1 = Button(window, text = "Load", command = loadImage)
clickButton1.grid(column=2, row=0)

videoLabel = Label(window, text = "Type the full path for your video", font = ("Arial Bold", 20))
videoLabel.grid(column=0, row=5)

videoPath = Entry(window, width=10)
videoPath.grid(column=1, row=5)

def loadVideo(): #button click
    videoLabel.configure(text= "Your video was successfully loaded")

clickButton2 = Button(window, text = "Load", command = loadVideo)
clickButton2.grid(column=2, row=5)

window.mainloop()
