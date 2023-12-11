from twilio.rest import Client
from twilioConstants import accountSid, authToken, twilioPhoneNo
from pathlib import Path
import sys
import time
from threading import Thread
sys.path.insert(0, str(Path().parent.absolute() / 'src'))
from shared.textBody import getTextBody

class TextingClient:
    def __init__(self) -> None:
        self.MAX_ATTTEMPTS = 3
        self.client = Client(accountSid, authToken)
        self.undeliveredMessages = dict()

        thread = Thread(target=self.resendLoop)
        thread.start()

    def sendTextMessage(self, phoneNo):
        try:
            message = self.client.messages.create(
                from_=twilioPhoneNo,
                body=getTextBody(),
                to=phoneNo,
                )
            if message.to in self.undeliveredMessages:
                numAtts = self.undeliveredMessages[message.to][1]
                self.undeliveredMessages[message.to] = (message, numAtts + 1)
            else:
                self.undeliveredMessages[message.to] = (message, 1)
        except:
            print("There was an issue sending a message to this phone number")
    
    def verifyMessageDelivery(self, sid):
        status = self.client.messages(sid).fetch().status
        print(f"SID:{sid} Status:{status}")
        return status == 'delivered'

    def resendLoop(self):
        print("Resend loop initiated")
        starttime = time.monotonic()
        while True:
            if len(self.undeliveredMessages) != 0:
                self.resendUndeliveredMessages()
            time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))

    def resendUndeliveredMessages(self):
        dictCopy = self.undeliveredMessages.copy()
        for phoneNo in dictCopy:
            message, numAttempts = self.undeliveredMessages[phoneNo]
            if not self.verifyMessageDelivery(message.sid):
                if numAttempts < 3:
                    print(f"Resending to {message.to} att#: {numAttempts}")
                    self.sendTextMessage(message.to)
                else:
                    self.undeliveredMessages.pop(message.to)
                    print("Reached max number of attempts for " + message.to)
            else:
                self.undeliveredMessages.pop(message.to)
