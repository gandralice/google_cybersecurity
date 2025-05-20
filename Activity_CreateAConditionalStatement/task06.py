#Now you'll move on to the next part of your work. You've been asked to investigate login attempts 
#to a specific device. Only approved users should log on to this device.You'll start with two authorized 
#users, stored in the variables approved_user1 and approved_user2. You'll need to write a conditional 
#statement that compares those variables to a third variable, username. This will be the username of a 
#specific user trying to log in.

approved_user1 = "elarson"
approved_user2 = "bmoreno"

username = "bmoreno"

if username == approved_user1 or username == approved_user2:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")