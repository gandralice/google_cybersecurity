#Functions can include other components that you've already worked with. The following code cell 
#contains a variation of the alert() function that now uses a for loop to display the alert message 
#multiple times.For this task, call the new alert() function and observe the output.

def alert(): 
    for i in range(3):
        print("Potential security issue. Investigate further.")

alert()