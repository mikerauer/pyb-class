#!/usr/bin/python3

# this library allows us to generate uuis values.

import uuid

howmany= int(input("How many UUIDs should be generated? "))
print("Generatting UUIDs...")

# range is required because an int cannot be looped
for rando in range(howmany):
    print( uuid.uuid4()  )

