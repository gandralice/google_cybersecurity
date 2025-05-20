#This setup is still not ideal. If the variable system contains a random string or integer, the 
#conditional above would still display update needed.To improve the conditional, you will need to add 
#the elif keyword. In the following cell, you will add two elif statements after the if statement, to 
#create the final code. The first elif statement will display update needed if system is "OS 1". The 
#second elif statement will display the same message, if system is "OS 3". Complete the second elif 
#statement, and then run the cell with the variable system set to a different string each time. Observe 
#what happens when each operating system is running. Also try assigning the system variable to some 
#strings other than "OS 1", "OS 2", and "OS 3" (for example "OS 4").

system = "OS 3"  # Try "OS 1", "OS 2", "OS 3", "OS 4"

if system == "OS 2":
    print("no update needed")
elif system == "OS 1":
    print("update needed")
elif system == "OS 3":
    print("update needed")