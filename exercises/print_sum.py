# A program that prints the sum of the current number and the previous number
# https://pynative.com/python-basic-exercise-for-beginners/ / Exercise 2
current_num = 0 # declare and initialize variable 
prev_num = 0 # declare and initialize variable
sum_num = 0 # declare and initialize variable 

print("Printing current and previous number sum in a range(10)") # print a message

for num in range(10): # for loop
	if num == 0: # when num = 0
		print(f"Current Number {current_num} Previous Number {prev_num} Sum {sum_num}") # use variables set to 0 for beginning
	else:
		current_num = num # when num > 0 assign num to current_num
		prev_num = current_num - 1 # prev_num previous number
		sum_num = current_num + prev_num # sum previous number and current_num
		print(f"Current Number {current_num} Previous Number {prev_num} Sum {sum_num}") # print a message using f-string
	
