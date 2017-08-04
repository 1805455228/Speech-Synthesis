#Here, we are converting simple text input in speech with the help of "pyttsx" - text to speech engine.

import pyttsx
engine = pyttsx.init()

while True:
    data = raw_input("Inset your text")
    engine.say(data)
    engine.runAndWait()
