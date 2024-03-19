Intro = '''
Application Name:- Jarvis
AI Powered Bot:- 'Bing + ChatGpt' A.I
Developer Name:- RISHABH-SAHIL 
Version:- DEV 0.25.09\n\n
'''

# Start Intro
import pyfiglet # pip install pyfiglet
from rich.console import Console
con = Console()

banner = pyfiglet.figlet_format("JARVIS",font="banner3-D")
con.print(banner,style="green")
# then printing that out with rich console and a little intro
con.print(Intro,style="bold green")

# New Speak Function 
import t_spk 
import os
import emojis_remover
import functions_tools

def AI_Speak(text,lang='en'):
    # if "en"==lang:
    #     print(f'English Jarvis:- {text}')
    # else:
    #     print(f'Hindi Jarvis:- {text}')
    text_without_emojis = emojis_remover.remove_emojis(text)
    not_remove_file = t_spk.AI_Speak(text=text_without_emojis,with_emojis=text,lang=lang)
    functions_tools.remove_fils(folder_path=".\\Speak-Mp3-Data\\", file_extension='.mp3', not_remove_this_filse_name=not_remove_file)


# print(">> Starting The Jarvis : Wait For Some Seconds...")
# from Body.Speak import AI_Speak
AI_Speak("Starting The Jarvis : Wait For Some Seconds...")
from Body.Listen import MicExecution
from Brain.AIBrain import ReplyBrain, Bing_Chat_Bot
from Brain.Qna import Questions_Ans
from Features.Clap import Tester
from Features.Open import OpenExe_English, OpenExe_Hindi
import wikipedia # pip install wikipedia
import webbrowser
import datetime
from time import sleep
# import Whatsapp 


#  Bing + GptBot Code Start's 
import asyncio
from EdgeGPT import Chatbot, ConversationStyle
sleep(6)
AI_Speak("Starting The Jarvis : Wait For Few Seconds More...")
sleep(3)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return "Good Morning Sir"
    elif hour>=12 and hour<18:
        return "Good Afternoon Sir"
    else:
        return "Good Evening Sir"


async def main(query):
    bot = Chatbot(cookiePath='./cookies.json')
    data = await bot.ask(prompt=str(query), conversation_style=ConversationStyle.creative)
    await bot.close()

    # print(data)
    # print("\n\n\n")
    
    replay_002 = str(data['item']['messages'][1]['text'])
    BingGpt = "'Bing + ChatGpt' A.I Powered Bot Created By ~~RISHABH-SAHIL~~"
    # print(f"Jarvis:- {replay_002}")
    return str(replay_002)
    # print(f"Jarvis:- {replay_002} \n {BingGpt}")
    # print("\n\n")

'''============================================================ENGLISH---JARVIS================================================================'''

def English_Jarvis():

    AI_Speak(str(wishMe()))
    sleep(2)
    AI_Speak("I'm Jarvis, I'm Ready To Assist You Sir.")

    while True:
        Data = MicExecution()
        Data = str(Data).lower()
        ReplyData = OpenExe_English(Data)
        if Data==True:
            Reply = ReplyBrain(Data)
            AI_Speak(Reply)

        # if "whatsapp" in Data:
        #     Namen = str(Data).replace("send ","")
        #     Namen = str(Namen).replace("whatsapp ","")
        #     Namen = str(Namen).replace("message ","")
        #     Namen = str(Namen).replace("to ","")
        #     Whatsapp.WhatsappSender(Namen)
        #     pass

        if len(Data)<3:
            pass

        elif "turn on the tv" in Data:
            AI_Speak("Ok... But Where is Your T.V")

        elif "what is " in Data or "What is" in Data or "question" in Data or "answer" in Data or "why" in Data or "how" in Data:
            Reply = Questions_Ans(Data)
            AI_Speak(Reply)

        elif 'the time' in Data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            AI_Speak(f"Sir, the time is {strTime}")

        elif 'wikipedia' in Data:
            AI_Speak('Searching Wikipedia...please wait')
            Data = Data.replace("wikipedia", "")
            results =  wikipedia.summary(Data, sentences = 2)
            AI_Speak("wikipedia says")
            AI_Speak(results)

        elif 'talk to bing' in Data or "start bing" in Data or "start the bing" in Data or 'talk to edge' in Data or "start edge" in Data or "start the edge" in Data or "code 1234" in Data:
            AI_Speak("Okey Sir")
            AI_Speak("Starting The AI Bing : Wait For Some Seconds...")
            Reply = Bing_Chat_Bot("Hello")
            AI_Speak("Starting The AI Bing : Wait For Few Seconds More...")
            sleep(2)
            AI_Speak(Reply)
            stop = True
            while stop:
                Data = MicExecution()
                Data = str(Data).lower()
                ReplyData = OpenExe_English(Data)

                if Data==True:
                    Reply = ReplyBrain(Data)
                    AI_Speak(Reply)

                if len(Data)<3:
                    pass

                elif 'talk in hindi' in Data or "code 2468" in Data or 'speak in hindi' in Data:
                    AI_Speak("ठीक है सर!")
                    Hindi_Jarvis()

                else:
                    AI_Speak("Sir, A.I Bing gives very slow response so have to wait")
                    Reply = Bing_Chat_Bot(Data)
                    AI_Speak(Reply)

        elif 'talk in hindi' in Data or "code 2468" in Data:
            AI_Speak("ठीक है सर!",lang="hi")
            Hindi_Jarvis()


        # else:   
            # if 'wikipedia' in Data:
            #     AI_Speak('Searching Wikipedia...please wait')
            #     Data = Data.replace("wikipedia", "")
            #     results =  wikipedia.summary(Data, sentences = 2)
            #     AI_Speak("wikipedia says")
            #     AI_Speak(results)
            # else:
            #     Reply = ReplyBrain(Data)
            #     AI_Speak(Reply)
            #     if "bye" in Reply:
            #         ClapDetect()
            
        else:
            Reply = ReplyBrain(Data)
            AI_Speak(Reply)

        # else:
        #     Reply = Bing_Chat_Bot(Data)
        #     AI_Speak(Reply)

