#!/usr/bin/python3

'''
Author: MikeRAuer
Return list of interfaces with IP and MAC address
'''

import netifaces

def IP_Address():
    '''Returns IP for a specfied interface'''
    try:
        i = input("Enter Interface you are looking for an IP for: ")
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:
        print('Thats not a valid interface')

def MAC_Address():
    '''Returns MAC for a specfied interface'''
    try:
        i = input("Enter Interface you are looking for an MAC for: ")
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
    except:
        print('Thats not a valid interface')

print(netifaces.interfaces())

for i in netifaces.interfaces():
    try:
        print('\n****** Details of Interface - ' + i + ' ********')
        print("MAC: ", end='')  # prints label
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])  #prints MAC Address
        print("IP: ", end='')  # prints label
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])  #prints IP Address
    except:
        print('Could not collect adapter info')  #print error

IP_Address()
MAC_Address()
