# Assign `import_file` to the name of the text file that contains the security log file
import_file = "login.txt"

# Assign `missing_entry` to a log that was not recorded in the log file
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

# Open file in append mode to add the missing entry
with open(import_file, "a") as file:
    file.write("\n" + missing_entry)  # Add newline before appending

# Read the updated file and store it as `text`
with open(import_file, "r") as file:
    text = file.read()

# Display the contents of `text`
print(text)