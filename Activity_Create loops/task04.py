#Now, you'll move onto your next task. You'll automate checking whether IP addresses are part of 
#an allow list. You will start with a list of IP addresses from which users have tried to log in, 
#stored in a variable called ip_addresses. Write a for loop that displays the elements of this list 
#one at a time. Use i as the loop variable in the for loop.

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", 
                "192.168.131.147", "192.168.205.12", "192.168.200.48"]

for i in ip_addresses:
    print(i)