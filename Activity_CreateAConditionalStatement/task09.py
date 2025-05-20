#The following cell assembles the code from the previous tasks. It includes the conditional 
#statement that checks if a user is on the allow list and the conditional statement that checks 
#if the user logged in during organization hours.Run the cell below a few times. Each time, enter 
#a different combination of values for username and organization_hours to observe how that affects 
#the output.

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "bmoreno"
organization_hours = True

if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")

if organization_hours:
    print("Login attempt made during organization hours.")
else:
    print("Login attempt made outside of organization hours.")