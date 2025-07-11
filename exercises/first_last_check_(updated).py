# Check if the first and last number of a list is the same
# Make a list of a series of numbers and use a flag to break from a for loop
# Additional feature added based on https://pynative.com/python-basic-exercise-for-beginners

def first_last_check():
	lst = [] # define an empty list	
	num = input()	# input function for a string

	str_new = ""	# empty string
	index = 0			# initialize index to 0
	
	while index < len(num) and num[index] != "!": # while index is less than the length of the string and not flagged exit
		if num[index] == "!": # exit flag
			break
		elif num[index] == " ": # when space is encountered 
			lst.append(int(str_new)) # append current string
			str_new = "" # reset str_new to empty string
			index += 1 # increment index by one
			continue # continue to next iteration
		else:
			str_new += num[index]
			#print(f"test:{str_new}")
		
		index += 1 # increment index by one
		if index == (len(num) - 1): # when index == one less than length of num
			str_new += num[index] # string concatenation
			lst.append(int(str_new)) # append integer to lst
			
	print(lst)
	if num[0] == "!": # exit flag
		return "Exit..." # return string
	elif lst[0] == lst[len(lst) - 1]: # otherwise check if first element of the list equals the last
		return True # return True
	else:
		return False # return False

print(first_last_check())
