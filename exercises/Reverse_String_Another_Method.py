python_string = "Facebook is social media"
python_string_slice = python_string
string_len = len(python_string_slice)
new_string = ""

for let in range(string_len - 1, -1, -1):
    if python_string_slice[let] == " ":
        print(python_string_slice[let - len(python_string_slice) + 1:])
        new_string += python_string_slice[let - len(python_string_slice) + 1:] + " "
        python_string_slice = python_string_slice[:let]
    elif let == 0:
        print("Python")
        new_string += python_string_slice
    

print("Original string:\n-------------")

print(python_string)

print("Reversed string:")

print(new_string)
