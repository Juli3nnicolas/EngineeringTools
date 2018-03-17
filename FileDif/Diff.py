#! /usr/bin/python

# Display differences between two text files on stdout (prints nothing if none)
# Returns 0 if no errors are detected, 1 if they aren't the right amount of parameters, 2 file paths are wrong.
# Syntax : Diff file1 file2

from sys import argv, exit
from os import stat


if len(argv) != 3:
    print("Error - wrong number of parameters")
    print("Syntax - dif file1 file2") 
    exit(1)

# Open files
try:
    f1 = open(argv[1], "r")
    f2 = open(argv[2], "r")

except IOError as err: # Python 2
    print(str(err))
    exit(2)
except OSError as err: # Python 3
    print(str(err))
    exit(2)

# Compare file content line-per-line
SEPARATION_SYMBOL = " -|- "
dif_str = ""
for l1 in f1:
    l2 = f2.readline()

    # First comparison in case f1 is longer than f2
    if l1 != l2:
        if l2 != "":
            dif_str += l1[:-1] + SEPARATION_SYMBOL + l2
        else:
            dif_str += l1[:-1] + SEPARATION_SYMBOL + "EOF\n"

# If f2 is longer than f1, append what's more in f2
if stat(argv[2]).st_size > stat(argv[1]).st_size:
    lines = f2.readlines()
    for l in lines:
        dif_str += "EOF" + SEPARATION_SYMBOL + l

# Output dif on stdout
print(dif_str)

# Clean up
f1.close()
f2.close()

exit(0)