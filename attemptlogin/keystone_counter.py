#!/usr/bin/python3

loginfail = 0
loginpass = 0
keystone_file = open("attemptlogin/keystone.common.wsgi", "r")
keystone_lines = keystone_file.readlines()


for line in keystone_lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
        ip = line.split()
        print(ip[-1])
    elif "-] Authorization failed" in line:
        loginpass += 1
    else:
        ("EH EH EH you didnt say the magic word")


print("The number of failed login attempts is " + str(loginfail))
print("The number of successful login attempts is " + str(loginpass))

