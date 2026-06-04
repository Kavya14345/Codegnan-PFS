'''
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
    try:
        print("Recognizing...")
        command=recognizer.recognize_google(audio)
        print("You said:",command)
        return command.lower()
    except Exception:
        print("Sorry, Please say that again.")
        return ""
def wish_user():
    hour=datetime.datetime.now().hour
    s="I am your Virtual Assistant"
    if hour<12:
        speak(f"Good Morning {s}")
    elif hour<18:
        speak(f"Good Afternoon {s}")
    else:
        speak(f"Good Evening {s}")
wish_user()
while True:
    command=take_command()
    if "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "who is" in command:
        person=command.replace("who is","")
        info=wikipedia.summary(person,2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("Goodbye")
        break
'''

import pyttsx3
import speech_recognition as sr
import datetime
import time
def speak(text):
    print(text)
    engine = pyttsx3.init() 
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.1)
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except Exception:
        print("Sorry, please say that again")
        return ""
def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        correct_greeting = "good morning"
    elif hour < 18:
        correct_greeting = "good afternoon"
    else:
        correct_greeting = "good evening"
    speak(f"{correct_greeting}. I am your virtual assistant.")
    speak("Please greet me back and tell me your name.")
    user_response = take_command()
    print("User response captured:", repr(user_response))
    if not user_response:
        speak("Sorry, I didn’t catch that.")
        return
    user_name = None
    if "my name is" in user_response:
        user_name = user_response.split("my name is")[-1].strip()
    else:
        user_name = "friend"  
    if correct_greeting in user_response:
        speak(f"Correct! Thank you for greeting me,{user_name}.")
    elif ("good morning" in user_response or
          "good afternoon" in user_response or
          "good evening" in user_response):
        speak(f"That is incorrect, {user_name}. It is {correct_greeting}, not another time of day.")
    else:
        speak(f"I could not recognize a proper greeting,{user_name}.")
wish_user()











