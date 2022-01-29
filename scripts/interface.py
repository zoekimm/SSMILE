from tkinter import *
import cv2
import face_detection
#import dlib

def takeImage(window, path):
    imageLabel = Label(window, text = "Type the full path for your image", font = ("Arial Bold", 20))
    imageLabel.grid(column=0, row=0)

    imagePath = Entry(window, textvariable=path, width=10)
    imagePath.grid(column=1, row=0)

    def loadImage(): 
        imageLabel.configure(text = "Your image was successfully loaded")
        img = cv2.imread(path.get()) 
        face_detection.main(path.get())
        #cv2.imshow("Selected image", img) #display 
        #if cv2.waitKey(0) & 0xFF == ord('q'):
        #    cv2.destroyAllWindows()

    clickButton1 = Button(window, text = "Load", command = loadImage)
    clickButton1.grid(column=2, row=0)
    

def takeVideo(window, path):
    videoLabel = Label(window, text = "Type the full path for your video", font = ("Arial Bold", 20))
    videoLabel.grid(column=0, row=5)

    videoPath = Entry(window, width=10)
    videoPath.grid(column=1, row=5)

    def loadVideo():
        videoLabel.configure(text= "Your video was successfully loaded")

        #vid = cv2.VideoCapture(videoPath)  

        #if not vid.isOpened():
        #    print('The program failed to open the video\n') #add error message 

        #while vid.isOpened():
        #    ret, frame = vid.read()
        #    if ret:
        #        cv2.imshow("Selected video", frame)  # display the image
        #        cv2.waitKey(0)

    clickButton2 = Button(window, text = "Load", command = loadVideo)
    clickButton2.grid(column=2, row=5)

def main():
    window = Tk()
    window.title("SSMILE")
    window.geometry('500x300')

    path = StringVar()

    takeImage(window, path)
    takeVideo(window, path)

    window.mainloop()

if __name__ == "__main__":
    main()


