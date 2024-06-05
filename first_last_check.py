# Check if the first and last number of a list is the same
# Make a list of a series of numbers and use a flag to break from a for loop
# Additional feature added based on https://pynative.com/python-basic-exercise-for-beginners

def first_last_check():
	lst = []
	num = input()

	for index in range(len(num)):
		if num[index] == "!":
			break
		if num[index] == " ":
			continue
		else:
			str_to_num = int(num[index])
			lst.append(str_to_num)
			
	if num[0] == "!":
		return "Exit..."
	elif lst[0] == lst[len(lst) - 1]:
		return True
	else:
		return False 

print(first_last_check())