#!/usr/bin/python3

#import always go at the top of your code
import requests

def main():
    '''run time code'''

    #create r, which is out requests object
    r = requests.get('http://cat-fact.herouapp.com/facts')

    #display the methods available to out new object

    print(dir(r))

main()
