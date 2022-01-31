from tkinter import *
from PIL import Image, ImageTk

HEIGHT = 800
WIDTH = 800

window = Tk()
window.title("SSMILE")

frame = Frame(window)
frame.pack()

canvas = Canvas(frame, bg = "white", width = WIDTH, height = HEIGHT)
canvas.pack()

def nextPage():
    window.destroy()
    import face_page1

def prevPage():
    window.destroy()
    #import audio_page2

canvas.create_text(WIDTH/2, 50, fill = "Black", font = "Roboto 35 bold", text = "S S M I L E")
canvas.create_text(WIDTH/2, 95, fill = "Black", font = "Roboto 20 bold", text = "Stroke Screening Made Instant, Live, and Easy :)")

emoji_image = ImageTk.PhotoImage(file="/Users/zoekim/Desktop/git_SSMILE/SSMILE/scripts/smile_emoji3.png")
canvas.create_image(WIDTH/2, HEIGHT/2, anchor="center", image = emoji_image)

btn1 = Button(window, text = 'Welcome to SSMILE!', highlightbackground = 'white')
btn2 = Button(window, text = 'Face Detection', highlightbackground = 'white', command = nextPage)
btn3 = Button(window, text = 'Audio Test', highlightbackground = 'white')

btn1.place(x = 400, y = 700, anchor = "center")
btn2.place(x = 400, y = 730, anchor = "center")
btn3.place(x = 400, y = 760, anchor = "center")

window.mainloop()
