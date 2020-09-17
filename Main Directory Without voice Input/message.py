import os
from twilio.rest import Client

def message(visitor_name, purpose, to_contact):
    account_sid = 'AC0e0d3c6d6550b2443f2fd0deae64f1b6'
    auth_token = 'e9e5478930ead8b9c65950e62a0c5644'
    client = Client(account_sid, auth_token)
    # to_contact=''
    # message_body=""
    message_body="\nDear staff, This is from Roboception.\n Visitor Name: "+visitor_name+"\n Purpose: "+purpose
    # print(to_contact)
    to_contact='+91'+to_contact
    # print(to_contact)
    message = client.messages \
                    .create(
                         body=message_body,
                         from_='+19732873753',
                         to=to_contact
                     )

    print(message.sid)
# message("kunal"," apointment",'7987350755')