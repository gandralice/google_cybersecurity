#You can also provide a single message about the login attempt. To do this, you can join both 
#conditions into a single conditional statement using a logical operator. This will make the code 
#more concise.Examine the code in the following cell and add the missing operator that would allow 
#for a single message.

approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "bmoreno"  # Try "unknownuser"
organization_hours = True  # Try False

if username in approved_list and organization_hours == True:
    print("Login attempt made by an approved user during organization hours.")
else:
    print("Username not approved or login attempt made outside of organization hours.")