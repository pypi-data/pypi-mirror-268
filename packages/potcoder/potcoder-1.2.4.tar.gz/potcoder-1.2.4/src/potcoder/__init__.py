# Welcome to Potcoder, a module created for the Python language that makes programming easier for programmers and developers
# PotCoder will need additional additional modules, details can be found at https://github.com/hiactions/potcoder/

import os
# import openai [Uncomment if you want to use PyGPT (potcode.pygpt)]
# import platform (Comment with openai module)
import subprocess
import wget
import sys
from pytube import YouTube
from dotenv import load_dotenv

load_dotenv()

# Get the value of the environment variable "POTCODER-VERSION"
potcoder_version = os.getenv("POTCODER-VERSION")

# Welcome message
if potcoder_version is not None:
    print(f"Welcome to PotCoder [v{potcoder_version}]")

# Converts strings to binary code [Usage: potcoder.conv_str_bin("[Question when running Python code]")]
def conv_str_bin(machine_question):
    user_input = input(machine_question)
    binary_result = ''.join(format(ord(char), '08b') for char in user_input)

    print("Binary Code: " + binary_result)

# potcoder CLI [Usage: potcoder.cli()]
def cli():
    while True:
        usr_cmd = input(f"potcoder-{potcoder_version}> ")

        if usr_cmd is None:
            pass
        if "hi" in usr_cmd or "hello" in usr_cmd:
            print(f"potcoder-{potcoder_version}  [RETURN] >> Thank you :)")
        elif "bye" in usr_cmd:
            print(f"potcoder-{potcoder_version}  [RETURN] >> Good bye! :(")
            break
        elif usr_cmd == "info":
            print(f"potcoder-{potcoder_version}  [RETURN] >> potcoder [v{potcoder_version}]. Made by Thai Minh Nguyen (@hiactions)")
        elif usr_cmd == "help":
            print("============================================================")
            print(f"|                   PotCoder CLI V{potcoder_version}                    |")
            print("============================================================")
            print("\nCommands:")
            print("info                  See information about PotCoder CLI")
            print("help                  View available commands in PotCoder")
            print("check-ver             Check and update PotCoder version")
            print("exit                  Exit PotCoder CLI")
        elif usr_cmd == "check-ver":
            ver_file_url = 'https://raw.githubusercontent.com/hiactions/potcoder/main/src/potcoder/potcoder-ver.txt'
            release_whl_version = f'https://github.com/hiactions/potcoder/releases/download/v{potcoder_version}/potcoder-{potcoder_version}-py3-none-any.whl'

            try:
                wget.download(ver_file_url, 'potcoder-ver.txt')
            except Exception as e:
                print(f"Error downloading the file: {e}")
                exit(1)

            with open("potcoder-ver.txt", "r") as file:
                data = file.read().strip()  # Remove newline character

            if data == potcoder_version:
                print(f"\nYou are using the latest version of potcoder [v{potcoder_version}]")
            else:
                print(f"\nInstalling new potcoder version [v{data}]")
                wget.download(release_whl_version, f'potcoder-{data}-py3-none-any.whl')
                subprocess.run(["pip", "install", f"potcoder-{data}-py3-none-any.whl"], check=True)
        else:
            print(f"potcoder-{potcoder_version}  [RETURN] >> I don't understand what you are asking me to do :)?")

# ChatGPT built with Python [Usage: potcoder.pygpt([Your API Key], [Model ID], [Machine Question])] (Note: Uncomment if you want to use PyGPT)
# def pygpt(openai_api_key, openai_model_id, machine_question):
#     openai.api_key = openai_api_key
#     MODEL_ID = openai_model_id

#     def PyGPT_conversation(conversation):
#         response = openai.ChatCompletion.create(
#             model=MODEL_ID,
#             messages=conversation
#         )
#         conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
#         return conversation

#     conversation = []
#     conversation.append({'role': 'system', 'content': 'How may I help you?'})
#     conversation = PyGPT_conversation(conversation)
#     print(f"{machine_question}: {conversation[-1]['content'].strip()}\n")

#     while True:
#         prompt = input(machine_question)
#         if prompt == "gptFoundation()":
#             print("Foundation: Python v" + platform.python_version() + " with " + MODEL_ID)
#         else:
#             conversation.append({'role': 'user', 'content': prompt})
#             conversation = PyGPT_conversation(conversation)
#             print(f"{machine_question} {conversation[-1]['content'].strip()}\n")


# Python Runtime Environment Checker (IDLE or CLI) [Usage: potcoder.pyenv_detect()] (Note: When you use potcoder.pyenv_detect() function, the result will be returned to one of two values: "IDLE" or "CLI")
def pyenv_detect():
    if 'idlelib' in sys.modules:
        return "IDLE"
    else:
        return "CLI"
    
# Download high quality Youtube videos [Usage: potcode.ytdl([Youtube video link], [Successful download message], [Error download message])]
def ytdl(machine_question, success_msg, err_msg):
    yt_link = input(machine_question)
    youtubeObject = YouTube(yt_link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        print(success_msg)
    except:
        print(err_msg)

    

