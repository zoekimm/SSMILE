import speech_recognition as sr
  
r = sr.Recognizer() 
#audio_file

with audio_file as s: 
    r.adjust_for_ambient_noise(s) 
    audio = r.record(s)
    