from tkinter import *


window = Tk()
window.title("SSMILE")
window.geometry('500x300')
imageLabel = Label(window, text = "Type the full path for your image", font = ("Arial Bold", 20))
imageLabel.grid(column=0, row=0)

imagepath = Entry(window,width=10)
imagepath.grid(column=1, row=0)

def loaded(): #button click
    imageLabel.configure(text= "Image was successfully loaded")

clickButton = Button(window, text = "Load", command = loaded)
clickButton.grid(column=2, row=0)
window.mainloop()
