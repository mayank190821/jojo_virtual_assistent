# importing libraries
import datetime
import os
import random
import webbrowser as wb

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)


def speak(audio_data):
    '''
    It take audio_data and speak that data.
    :param audio_data: audio data take as parameter.
    '''
    engine.say(audio_data)
    engine.runAndWait()


def wishMe():
    '''
    Take realtime date and wish according to it.
    '''
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0) and (hour < 12):
        speak("Good Morning")
    elif (hour >= 12) and (hour < 18):
        speak("Good After Noon")
    else:
        speak("Good Evening")
    speak("I am JOJO sir. How can i help you?")


def takeCommand():
    '''
    It take Microphone input from the user.
    :return: voice_command
    '''
    global voice_command
    r = sr.Recognizer()
    r.energy_threshold = 1700
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_command = r.recognize_google(audio)
            print("Command: " + voice_command)
        except Exception as e:
            speak("sorry, I didn't get it.")
        if voice_command == "exit":
            speak("Thanks for using me sir.")
            exit()
        return voice_command


if __name__ == '__main__':
    wishMe()
    while (True):
        voice_command = ''
        print("Listening...")
        voice_command = takeCommand().lower()
        # Logic for executing tasks based on command
        if "wikipedia" in voice_command:
            speak("Searching wikipedia...")
            voice_command = voice_command.replace('wikipedia', "")
            results = wikipedia.summary(voice_command, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open google' in voice_command:
            speak('opening google...')
            wb.open('www.google.com')
        elif 'play music' in voice_command:
            speak('playing music...')
            music_dir = 'G:\\cd'
            songs = os.listdir(music_dir)
            song_number = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[song_number]))
