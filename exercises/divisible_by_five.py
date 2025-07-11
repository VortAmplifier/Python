# Display numbers divisible by 5 from a list
# https://pynative.com/python-basic-exercise-for-beginners/ / Exercise 6
lst = [10, 20, 33, 46, 55] # define a list

def divisible_by_five(): # define a function
	print(f"Given list is {lst}") # print list
	print("Divisible by 5") # print message
	
	for index in range(len(lst)): # for loop iterate over a range of indices
		if lst[index] % 5 == 0: # check if divisible by 5
			print(lst[index]) # print elements of the list

def main(): # define main function
	divisible_by_five() # call a function

if __name__ == "__main__": # standolone program or a module check
	main() # call main function
	
