# Create a `with` statement to write to the text file 
with open(import_file, "w") as file:
    # Write `ip_addresses` to the text file
    file.write(ip_addresses)