#!usr/bin/python3

##list including local lan connection info
my_list = ["192.168.0.5", 5060, "UP"]

##prints IP address
print("The first item in the list (ip):" + my_list[0])

##prints port
print("The second item in the list (port):" + str(my_list[1]))

##prints state
print("The last item in the list (state):" + my_list[2])

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

##print using f string
#print(f"When I SSH into IP Address {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]} or {new_list[2]}.")

##print using .format unpacking
print("When I SSH into IP Address {3} or {4} I am unable to ping ports {0}, {1}, or {2}".format(*new_list))


