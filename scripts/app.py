import dlib
import numpy as np
from app1 import run_face_detection
import app2
import streamlit as st

#dict for pages
def main():
    st.title('SSMILE')
    pages = ['Face Detection', 'Audio Evaluation']
    choice = st.sidebar.radio('Select Pages', pages)

    if choice == 'Face Detection':
        run_face_detection()
    
if __name__ == '__main__':
    main()

