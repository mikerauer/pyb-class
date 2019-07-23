#!/usr/bin/python3


ipchk = input("Apply an IP Address: ") # this line prompts user for IP
#ipchk = "192.168.0.1"

if ipchk == "192.168.70.1": # if any data is provided, this will test true
    print("Looks like the IP Address of the Gateway was set: " + ipchk + " This is not recommended")
elif ipchk: #if any data provided returns true
    print("Looks like the IP Address was set: " + ipchk)
else:    
    print("You did not provide input.")


