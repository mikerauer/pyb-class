#!/usr/bin/python3

## Script to searc and stop on frst match
import os

##Define a func that stops searching on 1st match
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

lookfor = input("What am I looking for? ")
lookwhere = input("What is the path in which I should search? ")

print(find(lookfor, lookwhere))
