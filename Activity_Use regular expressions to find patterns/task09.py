# Pattern to match IPs where each segment is 1 to 3 digits only
pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

# Extract only valid IPs
valid_ip_addresses = re.findall(pattern, log_file)

# Display results
print(valid_ip_addresses)