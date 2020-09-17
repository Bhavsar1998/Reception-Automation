import TextToSpeech
import DB
import MainRunCode
import route_try
import Tokenize
import message
while True:
    print("You:: ",end='')
    trigger=input()
    if trigger=="Reception":
        print("RoboCeption: Welcome to Acropolis. This is RoboCeption, How May I help you ?")
        TextToSpeech.textToSpeech("Welcome to Acropolis. This is RoboCeption, How May I help you ?")
        while True:
            print("You:: ",end='')
            request=input()
            response=MainRunCode.chat(request)
            if response[0]=="Thanks" or response[0]=="goodbye":
                print("RoboCeption: ",response[1])
                TextToSpeech.textToSpeech(response[1])
                break

            if response[0].isdigit():
                print("type your name: ",end='')
                TextToSpeech.textToSpeech("What is your Name ?")
                print("You:: ",end='')
                visitor_name = input()
                # print(visitor_name)
                visitor_name=Tokenize.preprocess(visitor_name)
                print(visitor_name)
                print("type your purpose: ",end='')
                TextToSpeech.textToSpeech("What is your purpose ?")
                print("You:: ",end='')
                purpose = input()
                staff_id=int(response[0])
                staff_info=DB.database_function(staff_id, visitor_name, purpose)
                if staff_info == None:
                    print("Sorry !! This record is not presnt in our data.")
                    TextToSpeech.textToSpeech("Sorry !! This record is not present in our data.")
                elif len(staff_info)==1:
                    absent=""
                    absent=staff_info[0]+" is not present right now."
                    print("RoboCeption: ",absent)
                    TextToSpeech.textToSpeech(absent)
                else:
                    cabin_no=str(staff_info[1])+'.gif'
                    to_contact=staff_info[3]
                    print("RoboCeption: ",response[1])
                    TextToSpeech.textToSpeech(response[1])
                    message.message(visitor_name, purpose, to_contact)
                    route_try.intialize_map(cabin_no)

            else:
                if(response[0]=="canteen_path"):
                    print("RoboCeption: ",response[1])
                    TextToSpeech.textToSpeech(response[1])
                    route_try.intialize_map('canteen_path.gif')
                elif response[0]=="Transport_path":
                    print("RoboCeption: ",response[1])
                    TextToSpeech.textToSpeech(response[1])
                    route_try.intialize_map('Transport_path.gif')
                elif response[0]=="Student_window_path":
                    print("RoboCeption: ",response[1])
                    TextToSpeech.textToSpeech(response[1])
                    route_try.intialize_map('Student_window_path.gif')
                elif response[0]=="Fees_path":
                    print("RoboCeption: ",response[1])
                    TextToSpeech.textToSpeech(response[1])
                    route_try.intialize_map('Fees_path.gif')
                elif response[0]=="CDC_path":
                    print("RoboCeption: ",response[1])
                    TextToSpeech.textToSpeech(response[1])
                    route_try.intialize_map('CDC_path.gif')
                else:
                    print("RoboCeption: ",response[1])
                    TextToSpeech.textToSpeech(response[1])



