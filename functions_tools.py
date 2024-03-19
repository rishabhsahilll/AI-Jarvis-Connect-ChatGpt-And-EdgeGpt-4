import os
from googletrans import Translator

def remove_fils(folder_path, file_extension='.mp3', not_remove_this_filse_name='.mp3'):
    # get a list of all files in the folder
    files = os.listdir(folder_path)

    # loop through the files
    for file_name in files:
        # check if the file is an MP3 file
        if file_name.endswith(file_extension) and file_name != not_remove_this_filse_name:
            # build the full file path
            file_path = os.path.join(folder_path, file_name)
            # remove the file
            os.remove(file_path)
            # print(f"\nRemoved file: {file_path}\n")

# create a translator object
translator = Translator()

# # set the text to be translated
# text = 'Hello, this is a test of Google Translate in Hindi.'

def translate_into(text,lang='en'):

    # translate the text to Hindi
    translation = translator.translate(text, dest=lang)

    # print the translated text
    return str(f"{translation.text}")

# print(translate_into(text,lang='hi'))