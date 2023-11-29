#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file
"""

import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# check if filename exists
if os.path.exists(filename):
    args_list = list(load_from_json_file(filename))
else:
    args_list = []

args_length = len(argv)
i = 1

while i < args_length:
    args_list.append(argv[i])
    i += 1

save_to_json_file(args_list, filename)
