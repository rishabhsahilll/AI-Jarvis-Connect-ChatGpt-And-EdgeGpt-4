Intro = '''
Application Name:- Jarvis
Developer Name:- RISHABH-SAHIL 
'''

# ----------------------Modules Name----------------------
# Windows Based pip install pyttsx3
# Chrome Based pip install selenium==4.1.3

# ----------------------Windows Based----------------------

import pyttsx3

def AI_Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 170)
    print("")
    print(f"You:- {Text}")
    print("")
    engine.say(Text)
    engine.runAndWait()

# ----------------------Chrome Based----------------------

# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep

# chrome_options = Options()
# chrome_options.add_argument('--log-level=3')
# chrome_options.headless = True
# Path = "DataBase\chromedriver.exe"
# driver = webdriver.Chrome(Path,options=chrome_options)
# driver.maximize_window()

# website = r"https://ttsmp3.com/text-to-speech/British%20English/"
# driver.get(website)
# ButtonSelaction = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
# ButtonSelaction.select_by_visible_text('British English / Brian')
# # ButtonSelaction.select_by_visible_text('Indian English / Raveena')

# def AI_Speak(Text):
#     lengthtext = len(str(Text))

#     if lengthtext==0:
#         pass

#     else:
#         print("")
#         print(f"Jarvis:- {Text}")
#         print("")
#         Data = str(Text)
#         Xpathodsec = '/html/body/div[4]/div[2]/form/textarea'
#         driver.find_element(By.XPATH,value=Xpathodsec).send_keys(Data)
#         driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

#         if lengthtext>=30:
#             sleep(4)
        
#         elif lengthtext>=40:
#             sleep(6)

#         elif lengthtext>=55:
#             sleep(8)

#         elif lengthtext>=70:
#             sleep(10)

#         elif lengthtext>=100:
#             sleep(13)

#         elif lengthtext>=120:
#             sleep(14)

#         else:
#             sleep(2)

# while True:
#     aa=input(">> ")
#     AI_Speak(aa)
