#! /usr/local/bin/python3

import os

# CONSTANTS

root_dir = "/Users/juliennicolas/Documents/Work/Billing/Projects/api-permission/internal"

text_to_change = """\tconf := helpers.GetDBConfig()
\tdb, err := helpers.Connect(conf)
\tassert.Nil(t, err)
\tdefer helpers.Close(db)"""

replacing_content = "\tdb := database.GetPool()"

# HELPERS


def open_file(path, mode="r"):
    try:
        f = open(file, mode)
        try:
            content = f.read()
        except IOError:
            print(f"Error: Couldn't read file {file}")
            exit()
    except IOError:
        print(f"Error : couldn't open file {file}")
        exit()

    return f, content


# MAIN
# List all files in input directory and return absolute paths
out_files = list()
for root, dirs, files in os.walk(root_dir):
    for name in files:
        out_files.append(os.path.join(root, name))

# Replace content
for file in out_files:
    print(f"opening {file}")
    f, content = open_file(file)
    f.close()

    print(f"reading {file}")

    if text_to_change in content:
        print("replacing content :")
        print("old : ")
        print(f"{text_to_change}")
        print("new : ")
        print(f"{replacing_content}")
        content = content.replace(text_to_change, replacing_content)

        # rewrite file
        f, _ = open_file(file, "w+")
        f.write(content)
        f.close()
