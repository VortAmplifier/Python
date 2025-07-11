# Enter values and place them in a list
# Merge strings from two lists into a third list
# Program is Work-In-Progress as of 6/8/2024

string1 = input()
string2 = input()

lst1 = []
lst2 = []

for index in range(len(string1)):
	if string1[index] == " ":
		continue
	else:
		lst1.append(string1[index])
		
for index in range(len(string2)):
	if string2[index] == " ":
		continue
	else:
		lst2.append(string2[index])
		
print(f"List one: {lst1}")
print(f"List two: {lst2}")

lst3 = []

if len(lst1) > len(lst2):
	for index in range(len(lst1)):
		while index <= (len(lst2) - 1):
			lst3.append(lst1[index] + lst2[index])
	lst3.append(lst1[len(string1) - 1])

if len(lst2) > len(lst1):
	for index in range(len(lst2)):
		while index <= (len(lst2) - 1):
			lst3.append(lst1[index] + lst2[index])
	lst3.append(lst2[len(lst2) - 1])

if len(lst1) == len(lst2):
	for index in range(len(lst1)):
		lst3.append(lst1[index] + lst2[index])

print(lst3)

