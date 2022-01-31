import speech_recognition as sr
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
  
r = sr.Recognizer() 
audio_file = sr.AudioFile('output.wav')

with audio_file as source: 
    r.adjust_for_ambient_noise(source) 
    audio = r.record(source)

r.recognize_google(audio)
