from twilio.rest import Client
from twilioConstants import accountSid, authToken, twilioPhoneNo
from textBody import getTextBody


def sendText(phoneNo):
    client = Client(accountSid, authToken)

    message = client.messages.create(
        from_=twilioPhoneNo,
        body=getTextBody(),
        to=phoneNo
    )

    print(message.sid)
