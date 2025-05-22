#The next part of the algorithm uses the .index() method to find the index of username in the 
#approved_users and store that index in a variable named ind.When used on a list, the .index() method 
#will return the position of the given value in the list.Add a statement to display ind in the following 
#code cell to explore the value it contains.

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"

ind = approved_users.index(username)
print(ind)