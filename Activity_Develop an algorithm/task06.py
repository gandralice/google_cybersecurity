#This task will allow you to build your understanding of list operations for the algorithm that 
#you'll eventually build. It will demonstrate how you can find an index in one list and then use 
#this index to display connected information in another list. First, use the .index() method again to 
#find the index of username in the approved_users and store that in a variable named ind. Then, connect
#ind to the approved_devices and display the device ID located at the index ind. Afterwards, run the 
#cell to observe the result.

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"

ind = approved_users.index(username)
print(approved_devices[ind])