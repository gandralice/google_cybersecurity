#There's a new employee joining the organization, and they need to be provided with a username and 
#device ID. In the following code cell, you are given a username and device ID of this new user, stored 
#in the variables new_user and new_device, respectively. Use the .append() method to add these variables 
#to the approved_users and approved_devices respectively. Afterwards, display the approved_users and 
#approved_devices variables to confirm the added information.

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

new_user = "gesparza"
new_device = "3rcv4w6"

approved_users.append(new_user)
approved_devices.append(new_device)

print(approved_users)
print(approved_devices)