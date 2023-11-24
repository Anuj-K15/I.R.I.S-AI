import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import pywhatkit
import pyautogui
import pyjokes
import pygame
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wakeupcommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I.R.I.S is Sleeping..")
        r.pause_threshold = 0.6
        r.adjust_for_ambient_noise(source, duration=0.6 )
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")
    except Exception as e:
        query = 'none'
    return query
    
def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        r.adjust_for_ambient_noise(source, duration=0.6 )
        audio = r.listen(source)
        
    try:
        print("Wait for Few Moments...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")
    except Exception as e:
        print(e)
        speak("Please Tell me again")
        query = 'None'
    return query

def wishings():
    hour = int (datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print ("Good Morning BOSS")
        speak("Good Morning BOSS")
    elif hour >= 12 and hour < 17:
        print ("Good Afternoon Boss")
        speak("Good Afternoon Boss")
    elif hour >= 17 and hour < 21:
        print ("Good Evening Boss")
        speak("Good Evening BOSS")
    else:
        print ("Good Night BOSS")
        speak("Good Night BOSS")
        
def play_music(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        pygame.mixer.music.pause()
        while pygame.mixer.music.get_busy():
            pygame.time.delay(100)
    except pygame.error:
        print("Error: Could not load or play the music file.")

if __name__ == "__main__":
    
    while True:
        query = wakeupcommands().lower()
        if 'wake up' in query:
            wishings()
            speak('Yes Boss what can I do for you.')
            
        while True:
            query = commands().lower()
            
            sites = [["Youtube", "https://www.youtube.com"],
                    ["Wikipedia", "https://www.wikipedia.com"],
                    ["Google", "https://www.google.com"],
                    ["Instagram", "https://www.instagram.com"],
                    ["Facebook", "https://www.Facebook.com"],
                    ["Amazon", "https://www.amazon.in"],
                    ["GPT", "https://chat.openai.com"],
                    ["Twitter", "https://www.twitter.com"],
                    ["Microsoft", "https://www.microsoft.com"], ]
            
            songs = [["Helen", "D:\\Chhatrapati Samrajya\\Audio\\Bloody Mary - Lady Gaga_128-(DJMaza).mp3"]]

            apps = [["Adobe Premiere Pro", "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2023\\Adobe Premiere Pro.exe"],
                    ["Microsoft Word", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"],
                    ["Google Chrome", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"],
                    ["Brave", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"],
                    ["Anaconda", "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda "
                                "Navigator.lnk"],]
            
            for site in sites:
                if f"Open {site[0]}".lower() in query.lower():
                    webbrowser.open(site[1])
                    speak(f"Opening {site[0]} Sir...")

            for song in songs:
                if f"Play {song[0]} Song".lower() in query.lower():
                    musicPath = song[1]
                    os.startfile(musicPath)
                    play_music(musicPath)
                    speak(f"Playing {song[0]} Sir...")
                    
            for app in apps:
                if f"Open {app[0]}".lower() in query.lower():
                    appPath = app[1]
                    os.startfile(appPath)
                    speak(f"Opening {app[0]} Sir...")
            
            if 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print (strTime)
                speak(f"Sir the Time is {strTime}")
                
            elif 'open brave' in query:
                speak("Opening Brave Sir...")
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk")
                while True:
                    bravequery = commands().lower()
                    if 'search' in bravequery:
                        youtubequery=bravequery
                        youtubequery=youtubequery.replace('search',"")
                        pyautogui.write(youtubequery)
                        pyautogui.press('Enter')
                        speak("Searching...")
                        
                    elif 'close brave' in bravequery or 'exit chrome' in bravequery:
                        pyautogui.hotkey('ctrl','w')
                        speak("Closing Brave Sir..")
                        break
                                            
                
            elif 'search' in query:
                speak("Searching in Wikipedia")
                print("Searching in Wikipedia")
                try:
                    query = query.replace("wikipedia","")
                    results = wikipedia.summary(query, sentences = 2)
                    speak("According to Wikipedia, ")
                    print(results)
                    speak(results)
                except:
                    print("No Results Found.")
                    speak("No Results Found.")
                    
            elif 'play' in query:
                query = query.replace('play' , '')
                speak("Playing" + query)
                pywhatkit.playonyt(query)
                        
            elif 'joke' in query:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)
                
            elif 'sleep' in query:
                speak("I'm Leaving Sir, BYE!")
                quit()
            
            elif 'what can you do for me' in query:
                speak('Yes Sir, Nice question')
                speak("As per my program, I am a bot which can perform task using your voice commands")
                
            elif 'cool' in query or 'nice' in query or 'awesome' in query or 'thank you' in query:
                speak("That's my Pleasure! Sir")
                
            elif 'minimize' in query or 'minimise' in query:
                speak('Minimizing Sir..')
                pyautogui.hotkey('win','down','down')
                
            elif 'maximize' in query or 'maximise' in query:
                speak('Maximizing Sir..')
                pyautogui.hotkey('win','up','up')
                
            elif 'close the application' in query or 'close the window' in query:
                speak('Closing Sir..')
                pyautogui.hotkey('ctrl','w')
                
            elif 'screenshot' in query:
                speak('Taking Screenshot Sir..')
                pyautogui.hotkey('prtsc')
                
            elif 'paste' in query:
                pyautogui.hotkey('ctrl','v')
                speak('Done Sir..')
                
            elif 'open notepad' in query:
                speak('Opening Notepad Application Sir..')
                os.startfile("C:\\Windows\\System32\\notepad.exe")
                while True:
                    notepadquery = commands().lower()
                    notepadsavingquery = commands().lower()
                    if 'paste' in notepadquery:
                        pyautogui.hotkey('ctrl','v')
                        speak('Done Sir..')
                        
                    elif 'save this file' in notepadquery:
                        pyautogui.hotkey('ctrl','s')
                        speak('Sir, Please Specify a name for the file')
                        notepadsavingquery=commands()
                        pyautogui.write(notepadsavingquery)
                        pyautogui.press('enter')
                        
                    elif 'type' in notepadquery:
                        speak('Please tell me what should I write')
                        while True:
                            writeInNotepad = commands()
                            if writeInNotepad == 'exit typing':
                                speak('Done Sir')
                            else:
                                pyautogui.write(writeInNotepad)
                            
                    elif 'exit notepad' in notepadquery or 'close notepad' in notepadquery:
                        speak('Exiting Notepad Sir..')
                        pyautogui.hotkey('ctrl','w')
                        break
