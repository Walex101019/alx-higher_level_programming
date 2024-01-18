#!/usr/bin/python3
def uppercase(str):
    """Function checks for uppercase characters."""
    if ord(str) >= 65 and ord(str) <= 90:
        return True
    else:
        return False
