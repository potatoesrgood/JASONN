#!/usr/bin/env python
import os

i = os.system

i('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"')
i('brew install python3')
i('pip3 install twilio')
i('pip3 install speechRecognition')
i('pip3 install pyttsx3')
i('pip3 install wikipedia')
i('pip3 install calendar')
i('pip3 install pyjokes')
i('pip3 install pywhatkit')
i('pip3 install pyaudio')
i('python jason.py')
