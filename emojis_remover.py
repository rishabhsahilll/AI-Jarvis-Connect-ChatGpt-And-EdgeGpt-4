import re

def remove_emojis(text):
    # define the regex pattern for emojis
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    # remove the emojis from the text
    return emoji_pattern.sub(r'', text)

# # Example Usage First Case With Emojis
# text_with_emojis = "Hello! 😊 How are you? 🙌"
# text_without_emojis = remove_emojis(text_with_emojis)
# print(text_without_emojis+"\n\n")  # prints "Hello!  How are you? "

# # Example Usage Second Case Without Emojis
# text_with_emojis = "Hello! How are you?"
# text_without_emojis = remove_emojis(text_with_emojis)
# print(text_without_emojis+"\n\n")  # prints "Hello!  How are you? "
