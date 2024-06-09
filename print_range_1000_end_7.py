# Print all numbers from 0 to 1000 which end with 7
for num in range(1001):
	if "7" in (str(num))[len(str(num)) - 1]:
		print("i = " + str(num))
