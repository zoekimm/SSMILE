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
    pages = ['Home', 'Face Detection', 'Audio Evaluation', 'More Information']
    choice = st.sidebar.radio('Select Pages', pages)

    load_css("style.css")
    
    if choice == 'Home':
        st.subheader('Stroke Screening Made Instant, Live, and Easy')

        st.subheader('Why SSMILE?')

        statistics_text = """<div>According to CDC, In 2018,
            <span class='highlight red'>1 in every 6 deaths</span>
            from cardiovascular disease was due to stroke. Someone in the United States has a stroke
            <span class='bold'> every 40 seconds</span>. Stroke is a <span class='highlight yellow'> leading cause </span> of serious long-term disability.</span>
            </div>"""

        st.markdown(statistics_text, unsafe_allow_html=True)

        st.write("--")

        info_text = """<div>With more than
            <span class='highlight red'>fifteen million</span>
            cases of <span class='bold'>stroke</span> worldwide every year and many more 
            complications arising from stroke,</span>
            <span class='highlight yellow'> early detection of stroke is significant 
            to prevent any further brain damage and to possibly decrease both mortality and morbidity.</span></span>
            </div>"""

        st.markdown(info_text, unsafe_allow_html=True)
        st.markdown("""👉 This web application helps one determine whether one has facial droop and speech problems
        so that one can act FAST to """)

        st.write("--")

        #st.caption('According to CDC,')
        #st.checkbox('In 2018, 1 in every 6 deaths from cardiovascular disease was due to stroke.')
        #st.checkbox('Someone in the United States has a stroke every 40 seconds.')
        #st.checkbox('Stroke is a leading cause of serious long-term disability.')
        #st.checkbox('Stroke reduces mobility in more than half of stroke survivors age 65 and over.')

        st.markdown('More information can be found:')

        github = 'https://github.com/zoekimm/SSMILE'
        devpost = 'https://devpost.com/software/ssmile'
        st.markdown("[Github repository](%s)" % github)
        st.markdown("[DevPost](%s)" % devpost)



        st.write("--")

    elif choice == 'Face Detection':
        run_face_detection()

    elif choice == 'Audio Evaluation':
        run_audio_evaluation()

    elif choice == 'More Information':
        pass

if __name__ == '__main__':
    main()

