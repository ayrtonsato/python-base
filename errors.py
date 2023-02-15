#!/usr/bin/env python3

import time
import logging

log = logging.Logger("errors")

def try_open_a_file(filepath, retry = 1) -> list:
    """Tries to open a file, if error retries n times"""
    # EAFP - Easy to ask forgiveness than permission
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines()
        except FileNotFoundError as e:
            log.error("ERRO: %s", str(e))
            time.sleep(1)
        else:
            print("Succeso!")
        finally:
            print("Execute isso sempre!")
    return []

for line in try_open_a_file("names.txt", retry = 5):
    print(line)
