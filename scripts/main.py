from tkinter import *
import cv2

import face_detection
import interface
#import dlib

window = Tk()
window.title("SSMILE")
window.geometry('500x300')

path = StringVar()

interface.takeImage(window, path)

window.mainloop()

#img_file_path = '/Users/minjeongkim/Desktop/SSMILE/scripts/human_face.jpg'
#face_detection.main(img_file_path)