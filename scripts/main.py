from tkinter import *
import cv2
import interface

window = Tk()
window.title("SSMILE")
window.geometry('500x300')
window['background'] = '#F5FF52'

f = ("Times bold", 14)

def nextPage():
    window.destroy()
    import face_page1

def prevPage():
    window.destroy()
    import audio_page2
    
Label(
    window,
    text = 'SSMILE',
    bg = '#F5FF52',
    font = ("Times bold", 30)
).pack(expand=True, fill=BOTH)

Label(
    window,
    text = 'Stroke Screening Made Instant, Live, and Easy :)',
    bg = '#F5FF52',
    font = ("Times bold", 20)
).pack(expand=True, fill=BOTH)

Button(
    window,
    text = "Previous Page", 
    font = f,
    command = nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    window, 
    text = "Next Page", 
    font = f,
    command = prevPage
    ).pack(fill=X, expand=TRUE, side = RIGHT)

#path = StringVar()

#interface.takeImage(window, path)

window.mainloop()

#img_file_path = '/Users/minjeongkim/Desktop/SSMILE/scripts/human_face.jpg'
#face_detection.main(img_file_path)

