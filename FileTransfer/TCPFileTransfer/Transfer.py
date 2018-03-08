#! /usr/bin/python

# Send a file. The recipient must run Receive.py
# Transfer.py [--port port_number] ip_recipient full_path_to_file
# The port by default is 8888.
# Call examples: 
#   Transfer.py 192.168.1.10 C:\Users\bob\Desktop\foo.txt
#   Transfer.py --port 8888 192.168.1.10 C:\Users\bob\Desktop\foo.txt

from socket import *
import os
from sys import argv

# Help or error messages
HELP_MSG_SYNTAX = "Syntax - Transfer.py [--port port_number] ip_recipient full_path_to_file"
HELP_MSG_EXAMPLE = "Example - Transfer.py --port 8888 192.168.1.10 C:\\Users\\bob\\Desktop\\foo.txt"
HELP_MSG_FULL = HELP_MSG_SYNTAX + "\n" + HELP_MSG_EXAMPLE

# Read input parameters
NB_REQUIRED_ARGS = 3
if len(argv) != NB_REQUIRED_ARGS and len(argv) != (NB_REQUIRED_ARGS + 2):
    raise RuntimeError("Wrong number of parameters\n" + HELP_MSG_FULL)

flag_index = -1
PORT = 8888
if "--port" in argv:
    flag_index = argv.index("--port")
    if flag_index != 1:
        raise RuntimeError("Wrong parameter.\n" + HELP_MSG_FULL)

    PORT = argv[flag_index + 1]

ADDR = argv[flag_index+2]
PATH = argv[flag_index+3]

def SendFile(_path, _socket):
    # Open the file and store its content
    file = open(_path, "rb")
    content = file.read()
    file_size = os.stat(_path).st_size

    # Send content
    count = 0
    while count < file_size:
        count += _socket.send(content)

# Create TCP socket
s = socket(AF_INET, SOCK_STREAM)

try:
    s.connect((ADDR, PORT))
    SendFile(PATH, s)
    print("Sending file " + PATH + " to " + ADDR)
except ConnectionError:
    print("Couldn't connect to " + ADDR)
    
except FileExistsError:
    print("Couldn't open file. Path is " + PATH)
    s.close()
    print("Failure")
    exit()

s.close()
print("Success.")