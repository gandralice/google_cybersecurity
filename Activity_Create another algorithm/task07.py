ip_addresses = " ".join(ip_addresses)    

with open(import_file, "w") as file:
    file.write(ip_addresses)