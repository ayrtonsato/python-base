#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota" 
tag: tech
text: 
Anotacao geral sobre carreira de tecnologia

$ notes.py read tech
...
...
"""
__version__ = "0.1.0"
__author__ = "Ayrton Hiroshi Sato"

import sys
import os

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if len(arguments) != 2:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read", "new")
if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    # leitura das notas
    for line in open(filepath):
        title,tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    title = arguments[1] # TODO: tratar exception
    text = [
        f"{title}",
        input("tag: ").strip(),
        input("text:\n").strip(),
    ]
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
