import speech_recognition as sr
import pyttsx3 as ptxt

listener=sr.Recognizer()
engine=ptxt.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...!")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        talk("ok,playing song")
        print("ok,playing song")

while True:
    run_alexa()        