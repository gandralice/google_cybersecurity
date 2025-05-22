#Your next step in creating the algorithm is to determine if a username and device ID correspond. To 
#do this, write a conditional that checks if the username is an element of the approved_devices and 
#if the device_id stored at the same index as username matches the device_id entered. You'll use the 
#logical operator and to connect the two conditions. When both conditions evaluate to True, display a 
#message that the username is approved and another message that the user has their assigned device.

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
device_id = "4n482ts"

ind = approved_users.index(username)

if username in approved_users and device_id == approved_devices[ind]:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)