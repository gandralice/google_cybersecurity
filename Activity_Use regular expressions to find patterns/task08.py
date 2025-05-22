# Update pattern to allow 1–3 digits in each segment
pattern = r"\d+\.\d+\.\d+\.\d+"

# Extract IP addresses with variable segment lengths
print(re.findall(pattern, log_file))