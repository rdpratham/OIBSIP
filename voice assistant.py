import speech_recognition as sr
import datetime
import webbrowser
import pyttsx3


r = sr.Recognizer()


engine = pyttsx3.init()

def respond(text):
    engine.say(text)
    engine.runAndWait()

def get_current_time():
    now = datetime.datetime.now()
    respond("The current time is " + now.strftime("%H:%M:%S"))

def get_current_date():
    now = datetime.datetime.now()
    respond("Today's date is " + now.strftime("%B %d, %Y"))

def search_web(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)
    respond("Searching for " + query)

def main():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        input = r.recognize_google(audio)
        print("You said: ", input)

        if 'hello' in input.lower():
            respond("Hello! How can I assist you today?")
        elif 'time' in input.lower():
            get_current_time()
        elif 'date' in input.lower():
            get_current_date()
        elif 'earch' in input.lower():
            query = input.replace("search", "")
            search_web(query)
        else:
            respond("I didn't understand that. Please try again!")

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again!")
    except sr.RequestError as e:
        print("Error: ", e)

if __name__ == "__main__":
    while True:
        main()