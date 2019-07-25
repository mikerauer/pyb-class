#!/usr/bin/python3

                        ###explore read###
configfile = open('vlanconfig.cfg', "r")    # create file object in "r"ead mode
print(configfile.read())                    # display file to screen
configfile.close()                          # close file

                    ####explore readlines####

configfile = open("vlanconfig.cfg", "r")    # re-create file object to eplorer new method
configlist = configfile.readlines()         # make list of file lines - .readlines()
for x in configlist:                        # iterate thru configlist
    print(x)

configfile.close()                          # always close file

