#String concatenation is a powerful concept in coding. It allows you to combine multiple strings together
#to form one large string, using the addition operator (+). Sometimes analysts need to merge individual 
#pieces of data into a single string value. In this task, you'll use string concatenation to modify how 
#the list_to_string() function is defined.In the following code cell, you're provided a variable named 
#sum_variable that initially contains an empty string. Your task is to use string concatenation to 
#combine the usernames from the username_list and store the result in sum_variable.In each iteration of 
#the for loop, add the current element of username_list to sum_variable. At the end of the function 
#definition, write a print() statement to display the value of sum_variable at that stage of the process.
#Then, run the cell to call the list_to_string() function and examine its output.

for i in username_list:
    sum_variable = sum_variable + username_list[i]