#!/usr/bin/python

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append('dns') # adds dns to EOL
protoa.append('dns') # adds dns to EOL
print(proto)
proto2 = [22,80,443,53] # list common ports
proto.extend(proto2) #pass proto2 as arguement to ext method
print(proto)
protoa.append(proto2) #pass proto2 as arguement to ext method
print(protoa)

#.insert added to lists
proto.insert(2,proto2) #inserts list proto2 into index 2
print(proto)
