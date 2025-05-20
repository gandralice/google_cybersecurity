#The number of approved users has now expanded to five. Rather than storing each of the approved 
#users' usernames individually, it would be more concise to store them in an allow list called 
#approved_list.The in operator in Python can be used to determine whether a given value is an element 
#of a sequence. Using the in operator in a condition can help you check whether a specific username is 
#part of a list of approved usernames. For example, in the code below, username in approved_list 
#evaluates to True if the value of the username variable is included in approved_list.

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "bmoreno"  # Try changing this to a non-approved user

if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")