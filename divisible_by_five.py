# Display numbers divisible by 5 from a list
# https://pynative.com/python-basic-exercise-for-beginners/ / Exercise 6
lst = [10, 20, 33, 46, 55]

def divisible_by_five():
	print(f"Given list is {lst}")
	print("Divisible by 5")
	
	for index in range(len(lst)):
		if lst[index] % 5 == 0:
			print(lst[index])

def main():
	divisible_by_five()

if __name__ == "__main__":
	main()
	