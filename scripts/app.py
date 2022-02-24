import dlib
import numpy as np
from app1 import run_face_detection
from app2 import run_audio_evaluation
import app2
import streamlit as st

#dict for pages
def main():

    st.title('SSMILE')
    st.header('Stroke Screening Made Instant, Live, and Easy')

    pages = ['Home', 'Face Detection', 'Audio Evaluation']
    choice = st.sidebar.radio('Select Pages', pages)
    
    if choice == 'Home':
        st.subheader('Why SSMILE?')
        st.markdown("""
        With fifteen million cases of stroke worldwide every year and many more 
        complications arising from stroke, early detection of stroke is significant 
        to prevent any further brain damage and to possibly decrease both mortality and morbidity.
        This StreamLit WebApp helps one determine whether one has facial asymmetry,
        one of the most common symptoms of stroke, with an image of one's face or through web camera.
        """)

        #picture = st.camera_input("Take a picture")

        #if picture:
            #st.image(picture)


    elif choice == 'Face Detection':
        run_face_detection()
    elif choice == 'Audio Evaluation':
        run_audio_evaluation()

if __name__ == '__main__':
    main()

