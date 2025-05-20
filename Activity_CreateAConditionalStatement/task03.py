#Nothing is displayed when the system is not equal to "OS 2". This is because the condition didn't 
#evaluate to True.It would be beneficial if an alternative message is provided to them when updates 
#are needed.In the following cell, add the appropriate keyword after the first conditional so that 
#it will display a message that conveys that an update is needed when the system is not running OS 2. 

system = "OS 1"

if system == "OS 2":
    print("no update needed")
else:
    print("update needed")
