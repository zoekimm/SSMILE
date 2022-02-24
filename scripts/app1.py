import streamlit as st
from PIL import Image
from face_detection import get_labels
import dlib
import cv2
import os
import numpy as np

path = '/Users/zoekim/Desktop/g/SSMILE/scripts/'

@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img 

def run_face_detection():
    st.subheader('Face Detection')

    option = st.selectbox(
     'File Type',
     ('Select Your File Type', 'Image', 'WebCam'))

    if option == 'Please Select Your File Type':
        pass

    if option == 'Image':

        img_file = st.file_uploader('Upload Your Image', type = ['png', 'jpeg', 'jpg'])
        if img_file is None:
            pass
        else:
            st.image(load_image(img_file))
            with open(img_file.name, 'wb') as f:
                f.write(img_file.getbuffer())

        #st.success('Image Uploaded')
        if st.button("Detection"):
            face_detector = dlib.get_frontal_face_detector()
            shape_predictor = dlib.shape_predictor('/Users/zoekim/Desktop/g/SSMILE/scripts/shape_predictor_68_face_landmarks_GTX.dat')
            
            saved_img_file = cv2.imread(os.path.join(path, img_file.name))
            
            #st.image(saved_img_file)
            
            new_img = get_labels(saved_img_file, face_detector, shape_predictor)
            cv2.imwrite('new.jpg', new_img)
            st.image(Image.open('/Users/zoekim/Desktop/g/SSMILE/scripts/new.jpg'))
            os.remove('/Users/zoekim/Desktop/g/SSMILE/scripts/new.jpg')

    if option == 'WebCam':
        camera_file = st.camera_input("Upload your picture by web camera")
        if camera_file is not None:
            bytes_data = camera_file.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

            if st.button("Detection"):
                face_detector = dlib.get_frontal_face_detector()
                shape_predictor = dlib.shape_predictor('/Users/zoekim/Desktop/g/SSMILE/scripts/shape_predictor_68_face_landmarks_GTX.dat')
                
                new_img = get_labels(cv2_img, face_detector, shape_predictor)
                cv2.imwrite('new.jpg', new_img)
                st.image(Image.open('/Users/zoekim/Desktop/g/SSMILE/scripts/new.jpg'))
                os.remove('/Users/zoekim/Desktop/g/SSMILE/scripts/new.jpg')
            