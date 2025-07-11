# Manipulating user input text
# https://dailypythonprojects.substack.com/p/python-project-manipulating-user

name = input("Please enter your full name: ") # input prompt
print(f'Your name in uppercase: {name.upper()}') # print output
print(f'Your name in lowercase: {name.lower()}') # print output
string_lst = name.split()

count = 0 # count variable
for s in string_lst: # looping thru the string_lst
    count += len(s) # count the length of each string
    
print(f'Total number of characters (excluding whitespace): {count}')

for l in range(-1, -len(name) - 1, -1):
    print(name[l], end = "")            # print the name in reverse
