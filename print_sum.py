# A program that prints the sum of the current number and the previous number
current_num = 0
prev_num = 0
sum_num = 0

print("Printing current and previous number sum in a range(10)")

for num in range(10):
	if num == 0:
		print(f"Current Number {current_num} Previous Number {prev_num} Sum {sum_num}")
	else:
		current_num = num
		prev_num = current_num - 1
		sum_num = current_num + prev_num
		print(f"Current Number {current_num} Previous Number {prev_num} Sum {sum_num}")
	