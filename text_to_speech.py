import pyttsx3


# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)
# engine.say("Hello")
# engine.runAndWait()

class Speech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 100)
        # voices = engine.getProperty('voices')
        self.engine.setProperty('volume', 1.0)

    def speak(self, text: str):
        self.engine.say("Hello")
        self.engine.runAndWait()
