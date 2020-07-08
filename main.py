import pyttsx3
import PyPDF2
import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import glob

def get_audio():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    said = ""

    try:
        said = r.recognize_google(audio)
        print(said)
    except Exception as e:
        print("Exception:" + str(e))

  return said

def speak_text():
 v = gTTS(text=air, lang="en", slow=False)
 v.save("audio.mp3")
 playsound("audio.mp3")

air="Hello, This programme will read out pdf for you. Are you ready?"
print(air)
speak_text()

air="Now i will read out all pdf files from your download folder one by one. Speak no if that file is not what you want to read. Else say yes!"
print(air)
speak_text()
os.chdir('/Users/aditya/Downloads')
x = glob.glob('*.pdf')
for i in x:
    print(i)
    air=i
    speak_text()
    yn=get_audio()
    if "yes" in yn:
        val = i
        break
    else:
        continue


val=i
book = open(val, 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = str(pdfReader.numPages)
air="Total number of pages in your file is:" + pages
speak_text()
print(air)

speaker = pyttsx3.init()

air="Enter words per minute you want to hear:"
speak_text()
print(air)
speed = int(get_audio())
speaker.setProperty('rate', speed)

voices = speaker.getProperty('voices')
en_voice_id = "com.apple.speech.synthesis.voice.moira"
speaker.setProperty('voice', en_voice_id)

air="Enter starting page number:"
speak_text()
print(air)


pageno = int(get_audio())
air="Now i will start reading out the pdf which you have specified"
speak_text()
print(air)
for num in pages:
 page = pdfReader.getPage(pageno-1)
 text = page.extractText()
 speaker.say(text)
 speaker.runAndWait()
 pageno=pageno+1
