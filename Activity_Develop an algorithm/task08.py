#It would also be helpful for users to receive messages when their username is not approved or 
#their device ID is incorrect.Add to the code by writing an elif statement. This elif statement 
#should run when the username is part of the approved_users but the device_id doesn't match the 
#corresponding device ID in the approved_devices. The statement should also display two messages 
#conveying that information.

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
device_id = "wrongdevice"

ind = approved_users.index(username)

if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)
elif username in approved_users and device_id != approved_devices[ind]:
    print("The user", username, "is approved to access the system, but", device_id, "is not their assigned device.")