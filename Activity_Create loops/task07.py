#You'll now complete another task. This involves automating the creation of new employee IDs.You have 
#been asked to create employee IDs for a Sales department, with the criteria that the employee IDs should 
#all be numbers that are unique, divisible by 5, and falling between 5000 and 5150. The employee IDs can 
#include both 5000 and 5150.Write a while loop that generates unique employee IDs for the Sales department 
#by iterating through numbers and displays each ID created.

i = 5000

while i <= 5150:
    if i % 5 == 0:
        print(i)
    i = i + 1