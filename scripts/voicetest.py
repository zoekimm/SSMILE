import speech_recognition as sr
from difflib import SequenceMatcher

def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

def evaluate_audio(file_name):
    
    r = sr.Recognizer() 
    audio_file = sr.AudioFile(file_name)

    with audio_file as source: 
        r.adjust_for_ambient_noise(source) 
        audio = r.record(source)

    return r.recognize_google(audio)
