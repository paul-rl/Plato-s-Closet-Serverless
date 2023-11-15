import datetime
import socket
import threading
from messaging import sendTextMessage
from database import Database
import localMessagingConstants as msgCons
from math import ceil


class Server:
    def __init__(self):
        ''' Networking and communication setup '''
        self.HEADER = msgCons.HEADER_SIZE
        self.PORT = msgCons.PORT
        self.IP = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.IP, self.PORT)
        self.ENCODING_FORMAT = 'utf-8'

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

        if msgType == msgCons.SEND_TEXT_MESSAGE:
            self.__sendText(data)
        elif msgType == msgCons.ADD_ENTRY_MESSAGE:
            self.__registerNumber(data)
        elif msgType == msgCons.QUERY_MESSAGE:
            query = self.__queryDb(data)
            self.__returnQuery(conn, query)
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
            phoneNo=phoneNo
        )

    def __queryDb(self, data: str):
        fields = data.split(msgCons.INTRA_SEPARATOR)
        if fields[0] == msgCons.DEFAULT_DATE:
            fields[0] = None
        if fields[1] == msgCons.DEFAULT_DATE:
            fields[1] = None
        return self.db.query(*fields)

    def __returnQuery(self, conn: socket.socket, query):
        # check how message size relates to sending message
        # Make protocol for splitting long messages
        msg = ':'.join({"apple", "potato", "banana", "water", "juice", "milk", "kiwi", "pineapple", "pen"})
        print(msg)

        message = msg.encode(self.ENCODING_FORMAT)
        msgLen = len(message)
        sendLen = str(msgLen).encode(self.ENCODING_FORMAT)
        # Pad length message to header specified length
        sendLen += b' ' * (self.HEADER - len(sendLen))
        print(f"Sending length: {sendLen}")
        conn.send(sendLen)

        # Information must be relayed across multiple messages
        if msgLen > self.HEADER:
            numMessages = ceil(msgLen / self.HEADER)
            for i in range(0, numMessages):
                startIdx = i * self.HEADER
                chunk = message[startIdx:startIdx + self.HEADER]
                print(f"Sending chunk {chunk}")
                conn.send(chunk)
        else:
            print(f"Sending message {message}")
            conn.send(message)
