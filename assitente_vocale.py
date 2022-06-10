from pyttsx3 import init
import speech_recognition as sr

engine = init()
engine.say("ciao ciao! come ti chiami?")
engine.runAndWait()

r=sr.Recognizer()
parole = None
with sr.Microphone() as source:
    print("Pronto ad ascoltare...")
    try:
        audio = r.listen(source)
        parole = r.recognize_google(audio, language="it-IT").lower()
    except sr.UnknownValueError:
        print("non hai detto niente")
        engine.say("non hai detto niente")
    
    
if(parole is not None):
    print("ciao "+parole+" piacere di conoscerti")
    engine.say("ciao "+parole+" piacere di conoscerti")
engine.runAndWait()
