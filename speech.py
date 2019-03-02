import speech_recognition as sr
r=sr.Recognizer()
print ("Kindly Speak!!")
with sr.Microphone()as source:
    audio=r.listen(source)
try:
    print("The System predicts the following:\n"+r.recognize_google(audio))
except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
