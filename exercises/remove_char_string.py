string0 = input("Enter a string: ")
letter = input("Enter a letter to be removed from a string: ")

conv_string = list(string0)

for i in range(len(string0)):
    if string0[i] == letter:
        conv_string.pop(i)
        break
    
new_string = ""
for j in range(len(conv_string)):
    new_string += conv_string[j]

print(new_string)
        

