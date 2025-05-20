#Now you'll begin to develop the body of the list_to_string() function.In the following code cell, 
#you're provided a list of approved usernames, stored in a variable named username_list. Your task is 
#to complete the body of the list_to_string() function. Recall that the body of a function must be 
#indented. To complete the function body, write a loop that iterates through the elements of the 
#username_list and displays each element. Then, call the function and run the cell to observe what 
#happens.

def list_to_string():
    username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
    for username in username_list:
        print(username)

list_to_string()