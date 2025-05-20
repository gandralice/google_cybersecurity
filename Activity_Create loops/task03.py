#n this task, a for loop and a while loop will produce similar results, but each is based on a 
#different approach. (In other words, the underlying logic is different in each.) A for loop terminates 
#after a certain number of iterations have completed, whereas a while loop terminates once it reaches 
#a certain condition. In situations where you do not know how many times the specified action should 
#be repeated, while loops are most appropriate.

connection_attempts = 0

while connection_attempts < 3:
    print("Connection could not be established.")
    connection_attempts = connection_attempts + 1
