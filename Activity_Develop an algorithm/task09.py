#In this task, you'll complete your algorithm by developing a function that uses some of the code you've 
#written in earlier tasks. This will automate the login process.There are multiple ways to use 
#conditionals to automate the login process. In the following code, a nested conditional is used to 
#achieve the goals of the algorithm. There is a conditional statement inside of another conditional 
#statement. The outer conditional handles the case when the username is approved and the case when 
#username is not approved. The inner conditional, which is placed inside the first if statement, handles 
#the case when the username is approved and the device_id is correct, as well as the case when the 
#username is approved and the device_id is incorrect.To complete this task, you must define a function 
#named login that takes in two parameters, username and device_id. Afterwards, call the function and pass
#in different username and device ID combinations to experiment and observe the function's behavior.

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

def login(username, device_id):
    if username in approved_users:
        print("The user", username, "is approved to access the system.")
        ind = approved_users.index(username)
        if device_id == approved_devices[ind]:
            print(device_id, "is the assigned device for", username)
        else:
            print(device_id, "is not their assigned device.")
    else:
        print("The username", username, "is not approved to access the system.")

login("sgilmore", "4n482ts")
login("sgilmore", "wrongdevice")
login("unauthorized", "0000000")