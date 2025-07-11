# Enter two numbers if product less than 1000 return product otherwise return sum
def mult(num1, num2):
	multipl = num1 * num2
	
	if (num1 * num2) <= 1000:
		return multipl
	else:
		return num1 + num2

def main():
	num1 = int(input("Enter the first number: "))
	num2 = int(input("Enter the second number: "))
	print(mult(num1, num2))

if __name__ == '__main__':
	main()
