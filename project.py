"""
Code created by - UTKARSH RASTOGI (ABESEC 2nd year CE BRANCH)
Use Python 3.8 anaconda interpreter for running this program successfully.
Write the Following Commands in the terminal for running this program successfully:
pip install pyttsx3
pip install speechRecognition
pip install pipwin
pipwin install pyaudio
NOTE:- User should the voice input only when he/she sees the word "Listening" on the console.
Not before that.
"""
import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    # It takes microphone input from the user and returns string output.
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,3)
        print("Listening")
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in',)
        print(f"User Said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    speak("Please select one option from below:")
    print("Please select one option from below:\n1) My Payslip\n2) My Attendance")
    choice = takeCommand().lower()
    if "my pay slip" in choice or "my payslip" in choice:
        speak("Which Month of the current Year ?.....")
        query = takeCommand().lower()
        if query == "january" or query == "february" or query == "march":
            speak("Pay slip is not available prior to April 2021...")
            print("Pay slip is not available prior to April 2021")
            exit()
        elif "april" in query or "fourth" in query or "four" in query or "4 " in query:
            speak("Here it is....")
            url = 'https://be.platform.simplifii.com/api/v1/custom/mypayslip?month=04'
            webbrowser.get().open(url)
        elif "may" in query or "fifth" in query or "m a y" in query or "five" in query or "5" in query:
            speak("Here it is....")
            url = 'https://be.platform.simplifii.com/api/v1/custom/mypayslip?month=05'
            webbrowser.get().open(url)
        elif "june" in query or "jun" in query or "sixth" in query or "six" in query or "6" in query:
            speak("Here it is....")
            url = 'https://be.platform.simplifii.com/api/v1/custom/mypayslip?month=06'
            webbrowser.get().open(url)
        elif "july" in query or "seventh" in query or "seven" in query or "7" in query:
            speak("Here it is....")
            url = 'https://be.platform.simplifii.com/api/v1/custom/mypayslip?month=07'
            webbrowser.get().open(url)
        elif "august" in query or "september" in query or "october" in query or "november" in query or "december" in query:
            speak("Pay slip for this month has not been generated yet....")
            print("Pay slip for this month has not been generated yet")
        else :
            speak("Please input a valid month...")
            print("Please input a valid month")
            exit()
    elif "my attendance" in choice:
        speak("I am unable to generate your attendance report")
        print("I am unable to generate your attendance report")
    else:
        speak("Invalid Input....Please choose a correct option...")
