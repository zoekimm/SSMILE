import cv2 #openCV
import dlib

def read_image():
    path = input('Type the full path for your image\n')
    img = cv2.imread(path) #read the image
    cv2.imshow("Selected image", img) #display the image
    cv2.waitKey(0)

def read_video():
    path = input('Type the full path for your video\n')
    vid = cv2.VideoCapture(path)  # read the image
    if not vid.isOpened():
        print('The program failed to open the video\n')

    while vid.isOpened():
        ret, frame = vid.read()
        if ret:
            cv2.imshow("Selected video", frame)  # display the image
            cv2.waitKey(0)

def detect_face(image, sf, neighbors, min_size): #opencv
    gimage =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    faces = face_cascade.detect(gimage, sf, neighbors, min_size)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)


def detect_face(modelpath): #dlib
    frontalFaceDetector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(modelpath)