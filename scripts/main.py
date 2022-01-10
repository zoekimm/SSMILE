from collections import OrderedDict
import cv2 #openCV
#import dlib

FACIAL_LANDMARKS_INDEXES = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 35)),
	("jaw", (0, 17))
])

def detect_face(image, sf, neighbors, min_size): #opencv
    gimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    faces = face_cascade.detect(gimage, sf, neighbors, min_size)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)


def detect_face_dlib(grayimage, modelpath): #dlib
    frontalFaceDetector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(modelpath)
    faces = frontalFaceDetector(grayimage)
    labels = predictor(grayimage, faces)

    for k in range(0, len(allFaces)):
        faceRectangleDlib = dlib.rectangle(int(allFaces[k].left()),int(allFaces[k].top()),
        int(allFaces[k].right()),int(allFaces[k].bottom()))