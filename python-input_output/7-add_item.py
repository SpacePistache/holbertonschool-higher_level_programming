#!/usr/bin/python3
"""A module that adds, loads and saves from a previous file"""
import sys
from os.path import exists
from importlib import import_module

save_to_json_file = import_module("5-save_to_json_file").save_to_json_file
load_from_json_file = import_module("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
