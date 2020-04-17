import socket
import pickle

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    # print "received message:", data

    #if transmitters sent pickle need to decode the data
    print pickle.loads(data)

    # if data != None:
    #     break