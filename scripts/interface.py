from tkinter import *
import cv2
#import dlib

def takeImage(window):
    imageLabel = Label(window, text = "Type the full path for your image", font = ("Arial Bold", 20))
    imageLabel.grid(column=0, row=0)

    imagePath = Entry(window,width=10)
    imagePath.grid(column=1, row=0)

    clickButton1 = Button(window, text = "Load", command = loadImage(imageLabel))
    clickButton1.grid(column=2, row=0)

    print(imagePath.get())

    #img = cv2.imread(imagePath.get()) 
    #cv2.imshow("Selected image", img) #display 
    #cv2.waitKey(0)

def takeVideo(window):
    videoLabel = Label(window, text = "Type the full path for your video", font = ("Arial Bold", 20))
    videoLabel.grid(column=0, row=5)

    videoPath = Entry(window, width=10)
    videoPath.grid(column=1, row=5)

    clickButton2 = Button(window, text = "Load", command = loadVideo(videoLabel))
    clickButton2.grid(column=2, row=5)

    #vid = cv2.VideoCapture(videoPath)  

    #if not vid.isOpened():
    #    print('The program failed to open the video\n') #add error message 

    #while vid.isOpened():
    #    ret, frame = vid.read()
    #    if ret:
    #        cv2.imshow("Selected video", frame)  # display the image
    #        cv2.waitKey(0)

def loadImage(imageLabel): 
    imageLabel.configure(text= "Your image was successfully loaded")

def loadVideo(videoLabel):
    videoLabel.configure(text= "Your video was successfully loaded")

def main():
    window = Tk()
    window.title("SSMILE")
    window.geometry('500x300')

    takeImage(window)
    takeVideo(window)

    window.mainloop()

if __name__ == "__main__":
    main()

