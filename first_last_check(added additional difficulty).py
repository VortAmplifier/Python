# Check if the first and last number of a list is the same
# Make a list of a series of numbers and use a flag to break from a for loop
# Additional feature added based on https://pynative.com/python-basic-exercise-for-beginners / Exercise 5
# This version works with single digit numbers only
# Purpose: practice conditionals and loops, list indexing

def first_last_check(): # define function first_last_check
	lst = [] # define empty string
	num = input() # input a string

	for index in range(len(num)): # for loop with range 0 to length of string num
		if num[index] == "!": # define a stop flag
			break # break from the loop once encountered	
		elif num[index] == " ":	# when space is encountered
			continue # continue to the next iteration
		else: # otherwise 
			str_to_num = int(num[index]) # convert to integer item in the string
			lst.append(str_to_num) # append to end of lst
			
	if num[0] == "!": # flag to exit	
		return "Exit..." # return a string
	elif lst[0] == lst[len(lst) - 1]: # check first and last element for equality
		return True # return True
	else: # otherwise
		return False # return false

print(first_last_check())
