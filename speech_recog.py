import speech_recognition as sr
r = sr.Recognizer()
FILE=("SR.wav")

with sr.AudioFile(FILE) as source: 
#with sr.Microphone() as source:
    #print("Please speak")
    #reads the audio file. Here we use record instead of 
    #listen 
    audio = r.record(source)   

try:
    speech=r.recognize_google(audio);
    print("The audio file contains: {}".format(speech)) 
  
except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio")
