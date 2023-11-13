import socket

HEADER = 16
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '192.168.1.127'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msgLen = len(message)
    sendLen = str(msgLen).encode(FORMAT)
    # Pad length message to header specified length
    sendLen += b' ' * (HEADER - len(sendLen))
    print("Sending length: " + str(sendLen))
    client.send(sendLen)
    print("Sending message: " + str(sendLen))
    client.send(message)


a = input()
send(a)
send("GAHDAMN")
send(DISCONNECT_MESSAGE)
