#Task 1: Read a File and Handle Errors

file_name = "sample.txt"
try:
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. /n")

#Task 2: Write and Append Data to a File

initial_text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(initial_text)
print("Data successfully written to output.txt.")

append_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write("\n" + append_text)
print("Data successfully appended.")

print("Final content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())




