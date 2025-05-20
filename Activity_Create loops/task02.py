#The range() function can also take in a variable. To repeat a specified action a certain number 
#of times, you can first assign an integer value to a variable. Then, you can pass that variable 
#into the range() function within a for loop.In your code that displays a network message connection, 
#incorporate a variable called connection_attempts. Assign the positive integer of your choice as the 
#value of that variable and fill in the missing variable in the iterative statement.

connection_attempts = 5

for i in range(connection_attempts):
    print("Connection could not be established.")