import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Iam listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'open' in command:
        g=command.replace('open','')
        talk("opening"+g)
        pywhatkit.search(g)         #modified 

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'day' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who ' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'search' in command:
        person = command.replace('keyword', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
   
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
   
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    # modified by rsmp
    elif 'name' in command:
        talk("Hi,Iam Aida,your personal assistant")
        talk("How can i help you")  

    elif 'who are you' in command:
        talk("Hello,Iam Alexa")
        talk("How can i help")  
    else:
        talk('Sir,could you repeat yourself,iam not clear..!.')


while True:
    run_alexa()