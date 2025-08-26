#Q1: File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

# Creating a file which doesn't exist and named orlandocv.pdf

file=open("orlandocv.pdf","w")
file.write("My name is Bucyedusenge Orlando Houston, Tanzanian bor and living in Kigali, Rwanda")

#reading a file

file=open("orlandocv.pdf", "r")
assignment=file.read()
print(assignment)

#modification to a new file version

file=open("orlandocv.pdf","w")
content="Furthmore Orlando is a good person\n"
file.write(content.upper())


# Q2: Error Handling Lab 🧪
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

try:
    filename = input("Please enter a filename: ")   # ask user for input
    file = open(filename, "r")                      # try to open file
    content = file.read()
    print("File content:\n", content)
    file.close()

except FileNotFoundError:
    print("Error: File doesn't exist.")

except IOError:
    print("Error: The file can’t be read.")

finally:
    print("Execution finished.")