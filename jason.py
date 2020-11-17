#!/usr/bin/env python
from twilio.rest import Client
import speech_recognition as sr
import time
import pyttsx3
from datetime import date
import wikipedia
from datetime import datetime
import requests
import calendar
import pyjokes
import pywhatkit
import os

os.system('rm Setup')

# Settings
ccity = 'Wilmington'
api_key = "5ee35b677452b4f0f9ce23def22c4973"  # Your openweather api key
units = 'imperial'
temperature_unit = 'F'

account_sid = 'AC69939f516ffb94345219ab580fce7756'
auth_token = '72cdc42f41d398d29e1473637310426b'

client = Client(account_sid, auth_token)


def speak(text):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[2].id)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.RequestError as e:
            print("Request Error")
        except sr.UnknownValueError:
            print("Unknown Value Error")

    return said


speak('starting up...')

WAKE = "Jason"
text = get_audio()

while True:
    text = get_audio()

    if text.count(WAKE) > 0:
        speak("What do you need?")
        text = get_audio()

        if "hello" in text:
            speak("Hello, how are you")

        elif "stop" in text:
            speak("goodbye")
            os.system('pkill -a -i "Google Chrome"')

        elif "what is your name" in text:
            speak("My name is Jason. I was created by Michael bonner")

        elif "is your name" in text:
            speak("My name is Jason. I was created by Michael bonner")

        elif "your name" in text:
            speak("My name is Jason. I was created by Michael bonner")

        elif 'weather' in text:
            icons_list = {
                "01d": "Clear Sky Today:",  # Clear sky day.
                "01n": "Clear Sky Tonight:",  # Clear sky night.
                "02d": "Few Clouds Today:",  # Few clouds day.
                "02n": "Few Clouds To Night:",  # Few clouds night.
                "03d": "Scattered Clouds Today:",  # Scattered clouds day.
                "03n": "Scattered Clouds Tonight",  # Scattered clouds night.
                "04d": "Broken Clouds Today:",  # Broken clouds day.
                "04n": "Broken Clouds Tonight:",  # Broken clouds night.
                "09d": "Showers Today:",  # Shower rain day.
                "09n": "Showers Tonight:",  # Shower rain night.
                "10d": "Rain Today:",  # Rain day.
                "10n": "Rain Tonight:",  # Rain night
                "11d": "Thunderstorms Today:",  # Thunderstorm day.
                "11n": "Thunderstorms Tonight:",  # Thunderstorm night
                "13d": "Snow Today:",  # Snow day. Snowflake alternative: 
                "13n": "Snow Tonight:",  # Snow night. Snowflake alternative: 
                "50d": "Mist Today:",  # Mist day.
                "50n": "Mist Today:",  # Mist night.
            }

            atmophere_icons_list = {
                701: "Mist",  # Mist
                711: "Smoke",  # Smoke
                721: "Haze",  # Haze
                731: "Dust",  # Dust (Sand / dust whirls)
                741: "Fog",  # Fog
                751: "Sand",  # Sand
                761: "Dust",  # Dust
                762: "Ash",  # Ash
                771: "Squalls",  # Squalls
                781: "Tornado"  # Tornado
            }


            def main():
                try:
                    # Get data from openweather
                    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(city, units,
                                                                                                         api_key)
                    result = requests.get(url)

                    # If result was received
                    if result.status_code == requests.codes['ok']:
                        # Read json
                        weather = result.json()

                        # Get info from array
                        id = int(weather['weather'][0]['id'])
                        group = weather['weather'][0]['main'].capitalize()
                        icon = weather['weather'][0]['icon'].capitalize()
                        temp = int(float(weather['main']['temp']))

                        # Load another icons for Atmosphere group
                        if (group == "Atmosphere"):
                            return atmophere_icons_list[id] + ' {}°{}'.format(temp, temperature_unit)

                        return icons_list[icon] + ' {}°{}'.format(temp, temperature_unit)

                except:
                    return ""  # Return reload icon


            if __name__ == "__main__":
                speak(main())

        elif 'what time' in text:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[2].id)

            speak('Getting time')

            speak_time = time.strftime("%I %M %p")
            print(speak_time)

            engine.say('Its' + speak_time)
            engine.runAndWait()
            engine.stop()

        elif 'is it' in text:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[2].id)

            speak_time = time.strftime("%I %M %p")
            print(speak_time)

            engine.say('Its' + speak_time)
            engine.runAndWait()
            engine.stop()

        elif 'date' in text:
            my_date = date.today()
            the_date = datetime.today().day

            if the_date == 1:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'first')

            if the_date == 2:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'second')

            if the_date == 3:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'third')

            if the_date == 4:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'fourth')

            if the_date == 5:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'fifth')

            if the_date == 6:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'sixth')

            if the_date == 7:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'seventh')

            if the_date == 8:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'eighth')

            if the_date == 9:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'ninth')

            if the_date == 10:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'tenth')

            if the_date == 11:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'eleventh')

            if the_date == 12:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twelfth')

            if the_date == 13:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'thirteenth')

            if the_date == 14:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'fourteenth')

            if the_date == 15:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'fifteenth')

            if the_date == 16:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'sixteenth')

            if the_date == 17:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'seventeenth')

            if the_date == 18:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'eighteenth')

            if the_date == 19:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'nineteen')

            if the_date == 20:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twentieth ')

            if the_date == 21:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twenty first')

            if the_date == 22:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twenty second')

            if the_date == 23:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twenty third')

            if the_date == 24:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twenty fourth')

            if the_date == 25:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twenty fifth')

            if the_date == 26:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twenty sixth')

            if the_date == 27:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twenty seventh')

            if the_date == 28:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twenty eighth')

            if the_date == 29:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'twenty ninth')

            if the_date == 30:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'thirtieth')

            if the_date == 31:
                speak(calendar.day_name[my_date.weekday()] + calendar.month_name[my_date.month] + 'thirty first')
        elif 'search' in text:
            speak('Searching on Wikipedia...')
            text = text
            get_audio()
            speak('Searching...')
            speak(wikipedia.summary(text, sentences=2))

            if wikipedia.DisambiguationError:
                speak('Please repeat that')

            if wikipedia.HTTPTimeoutError:
                print('Please repeat that')

            if wikipedia.RedirectError:
                print('Please repeat that')

        elif 'joke' in text:
            speak(pyjokes.get_joke())

        elif 'Sing' in text:
            speak('playing ' + text + 'from youtube.com')
            pywhatkit.playonyt(text)

        elif 'sing' in text:
            speak('playing ' + text + 'from youtube.com')
            pywhatkit.playonyt(text)

        elif 'calculator' in text:
            speak('Would you like to add, multiply, subtract, or divide')
            text = get_audio()
            time.sleep(3)
            loop = True
            while loop == True:
                if 'add' in text:
                    speak('What is your first number')
                    text = get_audio()
                    time.sleep(3)
                    number1 = text
                    speak('What is your second number')
                    text = get_audio()
                    time.sleep(3)
                    number2 = text
                    print(sum(number1, number2))



        else:
            speak('I m sorry i do not know that one')
