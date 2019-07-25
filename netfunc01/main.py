#!/usr/bin/python3

# func to push commands

def commandpush(devicecmd):         #devicecmd==list
    for coffeetime in devicecmd.keys():
        print('\nHandshake. .. ... connecting with ' + coffeetime )
        for mycmds in devicecmd[coffeetime]:        #we'll learn to write code that connects to devices here
            print('Attempting to send command --> ' + mycmds )
            #we'll learn to write code that send cmds to device here

# func interate thru ips

def devicereboot(ips):
    for ip in ips:
        print('Connecting to.. ' + ip)
        print('REBOOTING NOW!')


# start our main script

def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.2":["interface eth1/1", "shutdown"]}

    print("Welcome to the network device command pusher")       #welcome message

    ##get data set
    print("\nData set found")         # replace with func call that reads in data file

    ##run
    commandpush(work2do)                # call func to push commands to devices
    devicereboot(work2do.keys())


# call our main func

main()





