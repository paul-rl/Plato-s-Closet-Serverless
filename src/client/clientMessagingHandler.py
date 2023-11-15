import socket
import localMessagingConstants as msgCons
from datetime import date
from math import ceil

class ClientMessagingHandler:
    def __init__(self) -> None:
        self.HEADER = msgCons.HEADER_SIZE
        self.PORT = msgCons.PORT
        self.FORMAT = msgCons.ENCODING_FORMAT
        self.SERVER = msgCons.SERVER_ADDR
        self.ADDR = (self.SERVER, self.PORT)

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.__socket.connect(self.ADDR)
        except ConnectionRefusedError:
            #TODO: Create error dialog and add here
            print("Could not establish connection with server.")
            

    def disconnectFromServer(self):
        self.__send(msgCons.DISCONNECT_MESSAGE)

    def sendAddEntryMsg(self, phoneNo):
        self.__send(f'{msgCons.ADD_ENTRY_MESSAGE}{msgCons.TYPE_SEPARATOR}{phoneNo}')

    def sendSendTextMsg(self, phoneNo):
        self.__send(f'{msgCons.SEND_TEXT_MESSAGE}{msgCons.TYPE_SEPARATOR}{phoneNo}')

    def __sendQueryMsg(self,
                       fromDate: date,
                       toDate: date,
                       phoneNo: int):
        fDate = fromDate.strftime("%Y-%m-%d")
        tDate = toDate.strftime("%Y-%m-%d")
        queryTuple = (fDate, tDate, str(phoneNo))
        data = msgCons.INTRA_SEPARATOR.join(queryTuple)
        self.__send(f'{msgCons.QUERY_MESSAGE}{msgCons.TYPE_SEPARATOR}{data}')

    def queryWithResults(self,
                         fromDate: date,
                         toDate: date,
                         phoneNo: int,):
        self.__sendQueryMsg(fromDate, toDate, phoneNo)
        return self.__receiveQueryResult()

    def __receiveQueryResult(self):
        response = b""
        responseLen = self.__socket.recv(self.HEADER)
        if responseLen:
            responseLen = int(responseLen)
            # Need to parse multiple messages
            if responseLen > self.HEADER:
                numMessages = ceil(responseLen / self.HEADER)
                for i in range(0, numMessages):
                    response += self.__socket.recv(self.HEADER)
            else:
                response = self.__socket.recv(self.HEADER)
        return response.decode(self.FORMAT)

    def __send(self, msg):
        ''' Send message stating length of next message'''
        message = msg.encode(self.FORMAT)
        msgLen = len(message)
        sendLen = str(msgLen).encode(self.FORMAT)
        # Pad length message to header specified length
        sendLen += b' ' * (self.HEADER - len(sendLen))
        print("Sending length: " + str(sendLen))
        self.__socket.send(sendLen)
        print("Sending message: " + str(sendLen))
        self.__socket.send(message)
