#!/usr/bin/python3
""" Adds all command line argumnents to a list and save in JSON file.

"""
import sys
from os.path import exists

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv[1:]

obj = args
if exists("add_item.json"):
    obj = load_from_json_file("add_item.json")
    obj.extend(args)
save_to_json_file(obj, "add_item.json")
