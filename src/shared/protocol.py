from socket import socket
from localMessagingConstants import HEADER_SIZE, ENCODING_FORMAT
from math import ceil


def send(conn: socket, msg: str):
    if len(msg) < 1:
        msg = 'None'
    message = msg.encode(ENCODING_FORMAT)
    msgLen = len(message)
    sendLen = str(msgLen).encode(ENCODING_FORMAT)
    # Pad length message to header specified length
    sendLen += b' ' * (HEADER_SIZE - len(sendLen))
    print(f"Sending length: {sendLen}")
    conn.send(sendLen)
    # Information must be relayed across multiple messages
    if msgLen > HEADER_SIZE:
        numMessages = ceil(msgLen / HEADER_SIZE)
        for i in range(0, numMessages):
            startIdx = i * HEADER_SIZE
            chunk = message[startIdx:startIdx + HEADER_SIZE]
            print(f"Sending chunk {chunk}")
            conn.send(chunk)
    else:
        print(f"Sending message {message}")
        conn.send(message)


def receive(conn: socket):
    print("Receiving results")
    response = b""
    responseLen = conn.recv(HEADER_SIZE)
    print("Received response len")
    if responseLen:
        print("Yes response len")
        responseLen = int(responseLen)
        # Need to parse multiple messages
        if responseLen > HEADER_SIZE:
            print("Large message incoming")
            numMessages = ceil(responseLen / HEADER_SIZE)
            for i in range(0, numMessages):
                response += conn.recv(HEADER_SIZE)
        else:
            print("Small mesage incoming")
            response = conn.recv(HEADER_SIZE)
            print("got small")
        print("Done receiving")
        return response.decode(ENCODING_FORMAT)
    else:
        print("None time")
        return None
