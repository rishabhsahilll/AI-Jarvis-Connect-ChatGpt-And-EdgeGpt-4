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

#  Bing + GptBot Code Start's 
import asyncio
import asyncio, json
from EdgeGPT import Chatbot, ConversationStyle

import t_spk
import os
import emojis_remover
import functions_tools

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

if __name__ == "__main__":
    while True:
        query = input("Human:- ")
        if "bye" == query or "exit" == query:
            query = query.replace(query, "bye")
            replay = str(asyncio.run(main(query=query)))
            text_without_emojis = emojis_remover.remove_emojis(replay)
            not_remove_file = t_spk.AI_Speak(text=text_without_emojis,with_emojis=replay)
            functions_tools.remove_fils(folder_path=".\\Speak-Mp3-Data\\", file_extension='.mp3', not_remove_this_filse_name=not_remove_file)
            exit()
        else:
            replay = str(asyncio.run(main(query=query)))
            text_without_emojis = emojis_remover.remove_emojis(replay)
            not_remove_file = t_spk.AI_Speak(text=text_without_emojis,with_emojis=replay)
            functions_tools.remove_fils(folder_path=".\\Speak-Mp3-Data\\", file_extension='.mp3', not_remove_this_filse_name=not_remove_file)
            
