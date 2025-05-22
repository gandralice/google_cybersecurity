#An employee has left the team and should no longer have access to the system. In the following code 
#cell, you are given the username and device ID of the user to be removed, stored in the variables 
#removed_user and removed_device respectively. Use the .remove() method to remove each of these elements 
#from the corresponding list. Afterwards, display both the approved_users and the approved_devices 
#variables to view the removed users. Run the code and observe the results.

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir", "3rcv4w6"]

removed_user = "tshah"
removed_device = "2ye3lzg"

approved_users.remove(removed_user)
approved_devices.remove(removed_device)

print(approved_users)
print(approved_devices)