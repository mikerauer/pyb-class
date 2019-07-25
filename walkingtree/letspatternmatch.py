#!/usr/bin/python3

## Script to search for pattern match
import os, fnmatch

##Define a func that stops searching on 1st match
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

lookfor = input("What pattern am I looking for? (ex *.txt, *.cfg) ")
lookwhere = input("What is the path in which I should search? ")

print(find(lookfor, lookwhere))
