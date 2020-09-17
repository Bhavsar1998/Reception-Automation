import pyttsx3

def textToSpeech(message):
    engine=pyttsx3.init()
    sound=engine.getProperty('voices')
    print(sound)
    engine.setProperty('voice', sound[1].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.say('{}'.format(message))
    engine.runAndWait()

# message='''
# hello everyone, welcome to automation of reception
# this is roboception of our college !!
# '''

# textToSpeech(message)