#In this final task, you'll modify the code you wrote previously to improve the readability of the 
#output.This time, in the definition of the list_to_string() function, add a comma and a space (", ") 
#after each username. This will prevent all the usernames from running into each other in the output. 
#Adding a comma helps clearly separate one username from the next in the output. Adding a space following 
#the comma as an additional separator between one username and the next makes it easier to read the output.
#Then, call the function and run the cell to observe the output.

def list_to_string():
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
    sum_variable = ""

    for i in username_list:
        sum_variable = sum_variable + i

    print(sum_variable)

list_to_string()