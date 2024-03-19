Intro = '''
Application Name:- Jarvis
Developer Name:- RISHABH-SAHIL 
'''

# ----------------------Modules Name----------------------
# pip install googletrans==3.1.0a0
# pip install speechrecognition

import speech_recognition as sr 
from googletrans import Translator

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")
    except:
        return ""

    query = str(query).lower()
    return query

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You:- {data}")
    return data

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

def WakeupDetected():
    query = MicExecution()

    if "wake up" in query or "get up" in query:
        print("Hiiii")

    else:
        pass

while True:
    WakeupDetected()     
    