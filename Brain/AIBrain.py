Intro = '''
Application Name:- Jarvis
Developer Name:- RISHABH-SAHIL 
'''
# Api Key

fileopen = open("Data\Api.txt","r") # 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
API = fileopen.read()
fileopen.close()

#  Bing + GptBot Code Start's 
import asyncio
from EdgeGPT import Chatbot, ConversationStyle

async def main(query):
    bot = Chatbot(cookiePath='./cookies.json')
    data = await bot.ask(prompt=str(query), conversation_style=ConversationStyle.creative)
    await bot.close()

    # print(data)
    # print("\n\n\n")
    
    replay_002 = str(data['item']['messages'][1]['text'])
    BingGpt = "'Bing + ChatGpt' A.I Powered Bot Created By ~~RISHABH-SAHIL~~"
    # print(f"Jarvis:- {replay_002}")
    replay_002 = replay_002.replace("^1^", "").replace("^2^", "").replace("^3^","").replace("^4^","").replace("^5^","").replace("^6^","").replace("^7^","").replace("^8^","").replace("^9^","").replace("^10^","").replace("[]","").replace("**", "")
    return str(replay_002)
    # print(f"Jarvis:- {replay_002} \n {BingGpt}")
    # print("\n\n")


# ----------------------Modules Name----------------------

# import openai
# from dotenv import load_dotenv

# openai.api_key = API
# load_dotenv()
# completion = openai.Completion()

# def ReplyBrain(question,chat_log=None):
#     FileLog = open("DataBase\\chat_log.txt","r")
#     chat_log_template = FileLog.read()
#     FileLog.close()

#     if chat_log is None:
#         chat_log = chat_log_template
    
#     prompt = f'{chat_log} You : {question}\nJarvis : '
#     response = completion.create(
#         model = "text-davinci-002",
#         prompt=prompt,
#         temperature = 0.5,
#         max_tokens = 60,
#         top_p = 0.3,
#         frequency_penalty = 0.5,
#         presence_penalty = 0)
#     answer = response.choices[0].text.strip()
#     # chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
#     # FileLog = open("DataBase\\chat_log.txt","w")
#     # FileLog.write(chat_log_template_update)
#     # FileLog.close()
#     return answer

def Bing_Chat_Bot(query):
    return str(asyncio.run(main(query=query)))



import google.generativeai as genai

def ReplyBrain(question):
    try:
        genai.configure(api_key=API)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        return response.text[:200]
    except:
        return "Please Try Again. Sir"

# while True:
#     query = input(">> ")
#     bot_replay = ReplyBrain(query)
#     bing_replay = asyncio.run(main(query=query))
#     if "I'm sorry but I don't understand your language" in str(bing_replay) or "I can understand and communicate fluently in Hindi" in str(bing_replay) or "I'm sorry but I don't understand your message." in str(bing_replay):
#         print(f"Bot:- {bot_replay}")
#     else:
#         print(f"Bing:- {bing_replay}")