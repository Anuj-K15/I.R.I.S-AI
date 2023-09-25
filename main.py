import speech_recognition as sr
import os
import win32com.client
from speech_recognition import Recognizer

#speaker = win32com.client.Dispatch("SAPI.SpVoice")

# s = 1
# while (s == 1):
#
#     s = "Hello I am JARVIS AI"
#     print(s)
#     speaker.Speak(s)
def say(text):
    os.system(f"say{text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-in")
        print(f"user Said: {query}")
        return query
if __name__ == '__main__':
    print('PyCharm')
    say('Hello i am Jarvis A.I')
    print("Listening...")
    text = takeCommand()
    say(text)







