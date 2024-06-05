# Print characters from a string that are present at an even index number
str = input("Original String is  ")

for index in range(len(str)):
	if index % 2 == 0:
		print(str[index])