import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import webPages
import requests

# from openai import OpenAI
from google import genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):

    client = genai.Client(api_key="Your_gemini_Api")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="You are an AI virtual assistant named Jarvis, skilled in performing a wide range of tasks similar to Alexa or Google Assistant. You were created by Akash Ghosh. You can understand and speak multiple languages, and you will communicate with the user in the language they use. This is user input" + command,
    )

    return response.text

def processCommand(c):
    if c.lower().startswith("open"):
        web = c.lower().split(" ")[1]
        link = webPages.webpage[web]
        webbrowser.open(link)
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=a8ffe627666346178603ca9e9d957b34")
        if r.status_code == 200:
            headlines = r.json()
            for article in headlines['articles']:
                speak(article['title'])

    #AI handle other requests
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()

        print("recognizing...")
        try:
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
