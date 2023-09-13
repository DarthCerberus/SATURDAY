#Language: Python
#Author: Cerberus16731
#Status: In Progress

#Dependancies:
import pyttsx3 as tts  #Used for text to speech functionality.
import webbrowser as wb #used to open web pages.
import wikipedia as wiki #used for defionitions.
import speech_recognition as sr #used for speech to text.

#Define things
def define(key):
     summary = wiki.summary(key,sentences=3,auto_suggest=False)
     return summary

#Text to Speech
def speak(text):
     """speak(text) : This function converts given text to speech using pyttsx3 library.
     text: str, preferably easy to hear in robotic voice.
     """
     engine = tts.init()
     engine.say(text)
     engine.runAndWait()

#webbrowser
wb.register("firefox",None,wb.BackgroundBrowser(r"C:\Program Files\Mozilla Firefox\firefox.exe"))   #Registering firefox as browser to use.
firefox = wb.get('firefox')
#wb.register("torr",None,wb.BackgroundBrowser(r"C:\Program Files\Tor Browser\Browser\firefox.exe"))
def web_open(url):
   """web_open(url): This function opens a webpage given url.
   url: str, preferably in proper format.
   """
   firefox.open_new(url)

#Speech to text
def hear():
     r = sr.Recognizer()
     try:
          with sr.Microphone() as source:
               r.adjust_for_ambient_noise(source)
               print("speak now")
               audio = r.listen(source,timeout=20,phrase_time_limit=30)
               spoken_text = r.recognize_google(audio) 
               print(f"You said: {spoken_text}")
          return spoken_text
     except Exception as e:
          print(str(e))

#main function
def main():

     speak("Hello, I'm saturday, your virtual assistant. How can i assist?")
     while True:
          command = hear()
          command = command.lower()
          if command is None:
               break
          if command == "kill":
               speak("Have a good day sir")
               break
          if "define" in command:
               try:
                    speak(define(command.replace("define"," ")))
               except Exception as e:
                    print(str(e))
                    web_open(f"https://www.google.com/search?&q={command}")


          if "search" in command:
               web_open(f"https://www.google.com/search?&q={command.replace('search',' ')}")

          

#run script
if __name__ == '__main__':
     main()