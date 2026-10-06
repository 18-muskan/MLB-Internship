# File Handling Practice

# Step 1: Create a text file and write data into it

file = open("students.txt", "w")

file.write("Ali\n")
file.write("Sara\n")
file.write("Ahmed\n")

file.close()

print("Data has been written to the file.")


# Step 2: Read and display file contents

file = open("students.txt", "r")

data = file.read()

print("\nFile contents:")
print(data)

file.close()


# Step 3: Append new data to the existing file

file = open("students.txt", "a")

file.write("Muskan\n")

file.close()

print("New data has been added.")


# Step 4: Read the file again to check the new data

file = open("students.txt", "r")

data = file.read()

print("\nUpdated file contents:")
print(data)

file.close()


# Step 5: Count the number of lines in the file

file = open("students.txt", "r")

lines = file.readlines()

file.close()

number_of_lines = len(lines)

print("Number of lines:", number_of_lines)

