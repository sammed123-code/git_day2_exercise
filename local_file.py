# Create or write to a local text file

# Specify the file name
file_name = "example.txt"

# Write content to the file
with open(file_name, "w") as file:
    file.write("This is an example of writing to a local text file.\n")
    file.write("You can add more lines as needed.\n")

print(f"File '{file_name}' has been created and written successfully.")