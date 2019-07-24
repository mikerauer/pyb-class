#!/usr/bin/python3

dnsfile = open("dnsservers.txt")    #openfile
dnslist = dnsfile.readlines()       #create list of lines
for svr in dnslist:                 #loop over lines
    print(svr, end="")               #print and end without a newline
dnsfile.close()                     #close file
