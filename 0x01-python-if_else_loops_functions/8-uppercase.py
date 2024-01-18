#!/usr/bin/python3
def uppercase(str):
    """Function converts a lowercase letter to uppercase."""
    if 'a' <= str <= 'z':
        return chr(ord(str) - ord('a') + ord('A'))
    else:
        return str