'''============================================================HINDI---JARVIS================================================================'''

def Hindi_Jarvis():

    AI_Speak(functions_tools.translate_into(text=str(wishMe()),lang='hi'),lang='hi')
    AI_Speak(functions_tools.translate_into(text="I'm Jarvis, I'm Ready To Assist You Sir.",lang='hi'),lang='hi')

    while True:
        Data = MicExecution()
        Data = str(Data).lower()
        ReplyData = OpenExe_Hindi(Data)
        if Data==True:
            Reply = ReplyBrain(Data)
            AI_Speak(functions_tools.translate_into(text=Reply,lang='hi'),lang='hi')

        # if "whatsapp" in Data:
        #     Namen = str(Data).replace("send ","")
        #     Namen = str(Namen).replace("whatsapp ","")
        #     Namen = str(Namen).replace("message ","")
        #     Namen = str(Namen).replace("to ","")
        #     Whatsapp.WhatsappSender(Namen)
        #     pass

        if len(Data)<3:
            pass

        elif "what is " in Data or "What is" in Data or "question" in Data or "answer" in Data or "why" in Data or "how" in Data:
            Reply = Questions_Ans(Data)
            AI_Speak(functions_tools.translate_into(text=Reply,lang='hi'),lang='hi')

        elif 'the time' in Data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            AI_Speak(functions_tools.translate_into(text=f"Sir, the time is {strTime}",lang='hi'),lang='hi')

        elif 'wikipedia' in Data:
            AI_Speak(functions_tools.translate_into(text='Searching Wikipedia...please wait',lang='hi'),lang='hi')
            Data = Data.replace("wikipedia", "")
            results =  wikipedia.summary(Data, sentences = 2)
            AI_Speak("wikipedia says")
            AI_Speak(functions_tools.translate_into(text=results,lang='hi'),lang='hi')

        elif 'talk to bing' in Data or "start bing" in Data or "start the bing" in Data or 'talk to edge' in Data or "start edge" in Data or "start the edge" in Data or "code 1234" in Data:
            AI_Speak("Okey Sir")
            AI_Speak(functions_tools.translate_into(text="Starting The AI Bing : Wait For Some Seconds...",lang='hi'),lang='hi')
            Reply = Bing_Chat_Bot("Hello")
            AI_Speak(functions_tools.translate_into(text="Starting The AI Bing : Wait For Few Seconds More...",lang='hi'),lang='hi')
            sleep(2)
            AI_Speak(functions_tools.translate_into(text=Reply,lang='hi'),lang='hi')
            stop = True
            while stop:
                Data = MicExecution()
                Data = str(Data).lower()
                ReplyData = OpenExe_Hindi(Data)

                if Data==True:
                    Reply = ReplyBrain(Data)
                    AI_Speak(functions_tools.translate_into(text=Reply,lang='hi'),lang='hi')

                if len(Data)<3:
                    pass

                elif 'talk to jarvis' in Data or "start jarvis" in Data or "start the jarvis" in Data or "code 1234" in Data:
                    AI_Speak("ठीक है सर!")
                    sleep(2)
                    AI_Speak(functions_tools.translate_into(text="I'm Jarvis, I'm Ready To Assist You Sir.",lang='hi'),lang='hi')
                    stop = False

                elif 'talk english' in Data or "code 2468" in Data or 'speak in english' in Data:
                    AI_Speak("Okey Sir!")
                    sleep(2)
                    AI_Speak("I'm Jarvis, I'm Ready To Assist You Sir.")
                    Hindi_Jarvis()

                else:
                    AI_Speak(functions_tools.translate_into(text="Sir, A.I Bing gives very slow response so have to wait",lang='hi'),lang='hi')
                    Reply = Bing_Chat_Bot(Data)
                    AI_Speak(functions_tools.translate_into(text=Reply,lang='hi'),lang='hi')

        # else:   
            # if 'wikipedia' in Data:
            #     AI_Speak('Searching Wikipedia...please wait')
            #     Data = Data.replace("wikipedia", "")
            #     results =  wikipedia.summary(Data, sentences = 2)
            #     AI_Speak("wikipedia says")
            #     AI_Speak(results)
            # else:
            #     Reply = ReplyBrain(Data)
            #     AI_Speak(Reply)
            #     if "bye" in Reply:
            #         ClapDetect()
            
        elif 'talk in english' in Data or "code 2468" in Data:
            AI_Speak("Okey Sir!")
            English_Jarvis()

        else:
            Reply = ReplyBrain(Data)
            AI_Speak(functions_tools.translate_into(text=Reply,lang='hi'),lang='hi')

        # else:
        #     Reply = Bing_Chat_Bot(Data)
        #     AI_Speak(Reply)


def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>>>")
        print("")
        English_Jarvis
    else:
        pass

English_Jarvis()