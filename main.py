import webbrowser

import speech_recognition as sr
import os
import win32com.client
import openai

speaker = win32com.client.Dispatch("SAPI.SpVoice")

s = 1
c = 1

while (s == 1) & (c == 1):

    s = "Hello I am JARVIS AI"
    c = "Ask me Something"
    print(s)
    speaker.Speak(s)
    print(c)
    speaker.Speak(c)


    def say(text):
        os.system(f"say{text}")


    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.6
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            speaker.speak(query)
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Sorry, there was an error connecting to the Google API: {e}")
            return ""


    if __name__ == '__main__':
        while True:
            query = takeCommand()
            sites = [["Youtube", "https://www.youtube.com"],
                     ["Wikipedia", "https://www.wikipedia.com"],
                     ["Google", "https://www.google.com"],
                     ["Instagram", "https://www.instagram.com"],
                     ["Facebook", "https://www.Facebook.com"],
                     ["Amazon", "https://www.amazon.in"],
                     ["Chat G P T", "https://chat.openai.com"],
                     ["Twitter", "https://www.twitter.com"], ]
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():

                    webbrowser.open(site[1])
                    speaker.speak(f"Opening {site[0]} Sir...")
