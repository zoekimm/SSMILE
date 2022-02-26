import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
from voicetest import similar
from voicetest import evaluate_audio

def check_file_type(audio_file):
    if audio_file.name[-3:] == 'm4a':
        track = AudioSegment.from_file(audio_file,  format= 'm4a')
        file_handle = track.export(audio_file.name[:-3] + '.wav', format='wav')
        audio_file = file_handle
    
    return audio_file

def run_audio_evaluation():
    st.subheader('Audio Evaluation')
    st.checkbox('Upload a recording of yourself reading the following sentence aloud')

    text = 'Nice to meet you'
    st.checkbox('Sample Setence : ' + text)

    option = st.selectbox(
     'File Type',
     ('Select your option', 'Upload', 'Recording'))

    if option == 'Select your option':
        pass

    if option == 'Upload':
        audio_file = st.file_uploader('Upload Your Audio', type = ['wav', 'm4a'])
        #audio_file2 = st.file_uploader('Upload Your Second Audio', type = ['wav', 'm4a'])

        if audio_file is None:
            pass
        else:
            audio_file = check_file_type(audio_file)
            spoken_text = evaluate_audio(audio_file)
            ratio = similar(spoken_text, text.lower())
            st.success(ratio)
            
            #audio_bytes = audio_file.read()
            #st.audio(audio_bytes, format='audio/ogg')

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


