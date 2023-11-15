import datetime
import socket
import threading
from messaging import sendTextMessage
from database import Database
import localMessagingConstants as msgCons


class Server:
    def __init__(self):
        ''' Networking and communication setup '''
        self.HEADER = msgCons.HEADER_SIZE
        self.PORT = msgCons.PORT
        self.IP = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.IP, self.PORT)
        self.ENCODING_FORMAT = 'utf-8'
        
        # TODO: Write wrapper function for this so we can pass arguments to individual functions
        # i.e.: handleMessage(*optional args*), optional args are used for each
        # different subfunction in function map
        self.FUNCTION_MAP = {
            msgCons.SEND_TEXT_MESSAGE: self.__sendText,
            msgCons.ADD_ENTRY_MESSAGE: self.__registerNumber,
            msgCons.DISCONNECT_MESSAGE: self.__disconnectClient
        }

        self.__activeConnections = set()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.bind(self.ADDR)

        ''' Database setup '''
        self.db = Database()

    def start(self):
        print('[STARTING] Server is starting')
        self.__socket.listen()
        print(f'[LISTENING] Server is listening on {self.ADDR}')
        while True:
            ''' Line below blocks, we will wait for a conn
                on conn, will continue. Returns a socket
                representing the connection and its address'''
            conn, addr = self.__socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')

    def handle_client(self, conn, addr):
        self.__activeConnections.add(conn)
        print(f'[NEW CONNECTION] {addr} connected.')

        while conn in self.__activeConnections:
            ''' First message contains information regarding
                the size of the following message.'''
            msgLen = conn.recv(self.HEADER).decode(self.ENCODING_FORMAT)
            if msgLen:
                print("Message len contents " + str(msgLen))
                msgLen = int(msgLen)
                msg = conn.recv(msgLen).decode(self.ENCODING_FORMAT)
                self.__handleMessage(conn, msg)

                print(f'[{addr}] {msg}')
        conn.close()

    def __handleMessage(self, conn: socket.socket, msg: str):
        msgType, data = msg.split(msgCons.TYPE_SEPARATOR)
        if msgType == msgCons.QUERY_MESSAGE:
            if msgType is msgCons.QUERY_MESSAGE:
                print("wtf?")
            print("huh?")
        if msgType == msgCons.SEND_TEXT_MESSAGE:
            # TODO: Might need to parsa data to right type
            self.__sendText(data)
        elif msgType == msgCons.ADD_ENTRY_MESSAGE:
            # TODO: Might need to parsa data to right type
            self.__registerNumber(data)
        elif msgType == msgCons.QUERY_MESSAGE:
            query = self.__queryDb(data)
            self.__returnQuery(query)
        elif msgType == msgCons.DISCONNECT_MESSAGE:
            self.__disconnectClient(conn)
        else:
            print("Error: Invalid message type")

    def __disconnectClient(self, conn):
        self.__activeConnections.remove(conn)

    def __sendText(phoneNo: str):
        sendTextMessage(phoneNo)

    def __registerNumber(self, phoneNo: str):
        # Change datetime to unix time, change db if unix to UNSENT
        self.db.addEntry(
            datetime.datetime.now(),
            phoneNo=phoneNo,
            orderNo=23
        )

    def __queryDb(self, data: str):
        fields = data.split(msgCons.INTRA_SEPARATOR)
        print("fields")
        print(fields)
        return self.db.query(*fields)

    