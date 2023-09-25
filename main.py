import speech_recognition as sr
import os
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

s = 1
p = 1
c = 1

while (s == 1) & (p == 1) & (c == 1):

    s = "Hello I am JARVIS AI"
    p = "Hey! Master"
    c = "Ask me Something"
    print(s)
    speaker.Speak(s)
    print(p)
    speaker.Speak(p)
    print(c)
    speaker.Speak(c)

    def say(text):
        os.system(f"say{text}")
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Sorry, there was an error connecting to the Google API: {e}")
            return ""


    if __name__ == '__main__':
        while True:
            print("Listening..")
            text = takeCommand()
           

