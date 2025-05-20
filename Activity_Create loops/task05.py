#You are now given a list of IP addresses that are allowed to log in, stored in a variable called 
#allow_list. Write an if statement inside of the for loop. For each IP address in the list of IP 
#addresses from which users have tried to log in, display "IP address is allowed" if it is among 
#the allowed addresses and display "IP address is not allowed" otherwise.

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", 
              "192.168.178.71", "192.168.86.232", "192.168.3.24", 
              "192.168.170.243", "192.168.119.173"]

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", 
                "192.168.131.147", "192.168.205.12", "192.168.200.48"]

for i in ip_addresses:
    if i in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed")