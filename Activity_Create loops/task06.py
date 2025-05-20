#magine now that the information the users are trying to access is restricted, and if an IP address 
#outside the list of allowed IP addresses attempts access, the loop should terminate because further 
#investigation would be needed to assess whether this activity poses a threat. To achieve this, use the 
#break keyword and expand the message that is displayed to the user when their IP address is not in 
#allow_list to provide more specifics. Instead of "IP address is not allowed", display "IP address is 
#not allowed. Further investigation of login activity required".

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", 
              "192.168.178.71", "192.168.86.232", "192.168.3.24", 
              "192.168.170.243", "192.168.119.173"]

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", 
                "192.168.131.147", "192.168.205.12", "192.168.200.48"]

for i in ip_addresses:
    if i in allow_list:
        print("IP address is allowed")
    else:
        print("IP address is not allowed. Further investigation of login activity required")
        break