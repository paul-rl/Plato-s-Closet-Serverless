from twilio.rest import Client
from twilioConstants import accountSid, authToken, twilioPhoneNo
from pathlib import Path
import sys
sys.path.insert(0, str(Path().parent.absolute() / 'src'))
from shared.textBody import getTextBody


def sendTextMessage(phoneNo):
    client = Client(accountSid, authToken)

    message = client.messages.create(
        from_=twilioPhoneNo,
        body=getTextBody(),
        to=phoneNo
    )

    print(message.sid)
