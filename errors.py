#!/usr/bin/env python3

import sys
import os

# EAFP - Easy to ask forgiveness than permission
try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Succeso!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
