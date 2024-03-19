import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
from Body.Speak import AI_Speak
from Body.Listen import MicExecution
from Brain.AIBrain import Bing_Chat_Bot

# New Speak Function 
import t_spk 
import os
import emojis_remover
import functions_tools

def AI_Speak(text,lang='en'):
    text_without_emojis = emojis_remover.remove_emojis(text)
    not_remove_file = t_spk.AI_Speak(text=text_without_emojis,with_emojis=text,lang=lang)
    functions_tools.remove_fils(folder_path=".\\Speak-Mp3-Data\\", file_extension='.mp3', not_remove_this_filse_name=not_remove_file)



'''============================================================ENGLISH---JARVIS================================================================'''

def OpenExe_English(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif'open youtube' in Query:
        webbrowser.open("youtube.com")
        return True

    elif 'open rishabh' in Query:
        webbrowser.open('https://www.rishabhsahil.ml/')
        return True

    elif 'open bing' in Query:
        webbrowser.open('https://www.bing.com/')
        return True

    elif 'open google' in Query:
        webbrowser.open('https://www.google.co.in/')
        return True

    elif 'search on google' in Query or 'google search' in Query:
        AI_Speak("What to search sir on google?")
        stop = True
        while stop:
            Data = MicExecution()
            if len(Data)<3:
                AI_Speak("What to search sir on google?")
                pass
            else:
                results = Bing_Chat_Bot(Data)
                webbrowser.open(f"https://www.google.com/search?q={str(Data)}")
                AI_Speak(results)
                stop = False
        return True

    elif 'search on bing' in Query or 'bing search' in Query or 'search on edge' in Query or "edge search" in Query:
        AI_Speak("What to search sir on Bing?")
        stop = True
        while stop:
            Data = MicExecution()
            if len(Data)<3:
                AI_Speak("What to search sir on Bing?")
                pass
            else:
                results = Bing_Chat_Bot(Data)
                webbrowser.open(f"https://www.bing.com/search?q={str(Data)}")
                AI_Speak(results)
                stop = False
        return True

    elif 'search on rishabh' in Query or 'rishabh search' in Query:
        AI_Speak("What to search sir on Rishabh?")
        stop = True
        while stop:
            Data = MicExecution()
            if len(Data)<3:
                AI_Speak("What to search sir on Rishabh?")
                pass
            else:
                results = Bing_Chat_Bot(Data)
                webbrowser.open(f"https://www.rishabhsahil.ml/search?q={str(Data)}")
                AI_Speak(results)
                stop = False
        return True

    elif 'search on bing ' in Query or 'bing search ' in Query or 'search on edge ' in Query or "edge search " in Query:
        Data = Query.replace("search on google", "").replace("bing search", "new").replace("search on edge", "").replace("edge search", "")
        webbrowser.open(f"https://www.bing.com/search?q={str(Data)}")
        results = Bing_Chat_Bot(Data)
        AI_Speak(results)
        return True

    elif 'search on rishabh ' in Query or 'rishabh search ' in Query:
        Data = Query.replace("search on rishabh", "").replace("rishabh search", "new").replace("search on rishabh", "").replace("rishabh search", "")
        webbrowser.open(f"https://www.rishabhsahil.ml/search?q={str(Data)}")
        results = Bing_Chat_Bot(Data)
        AI_Speak(results)
        return True

    elif 'search on youtube' in Query or 'youtube search' in Query or 'search on youtube' in Query or "youtube search" in Query or "play video on" in Query or "play video on" in Query:
        AI_Speak("Which video play sir?")
        stop = True
        while stop:
            Data = MicExecution()
            if len(Data)<3:
                AI_Speak("Which video play sir?")
                pass
            else:
                webbrowser.open(f"https://www.youtube.com/results?search_query={str(Data)}")
                stop = False
            return True

    elif 'search on youtube ' in Query or 'youtube search ' in Query or 'search on youtube ' in Query or "youtube search " in Query or "play video on " in Query or " play video on" in Query:
        Data = Query.replace("search on youtube", "").replace("youtube search", "").replace("search on youtube", "").replace("youtube search", "").replace("play video on", "").replace("play video on", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={str(Data)}")
        return True

    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(2)
        keyboard.write(Nameoftheapp)
        sleep(2)
        keyboard.press('enter')
        sleep(1)  
        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("open ","")

        if "chrome" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True

'''============================================================Hindi---JARVIS================================================================'''

def OpenExe_Hindi(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif'open youtube' in Query:
        webbrowser.open("youtube.com")
        return True

    elif 'open rishabh' in Query:
        webbrowser.open('https://www.rishabhsahil.ml/')
        return True

    elif 'open bing' in Query:
        webbrowser.open('https://www.bing.com/')
        return True

    elif 'open google' in Query:
        webbrowser.open('https://www.google.co.in/')
        return True

    elif 'search on google' in Query or 'google search' in Query:
        AI_Speak(functions_tools.translate_into(text="What to search sir on google?",lang='hi'),lang='hi')
        stop = True
        while stop:
            Data = MicExecution()
            if len(Data)<3:
                AI_Speak(functions_tools.translate_into(text="What to search sir on google?",lang='hi'),lang='hi')
                pass
            else:
                results = Bing_Chat_Bot(Data)
                webbrowser.open(f"https://www.google.com/search?q={str(Data)}")
                AI_Speak(functions_tools.translate_into(text=results,lang='hi'),lang='hi')
                stop = False
        return True

    elif 'search on bing' in Query or 'bing search' in Query or 'search on edge' in Query or "edge search" in Query:
        AI_Speak(functions_tools.translate_into(text="What to search sir on Bing?",lang='hi'),lang='hi')
        stop = True
        while stop:
            Data = MicExecution()
            if len(Data)<3:
                AI_Speak("What to search sir on Bing?")
                pass
            else:
                results = Bing_Chat_Bot(Data)
                webbrowser.open(f"https://www.bing.com/search?q={str(Data)}")
                AI_Speak(functions_tools.translate_into(text=results,lang='hi'),lang='hi')
                stop = False
        return True

    elif 'search on rishabh' in Query or 'rishabh search' in Query:
        AI_Speak(functions_tools.translate_into(text="What to search sir on Rishabh?",lang='hi'),lang='hi')
        stop = True
        while stop:
            Data = MicExecution()
            if len(Data)<3:
                AI_Speak(functions_tools.translate_into(text="What to search sir on Rishabh?",lang='hi'),lang='hi')
                pass
            else:
                results = Bing_Chat_Bot(Data)
                webbrowser.open(f"https://www.rishabhsahil.ml/search?q={str(Data)}")
                AI_Speak(functions_tools.translate_into(text=results,lang='hi'),lang='hi')
                stop = False
        return True

    elif 'search on bing ' in Query or 'bing search ' in Query or 'search on edge ' in Query or "edge search " in Query:
        Data = Query.replace("search on google", "").replace("bing search", "new").replace("search on edge", "").replace("edge search", "")
        webbrowser.open(f"https://www.bing.com/search?q={str(Data)}")
        results = Bing_Chat_Bot(Data)
        AI_Speak(functions_tools.translate_into(text=results,lang='hi'),lang='hi')
        return True

    elif 'search on rishabh ' in Query or 'rishabh search ' in Query:
        Data = Query.replace("search on rishabh", "").replace("rishabh search", "new").replace("search on rishabh", "").replace("rishabh search", "")
        webbrowser.open(f"https://www.rishabhsahil.ml/search?q={str(Data)}")
        results = Bing_Chat_Bot(Data)
        AI_Speak(functions_tools.translate_into(text=results,lang='hi'),lang='hi')
        return True

    elif 'search on youtube' in Query or 'youtube search' in Query or 'search on youtube' in Query or "youtube search" in Query or "play video on" in Query or "play video on" in Query:
        AI_Speak(functions_tools.translate_into(text="Which video play sir?",lang='hi'),lang='hi')
        stop = True
        while stop:
            Data = MicExecution()
            if len(Data)<3:
                AI_Speak(functions_tools.translate_into(text="Which video play sir?",lang='hi'),lang='hi')
                pass
            else:
                webbrowser.open(f"https://www.youtube.com/results?search_query={str(Data)}")
                stop = False
            return True

    elif 'search on youtube ' in Query or 'youtube search ' in Query or 'search on youtube ' in Query or "youtube search " in Query or "play video on " in Query or " play video on" in Query:
        Data = Query.replace("search on youtube", "").replace("youtube search", "").replace("search on youtube", "").replace("youtube search", "").replace("play video on", "").replace("play video on", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={str(Data)}")
        return True

    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(2)
        keyboard.write(Nameoftheapp)
        sleep(2)
        keyboard.press('enter')
        sleep(1)  
        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("open ","")

        if "chrome" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True