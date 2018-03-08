#! /usr/bin/python

# Receive a file from Transfer.py. One must run Transfer.py for
# this script to receive the file.
# The port by default is 8888.
# By default, the file received is saved in the script's current working directory, so make sure it has write access.
# Receive.py [--port port] [--path path_to_write_file] Transfer.py_ip
# Example: Receive.py --port 8888 --path C:\Users\ken\Desktop 192.168.1.12

from socket import *
import os
import time

def CreateFile(_path, _content):
    full_path = _path + "download_" + str(time.time()) + ".txt"
    file = open(full_path, "wb")
    file.write(_content)
    file.close()

PORT = 8888
PATH = "C:\\Users\\junic\\Desktop\\Receive\\" #os.getcwd()
MAX_RECEPTION_SIZE = 4096 # 4 KiB

# Waiting file
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', PORT))              # Allow connections to any addresses owned by this machine
s.listen(1)                     # Listen  but allow no more than 1 pending connection
print("Waiting file...")

# Download file
peer, peer_addr = s.accept()    # Accept first connection 
print("Connected to " + str(peer_addr))
print("Downloading file...")

content = bytes()
read_msg = bytes('1')
while read_msg != 0:
    read_msg = peer.recv(MAX_RECEPTION_SIZE)
    content += read_msg

peer.close()                    # File download is done so we stop the connection
s.close()                       # Currently, files can only be sent one by one. No further connections allowed.

# Writing file to HD
print("Creating file to " + PATH)
CreateFile(PATH, content)
print("Success.")

