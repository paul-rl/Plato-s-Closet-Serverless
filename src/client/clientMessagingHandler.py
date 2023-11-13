import socket
import localMessagingConstants as msgCons


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

    def sendQueryMsg(self, fromDate, toDate, phoneNo, orderNo):
        queryTuple = (fromDate, toDate, phoneNo, orderNo)
        data = msgCons.INTRA_SEPARATOR.join(queryTuple)
        self.__send(f'{msgCons.QUERY_MESSAGE}{msgCons.TYPE_SEPARATOR}{data}')

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
