from tkinter import *

def takeImage(window):
    imageLabel = Label(window, text = "Type the full path for your image", font = ("Arial Bold", 20))
    imageLabel.grid(column=0, row=0)

    imagepath = Entry(window,width=10)
    imagepath.grid(column=1, row=0)

    clickButton1 = Button(window, text = "Load", command = loadImage(imageLabel))
    clickButton1.grid(column=2, row=0)

def takeVideo(window):
    videoLabel = Label(window, text = "Type the full path for your video", font = ("Arial Bold", 20))
    videoLabel.grid(column=0, row=5)

    videoPath = Entry(window, width=10)
    videoPath.grid(column=1, row=5)

    clickButton2 = Button(window, text = "Load", command = loadVideo(videoLabel))
    clickButton2.grid(column=2, row=5)

def loadImage(imageLabel): #button click
    imageLabel.configure(text= "Your image was successfully loaded")


def loadVideo(videoLabel): #button click
    videoLabel.configure(text= "Your video was successfully loaded")

def main():
    print('here')
    window = Tk()
    window.title("SSMILE")
    window.geometry('500x300')
    takeImage(window)
    takeVideo(window)
    window.mainloop()

if __name__ == "__main__":
    main()

