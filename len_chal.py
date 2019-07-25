#!/usr/bin/python3
'''
Author: MikeRAuer
script to sort a list by length
'''

def length_list(EXAMPLE_LIST):
    '''Func to sort example_list into sizes'''
    for example_item in EXAMPLE_LIST:
        if len(example_item) >= 10:
            LONG.append(example_item)
        elif len(example_item) < 5:
            SHORT.append(example_item)
        else:
            MEDIUM.append(example_item)

SHORT = []
MEDIUM = []
LONG = []
EXAMPLE_LIST = ['banana', 'blueberry', 'nuts', 'acorns', 'hamburgers']
length_list(EXAMPLE_LIST)
print(SHORT)
print(MEDIUM)
print(LONG)
