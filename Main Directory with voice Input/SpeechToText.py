# import TextToSpeech
import speech_recognition as sr
def speechToText():
    while(1):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            t=""
            try:
                text = r.recognize_google(audio)
                t=format(text)
                # print("You said : {}".format(text))
                if len(t)!=0:
                    return (t)


            except:
                print("Sorry could not recognize what you said, please speak again")
# print(speechToText())