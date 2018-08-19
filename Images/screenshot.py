#! /usr/local/bin/python3

import pyautogui
from sys import argv, exit
from os import path

if len(argv) != 3:
    print("Syntax error, the first parameter must be a path to the saving location and the second must be a file name")
    print("python3 screenshot.py /my/path my_name.<image format>")
    print("Supported image formats are pmg and jpg")
    exit(-1)

PATH = argv[1]
NAME = argv[2]

if len(NAME.split('.')) < 2:
    print("Error, wrong file format. Your file name must be something like 'myfile.png'")
    exit(-2)

if NAME.split('.')[-1] not in {"png", "jpg"}:
    print("Error, unsupported image format. \nYour format must be one of png or jpg.")
    exit(-3)



pic = pyautogui.screenshot()
pic.save(path.join(PATH, NAME))