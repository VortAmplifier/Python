# A program that prints a sand clock
for r in range(5):
	for space in range(r):
		print(" ", end = '')
	
	for count in range(9-r-r):
		print("#", end = '')

	print()

for sr in range(4):
	for space_s in range(3-sr):
		print(" ", end = '')
	
	for count_s in range(3+sr+sr):
		print("#", end = '')

	print()