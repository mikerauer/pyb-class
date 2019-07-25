#!/usr/bin/python3

import subprocess  # changed from prev script
subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interface")
interface = input("Enter an interface, like, ens3: ")
subprocess.call(["ip", "addr", "show", "dev", interface])
subprocess.call(["ip", "route", "show", "dev", interface])
