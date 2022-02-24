import streamlit as st

def run_audio_evaluation():
    st.title('Audio Evaluation')

    audio_file = st.file_uploader('Upload Your Audio', type = ['wav', 'mp3'])

    if audio_file is None:
        pass
    else:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/ogg')