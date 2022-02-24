import dlib
import cv2
import numpy as np
import streamlit as st
from PIL import Image

def get_angle(leftend, rightend):
    x = np.array(leftend)
    y = np.array((leftend[0] + 2, leftend[1]))
    z = np.array(rightend)
    xy = x - y
    yz = z - y
    cos_ang = np.dot(xy, yz) / (np.linalg.norm(xy) * np.linalg.norm(yz))
    ang = np.arccos(cos_ang)
    return np.degrees(ang)

def get_labels(img, face_detector, shape_predictor):

    #img = np.asanyarray(img)
    #img = cv2.convertScaleAbs(img, alpha=0.03)
    #img = np.array(cv2.convert(img))
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    mouthpoints = []

    faces = face_detector(grayimg)

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
        
        maxx = max(xpoint)
        minx = min(xpoint)
        maxy = max(ypoint)
        miny = min(ypoint) 

        for i in mouthpoints:
            if i[0] == min(xpoint):
                leftend = i
            if i[0] == max(xpoint):
                rightend = i

        #cv2.circle(img, center_coordinates, radius, color, thickness)
        start_point = (leftend)
        middle_point = ((leftend[0] + 10, leftend[1]))
        end_point = (rightend)
        
        cv2.circle(img, (leftend), 2, (255, 255, 255), -1) 
        cv2.circle(img, (rightend), 2, (255, 255, 255), -1)
        cv2.circle(img, ((leftend[0] + 10, leftend[1])), 2, (255, 255, 255), -1)

        #cv2.line(image, start_point, end_point, color, thickness)
        cv2.line(img, start_point, middle_point, (255, 255, 255), 1)
        cv2.line(img, middle_point, end_point, (255, 255, 255), 1)

        angle = get_angle(leftend, rightend)

        if angle <= 175:
            st.error(angle)
        else:
            st.success(angle)

    pad = 15
    crop_image = img[miny-pad:maxy+pad,minx-pad:maxx+pad]
    crop_image = cv2.resize(crop_image, (0,0), fx=3, fy=3) 
    return crop_image

    #return img

    #cv2.imshow("Selected image", img) #display 
    #if cv2.waitKey(0) & 0xFF == ord('q'):
    #    cv2.destroyAllWindows()

def main(img_file_path):
    face_detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor('/Users/minjeongkim/Desktop/SSMILE/scripts/shape_predictor_68_face_landmarks_GTX.dat')
    img = cv2.imread(img_file_path)
    get_labels(img, face_detector, shape_predictor)

if __name__ == "__main__":
    img_file_path = '/Users/minjeongkim/Desktop/SSMILE/scripts/human_face.jpg'
    main(img_file_path)
