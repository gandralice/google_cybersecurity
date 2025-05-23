# Create a `with` statement to read in the text file 
with open(import_file, "r") as file:
    # Read the file and store the result in a variable named `text`
    text = file.read()

# Display the contents of `text`
print(text)