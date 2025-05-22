#You'll work with a list of approved usernames along with a list of the approved devices assigned to 
#these users. The elements of the two lists are synchronized. In other words, the user at index 0 in 
#approved_users uses the device at index 0 in approved_devices. Later, this will allow you to verify 
#if the username and device ID entered by a user correspond to each other.

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

print(approved_users[0])
print(approved_devices[0])

print(approved_users[3])
print(approved_devices[3])