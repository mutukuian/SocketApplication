import socket

HEADER = 64

PORT = 5050

FORMAT = 'utf-8'
DISCONECT_MESSAGE = "DISCONNECT"

SERVER ="192.168.83.49"
ADDR = (SERVER,PORT)


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)




def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))  # Use ' ' for padding
    client.send(send_length)
    client.send(message)

send("Hello world!")
send("I'm an android developer with 1 year of experience")
