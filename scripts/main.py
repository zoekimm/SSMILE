import dlib
import cv2
import numpy as np

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
        
        for i in mouthpoints:
            if i[0] == min(xpoint):
                leftend = i
            if i[0] == max(xpoint):
                rightend = i

        #cv2.circle(image, center_coordinates, radius, color, thickness)
        cv2.circle(img, (leftend), 1, (0, 0, 255), -1) 
        cv2.circle(img, (rightend), 1, (0, 0, 255), -1)
        cv2.circle(img, ((leftend[0] + 10, leftend[1])), 1, (0, 0, 255), -1)

        angle = get_angle(leftend, rightend)
        if angle <= 175:
            print('!')
        else:
            print('symmetric')

    #cv2.imshow(img)

def main():
    face_detector = dlib.get_frontal_face_detector()
    shape_predictor = dlib.shape_predictor('/Users/minjeongkim/Desktop/SSMILE/scripts/shape_predictor_68_face_landmarks_GTX.dat')

    img = cv2.imread('/Users/minjeongkim/Desktop/SSMILE/scripts/human_face.jpg')
    
    get_labels(img, face_detector, shape_predictor)

if __name__ == "__main__":
    main()
