# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is the first line.\n")
        file.write("This is the second line, and the number is 42.\n")
        file.write("This is the third line.")
except PermissionError:
    print("Error: Could not create the file. Check the file permissions.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("\nThis is the fourth line.")
        file.write("\nThis is the fifth line.")
        file.write("\nThis is the sixth line.")
except PermissionError:
    print("Error: Could not append to the file. Check the file permissions.")
except Exception as e:
    print(f"An error occurred: {e}")