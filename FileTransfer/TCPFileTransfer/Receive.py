#! /usr/bin/python

# Receive a file from Transfer.py. This script MUST be run first.
# The port by default is 8888.
# Receive.py [--port port] path_to_write_file
# Example: Receive.py --port 8888 C:\Users\ken\Desktop

from socket import *
from sys import argv
import os
import time

### HELP AND ERROR MESSAGES
HELP_MSG_SYNTAX = "Syntax - Receive.py [--port port] path_to_write_file"
HELP_MSG_EXAMPLE = "Example - Example: Receive.py --port 8888 C:\Users\ken\Desktop"
HELP_MSG_FULL = HELP_MSG_SYNTAX + "\n" + HELP_MSG_EXAMPLE


### I N P U T   P A R A M E T E R S
NB_REQUIRED_PM = 2
if len(argv) != NB_REQUIRED_PM and len(argv) != (NB_REQUIRED_PM + 2):
	print("Error, wrong parameters")
	print(HELP_MSG_FULL)
	exit()

# Set port
PORT = 8888
pm_offset = -1 
if "--port" in argv:
	pm_offset += 2 
	index = argv.index("--port")
	if index != 1:
		print("Error, bad syntax")
		print(HELP_MSG_FULL)
		exit()
	PORT = int(argv[index+1])
	
# Set Path
PATH = argv[pm_offset + 2]
if '/' in PATH and '\\' in PATH:
	print("Error, bad path value. Path - " + PATH)
	exit()

if '/' in PATH and PATH[-1:] != '/':
	PATH += '/'
	
if '\\' in PATH and PATH[-1:] != '\\':
	PATH += '\\'


# F U N C T I O N S
def CreateFile(_path, _content):
    full_path = _path + "download_" + str(time.time()) + ".txt"
    file = open(full_path, "wb")
    file.write(_content)
    file.close()


### M A I N   S C R I P T
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
read_msg = "a"
EMPTY = bytes()
while read_msg != EMPTY:
    read_msg = peer.recv(MAX_RECEPTION_SIZE)
    content += read_msg

peer.close()                    # File download is done so we stop the connection
s.close()                       # Currently, files can only be sent one by one. No further connections allowed.

# Writing file to HD
print("Creating file to " + PATH)
CreateFile(PATH, content)
print("Success.")

