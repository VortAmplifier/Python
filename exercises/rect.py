# Create a rectangular drawing w/ stars
def rectangle(num):
	star_space_star = 0
	string = " "
	for star in range(num):
		print("*", end = "")
		
	print()
		
	while star_space_star < num - 2:
		print("*", end = "")
		print(string * (num - 2), end = "")
		print("*\n", end = "")
		star_space_star += 1
	
	for star1 in range(num):
		print("*", end = "")

def main():
	n = int(input())
	rectangle(n)
	
if __name__ == "__main__":
	main()

