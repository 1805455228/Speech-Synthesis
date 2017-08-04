#this program takes user question in text format and give reply in speech format

import pyttsx
from time import ctime
import webbrowser
import time

engine = pyttsx.init()

def replyGiven(data):
    if ("how are you") in data:
        engine.say("I am fine, %s" % name)
        engine.runAndWait()
        
    elif "what time it is" in data:
        engine.say(ctime())
        engine.runAndWait()
        
    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        engine.say("Hold on, I will show you where " + location + " is.")
        engine.runAndWait()
        url = "https://www.google.com/maps/place/" + location 
        webbrowser.open_new_tab(url)
    
    elif "believe in god" in data:
        engine.say("Ohh Dear, %s Humans have spiritualism. I have siliconism" % name)
        engine.runAndWait()
        
    elif "favourite colour" in data:
        engine.say("Well, My favourite colour is blue")
        engine.runAndWait()
        
    elif ("call" and "jarvis") in data:
        engine.say("I am afraid that I can't help you in making flying suit")
        engine.runAndWait()
        
    elif ("watch" and "game of thrones") in data:
        engine.say("yes. I would ask Jon Snow for some hints, but he knows nothing.")
        engine.runAndWait()
        
    elif ("what's up")  in data:
        engine.say("Nothing Much! Just working on python project")
        engine.runAndWait()
        
    elif "real" in data:
        engine.say("Sorry, %s, I have been advised not to discuss my exential status" % name)
        engine.runAndWait()    
     
    elif ("phone" or ("iphone" and "samsung"))  in data:
        engine.say("But Obivious!!! Iphone it is")
        engine.runAndWait()
        
    elif "stop time" in data:
        engine.say("I will, once i get back from the future")
        engine.runAndWait() 
        
    else:
        engine.say("I didn't get that! Can you repeat it again?")
        engine.runAndWait() 
        
engine.say('Hello there, May I know your name please?')
engine.runAndWait()

name = raw_input("Your Good Name is: ")
say = "Hi %s, what can i do for you?" % name
engine.say(say)
engine.runAndWait()

while True:
    data = raw_input("hi %s, what can i do for you? \n" % name )
    replyGiven(data)
    time.sleep(1)
    

