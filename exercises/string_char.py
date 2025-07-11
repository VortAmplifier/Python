# Print characters from a string that are present at an even index number
# https://pynative.com/python-basic-exercise-for-beginners/ / Exercise 3
str = input("Original String is  ") # input function, enter a string

for index in range(len(str)): # for loop 
	if index % 2 == 0: # test even number
		print(str[index]) # print result
