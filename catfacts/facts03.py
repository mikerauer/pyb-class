#!/usr/bin/python3

#import always go at the top of your code
import requests

def main():
    '''run time code'''

    #create r, which is out requests object
    r = requests.get('http://cat-fact.herokuapp.com/facts')

    #catfact is our iterable -- that just means it will take on the values found within
    #r.json()["all"], one after the next -- which happens to be a dictionary
    #the code with the loop, says, "from that single dictionary"

    #print the value associated with text
    for catfact in r.json()['all']:
        print(catfact.get('text')) #the .get() method returns none if key not found

main()
