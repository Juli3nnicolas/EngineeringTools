#! /usr/bin/python

# Send a file. The recipient must run Receive.py
# Transfer.py [-p port_number] recipient's_ip path_to_file
# The port by default is 8888.
# Call examples: 
#   Transfer.py 192.168.1.10 C:\Users\bob\Desktop\foo.txt
#   Transfer.py -p 8888 192.168.1.10 C:\Users\bob\Desktop\foo.txt

from socket import *

def SendFile(_path, _socket):
    # Open the file and store its content
    file = open(_path, "rb")
    content = file.read()
    file_size = file.file_size

    # Send content
    count = 0
    while count < file_size:
        count += _socket.send(content)

ADDR = "192.168.1.95"
PORT = 8888
PATH = "C:\\Users\\junic\\Desktop\\Transfer\\Tree.jpg"

# Create TCP socket
s = socket(AF_INET, SOCK_STREAM)
s.connect((ADDR, PORT))

print("Sending file " + PATH + " to " + ADDR)
SendFile(PATH, s)
s.close()
print("Success.")