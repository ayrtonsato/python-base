#!/usr/bin/env python3

import sys
import os

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...") # Race Condition
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

# LBYL - Look Before You Leap
if len(names) >= 3:
    print(names[2])
else:
    print("Missing name in the list")
    sys.exit(1)
