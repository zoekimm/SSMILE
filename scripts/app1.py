import streamlit as st
from PIL import Image
from face_detection import get_labels
import dlib

@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img 

def run_face_detection():
    st.title('Face Detection')
    st.write('Face Detection Page')

    img_file = st.file_uploader('Upload Your Image', type = ['png', 'jpeg', 'jpg'])
    if img_file is None:
        pass
    else:
        st.image(load_image(img_file))
        with open(img_file.name, 'wb') as f:
            f.write(img_file.getbuffer())

    st.success('Image Uploaded')

    if st.button("Detection"):
        face_detector = dlib.get_frontal_face_detector()
        shape_predictor = dlib.shape_predictor('/Users/zoekim/Desktop/g/SSMILE/scripts/shape_predictor_68_face_landmarks_GTX.dat')

        #result_img = get_labels(img_file, face_detector, shape_predictor)
        #st.image(result_img)