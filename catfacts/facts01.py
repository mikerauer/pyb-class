#!/usr/bin/python3

#import always go at the top of your code
import requests

def main():
    '''run time code'''

    #create r, which is out requests object
    r = requests.get('http://cat-fact.herokuapp.com/facts')

    # the .json() method will dump JSON string into Pythonic data structures
    # This is much easier then using urllib.request library
    print("\n\n\n")
    print(r.json().get('all'))

main()
