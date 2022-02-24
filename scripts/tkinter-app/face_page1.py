from tkinter import *
import tkinter
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import cv2

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
canvas.create_text(WIDTH/2, 95, fill = "Black", font = "Roboto 20", text = "Click your options below (Image/Webcam)")

load_text = StringVar()

load_button = Button(window,
        textvariable = load_text,
        command = lambda:open_file(),
        highlightbackground = 'white',
        width=15)

load_text.set("Image Load")

load_button.place(x = 400, y = 600, anchor = "center")

def open_web_cam():
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while cv2.waitKey(33) < 0:
                ret, frame = capture.read()
                cv2.imshow("Face Detection (Webcam)", frame)

        capture.release()
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
        return 

web_cam_button = Button(window,
        text = 'Webcam', 
        command = lambda:open_web_cam(),
        highlightbackground = 'white',
        width=15)

web_cam_button.place(x = 400, y = 680, anchor = "center")

window.mainloop()

