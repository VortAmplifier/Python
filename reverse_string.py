s = "A D F"
new_string = s
index = 0
string_for_reverse = ""

while index < (len(new_string)):
	if new_string[index] == " ":
		if index % 2 == 0:
			print(new_string[:index])
			string_for_reverse += new_string[:index] + " "
			
		new_string = new_string[(index + 1):]
		index = 0
	else:
		index += 1
		if index == (len(new_string) - 1) and (index + 1) % 2 == 0:
			print(new_string[:])
			string_for_reverse += new_string[:]

print(string_for_reverse)
			
index = -1
reversed_string = ""
while index >= -len(string_for_reverse):
	if string_for_reverse[index] == " ":
		reversed_string = reversed_string + string_for_reverse[(index + 1):] + " "
		string_for_reverse = string_for_reverse[:index]
		index = -1
	else:
		index = index - 1
		if index == (-len(string_for_reverse)):
			reversed_string += string_for_reverse
			
print(reversed_string)