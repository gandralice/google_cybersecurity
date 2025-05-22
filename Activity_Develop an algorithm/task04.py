#As part of verifying a user's identity in the system, you'll need to check if the user is one of 
#the approved users. Write a conditional statement that verifies if a given username is an element 
#of the list of approved usernames. If it is, display "The user ______ is approved to access the system."
#. Otherwise, display "The user ______ is not approved to access the system.".

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"

if username in approved_users:
    print("The username", username, "is approved to access the system.")
else:
    print("The username", username, "is not approved to access the system.")