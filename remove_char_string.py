# A program that removes certain characters from a given string includes a function
# https://pynative.com/python-basic-exercise-for-beginners/ / Exercise 4
def remove_chars(string, n): # define a function remove_chars that accepts two arguments string and a number
	new_string = string[n:] # Use string slicing
	
	return new_string # return new string
	
print(remove_chars("pynative", 2)) # test the function
