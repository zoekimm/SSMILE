import dlib
import numpy as np
from app1 import run_face_detection
from app2 import run_audio_evaluation
import app2
import streamlit as st
from css import load_css

#dict for pages
def main():

    st.title('SSMILE')
    pages = ['Home', 'Face Detection', 'Audio Evaluation']
    choice = st.sidebar.radio('Select Pages', pages)

    load_css("style.css")
    if choice == 'Home':
        st.header('Stroke Screening Made Instant, Live, and Easy')
        st.subheader('Why SSMILE?')
        info_text = """<div>With more than
            <span class='highlight red'>fifteen million</span>
            cases of <span class='bold'>stroke</span> worldwide every year and many more 
            complications arising from stroke,</span>
            <span class='highlight yellow'> early detection of stroke is significant 
            to prevent any further brain damage and to possibly decrease both mortality and morbidity.</span></span>
            </div>"""
        st.markdown(info_text, unsafe_allow_html=True)
        st.markdown("""This web application helps one determine whether one has facial asymmetry, one of the most common symptoms of stroke, with an image of one's face or through web camera""")



    elif choice == 'Face Detection':
        run_face_detection()
    elif choice == 'Audio Evaluation':
        run_audio_evaluation()

if __name__ == '__main__':
    main()

