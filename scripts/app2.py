import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write

def run_audio_evaluation():
    st.subheader('Audio Evaluation')
    st.checkbox('Upload a recording of yourself reading the following sentence aloud')
    st.checkbox('Sample Setence : Nice to meet you. What is your name?')
    option = st.selectbox(
     'File Type',
     ('Select your option', 'Upload', 'Recording'))

    if option == 'Select your option':
        pass

    if option == 'Upload':
        audio_file = st.file_uploader('Upload Your Audio', type = ['wav', 'mp3'])

        if audio_file is None:
            pass
        else:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/ogg')

    if option == 'Recording':
        if st.button("Start Recording"):
            fs = 44100
            duration = 10.5
            st.success("recording...............")

            #channel error
            recording_file = sd.rec(int(duration * fs), samplerate = fs, channels = 2)
            sd.wait()       
            write("sound.wav",fs , recording_file)

    return 


