#Writing code that is readable and concise is a best practice in programming.The conditional above 
#can be written more concisely.In the following cell, use a logical operator to combine the two elif 
#statements from the previous setup into one elif statement.

system = "OS 1"

if system == "OS 2":
    print("no update needed")
elif system == "OS 1" or system == "OS 3":
    print("update needed")