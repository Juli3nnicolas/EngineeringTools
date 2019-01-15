#! /usr/local/bin/python3

import mistune
import os
from sys import argv, exit

if len(argv) != 3:
	print('Wrong syntax.\n ./RenderMarkDown.py "path/to/file\.mdown" "path/to/destination/file.html"')
	exit()

path = argv[1]
dst_path = argv[2]

try:
	file = open(path, 'r')
	content = file.read()
except IOError as err:
	print(str(err))
	exit()
except TypeError as err:
	print("Error, Wrong source path.")
	print(str(err))
	exit()

html_content = mistune.markdown(content)

try:
	file = open(dst_path, 'w+')
	file.write(html_content)
except IOError as err:
	print("Error, couldn't write file.")
	print(str(err))
except TypeError as err:
	print("Error, wrong destination path.")
	print(str(err))
	exit()

try:
	# Use default browser
	os.system("open " + dst_path)
except:
	print("Error, couldn't open web browser.")
	exit()
