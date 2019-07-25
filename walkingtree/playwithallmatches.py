#!/usr/bin/python3

## Script to searc nd find all matches
import os

##Define a func that stops searching on 1st match
def findall(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

lookfor = input("What am I looking for? ")
lookwhere = input("What is the path in which I should search? ")

print(findall(lookfor, lookwhere))
