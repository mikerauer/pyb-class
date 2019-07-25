#!/usr/bin/python3

## Script to search for pattern match
import os, fnmatch

EXCLUDE = ["/usr", "/home", "/var"]  # dont search locations


##Define a func that stops searching on 1st match
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if root matches exclude list
            dirs[:] = [] # remove the dir list for this iter
            files[:] = [] # remove the file list for this iter
        for name in files:  #always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name, pattern): # if match
                result.append(os.path.join(root, name))
    return result

lookfor = input("What pattern am I looking for? (ex *.txt, *.cfg) ")
lookwhere = input("What is the path in which I should search? ")

print("Results: ", find(lookfor, lookwhere)) # call func
