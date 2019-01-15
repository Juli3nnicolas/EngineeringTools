#! /usr/local/bin/python3

# Logs on stdout if files have been added or removed from targetted root directory.
# Use -c to display new files' content. 

import os
from sys import argv, exit
from time import sleep


# H E L P E R S

# Returns a set of all files from _rootDir (recursive)
def GetFiles(_rootDir):
    if ( not isinstance(_rootDir, str) ):
        raise TypeError("Path is not a string!")

    outFiles = list()
    for root, dirs, files in os.walk(_rootDir):
        for name in files:
            outFiles.append( os.path.join(root, name) )

    return set(outFiles)

# Shows file names prefixed with PATH_MARKER.
# Also shows content if FLAG_SHOW_CONTENT has been passed (content prefixed by CONTENT_MARKER)
# The function will try to log info whether the file has been added (_added == True) or removed
# (_added == False)
def CatFile(_path, _added):
    PATH_MARKER = "#p:"
    CONTENT_MARKER = "#c:"
    
    print(PATH_MARKER + " " + path)
    if _added == True and flag == FLAG_SHOW_CONTENT:
        # Open file
        try:
            f = open(path)

            # Read content
            try:
                content = f.read()
                print(CONTENT_MARKER + " " + content + "\n")
            except IOError:
                print("Error: Couldn't read file {0}".format(path))
            finally:
                f.close()
        except IOError:
            print("Error : couldn't open file {0}".format(path))



## P A R S E   C O M M A N D   L I N E   A R G U M E N T S

if len(argv) != 2 and len(argv) != 3:
    raise RuntimeError("Wrong number of parameters. You need to provide a full path.")

flag = ""
rootIndex = 1
FLAG_SHOW_CONTENT = "-c"

if argv[1] == FLAG_SHOW_CONTENT:
    flag = argv[1]
    rootIndex += 1

root = argv[rootIndex]



### M A I N   S C R I P T

Files = set()

try:
    Files = GetFiles(root)
except TypeError as error:
    print("Error : " + str(error))
    exit()

print("CatNewFiles (press ctrl+c to exit):\n")

try:
    while (True):
        sleep(0.5) # Sleep for 0.5 seconds
        f = GetFiles(root)

        # Print folder variations

        # Files have been removed
        if (len(f) < len(Files) ):
            print("Files have been removed:")
            diff = Files - f

            for path in diff:
                CatFile(path, False)
            print("-------------\n")
            Files = f

        # Files have been added
        if (len(f) > len(Files)):
            print("Files have been added:")
            diff = f - Files

            for path in diff:
                CatFile(path, True)
            print("-------------\n")
            Files = f 

        
        
except KeyboardInterrupt:
    print("\nexit")