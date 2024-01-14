import speech_recognition as sr
import pyttsx3

import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

import openai
openai.api_key = OPENAI_KEY

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()
def divider():
    print("="*50)
def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                # print("I'm Listening")
                print("ChatGPT : " + "I'm Listening")
                # divider()
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                print("Myself  : " + MyText)
                return MyText
            
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            # print("Unknown error occured")
            divider()
        # divider()


def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens = 100,
        n = 1,
        stop = None,
        temperature=0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

# messages = [{"role": "user", "content": "Please act like Jarvis from Iron Man."}]
messages = []
while(1):
    text = record_text()
    messages.append({"role": "user", "content": text})
    response = send_to_chatGPT(messages)
    SpeakText(response)
    print("ChatGPT : " + response)
    divider()