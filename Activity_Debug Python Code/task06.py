import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file
    ip_addresses = file.read()

ip_addresses = split.ip_addresses()

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

print(ip_addresses)

#falta :, split.ip_addresses() errado

import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
    ip_addresses = file.read()

# Supondo que os IPs estejam separados por quebras de linha
ip_addresses = ip_addresses.split("\n")

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

print(ip_addresses)