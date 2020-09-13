# importing libraries
import datetime

import pyttsx3

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


# Take data and speak
def speak(audio_data):
    engine.say(audio_data)
    engine.runAndWait()


# This function wish me according to time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good After Noon")
    else:
        speak("Good Evening")
    speak("I am JOJO sir. How can i help you?")


if __name__ == '__main__':
    wishMe()
