print("i'm best in the world")

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
#creating a listener which recognize the comand
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        #it use microphone to listen our voice
        with sr.Microphone() as source:
            print('listening.....')
            #creating a variable voice which listen and store the voice
            voice = listener.listen(source)
            #by using google api here voice is converted into text
            command = listener.recognize_google(voice)
            command.lower()
            if 'Alexa' in command:
                command = command.replace('Alexa', '')
                print(command)
    except:
        pass
    return command
#take_command()

def run_alexa():
    command = take_command();
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing...'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('current time is ' + time)
    elif 'who' in command:
        info = wikipedia.summary(command,2)
        print(info)
        talk(info)
    elif 'what' in command:
        info = wikipedia.summary(command,2)
        print(info)
        talk(info)
    elif 'how' in command:
        info = wikipedia.summary(command, 2)
        print(info)
        talk(info)
    elif 'when' in command:
        info = wikipedia.summary(command, 2)
        print(info)
        talk(info)
    elif 'why' in command:
        info = wikipedia.summary(command, 2)
        print(info)
        talk(info)
    elif 'where' in command:
        info = wikipedia.summary(command, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("I don't know motherfucker")
while True:
    run_alexa()
