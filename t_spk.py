from gtts import gTTS
import os
from time import sleep
import random
import pygame

# initialize pygame
pygame.init()

# function to convert text to speech
def AI_Speak(text, with_emojis="🥲", lang='en'):
    print(with_emojis)

    # use the Google Text-to-Speech API to generate the speech
    tts = gTTS(text=text, lang=lang)

    # save the random number as an mp3 file
    rand_num1 = (random.randint(1, 100))
    rand_num2 = (random.randint(20, 40))
    rand_num3 = (random.randint(60, 80))
    rand_num = int(rand_num1)+int(rand_num2)+int(rand_num3)
    tts.save(f'Speak-Mp3-Data\\{rand_num}.mp3')
    
    # play the mp3 file
    pygame.mixer.music.load(f'Speak-Mp3-Data\\{rand_num}.mp3')

    # play the audio file
    pygame.mixer.music.play()

    return f"{rand_num}.mp3"

# AI_Speak("Hello, I am Rishabh kumar")


from pydub import AudioSegment
from pydub.playback import play

def AI_Speak(text, with_emojis="🥲", lang='en'):
    if "en"==lang:
        print(f'English Jarvis:- {with_emojis}')
    else:
        print(f'Hindi Jarvis:- {with_emojis}')

    # use the Google Text-to-Speech API to generate the speech
    tts = gTTS(text=text, lang=lang)

    # save the random number as an mp3 file
    rand_num = (random.randint(1, 100))
    tts.save(f'Speak-Mp3-Data\\{rand_num}.mp3')

    # load the mp3 file
    pygame.mixer.music.load(f'Speak-Mp3-Data\\{rand_num}.mp3')
    pygame.mixer.music.play()
    stop_speak = True
    while pygame.mixer.music.get_busy() == stop_speak:
        # query = input(">> ")
        # if "q" in query:
        #     stop_speak = False
        # else:
        continue

    return f"{rand_num}.mp3"
