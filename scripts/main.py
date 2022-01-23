import dlib
import cv2
import numpy as np

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor('/content/shape_predictor_68_face_labels_GTX.dat')
img = cv2.imread('/content/human_face.jpg')
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mouthpoints = []

faces = detector(grayimg)

for face in faces:
	
  labels = shape_predictor(grayimg, face)

  for n in range(0,68):
      x = labels.part(n).x
      y = labels.part(n).y
      #cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
      if n in range(48, 67):
        mouthpoints.append((x,y))

  #print(mouthpoints)

  xpoint = [x[0] for x in mouthpoints]
  ypoint = [x[1] for x in mouthpoints]
  
  for i in mouthpoints:
    if i[0] == min(xpoint):
      leftend = i
    if i[0] == max(xpoint):
      rightend = i

  #cv2.circle(image, center_coordinates, radius, color, thickness)
  cv2.circle(img, (leftend), 1, (0, 0, 255), -1) 
  cv2.circle(img, (rightend), 1, (0, 0, 255), -1)
  cv2.circle(img, ((leftend[0] + 10, leftend[1])), 1, (0, 0, 255), -1)

#cv2.imshow(img)