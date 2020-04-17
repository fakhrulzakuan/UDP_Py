import socket
import pickle
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

#Send string - default
#MESSAGE = "Hello, World!"

#Send list of sorts of data type - using pickle
ts = int(time.time())
data = [ts, 1.2323,23232,-0.34, [2,'hj']]
MESSAGE = pickle.dumps(data)

#send int or float
# data = 1.2323
# MESSAGE = pickle.dumps(data)

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", data #MESSAGE
# if using pickle need to decode the msg
# print "message:", pickle.loads(MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while True:                    
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    time.sleep(0.1)