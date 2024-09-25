# ------------------
# Work-In-Progress Version of "Hangman"
# ------------------
# Practice if elif for loops

def hangman_draw():
	draw_items = ["|", "_", "O", "/", '\\']
	for a in range(10):
		print(draw_items[1], end = "")
	print()
	for b in range(6):
		if b == 0:
			print("|     |", end = "")
			print()
		elif b == 1:
			print("|     O", end = "")
			print()
		elif b == 2:
			print("|    /|\\", end = "")
			print()
		elif b == 3:
			print("|    / \\", end = "")
			print()
		else:
			print(draw_items[0])
	print("Items used")
	print(draw_items)
	
print("H_A_N_G_M_A_N")
print("-------------")

hangman_draw()

question = "What device turns off a TV?"
guessAnswer = "Your answer: "
answer = "remote"

print("""This is a version of "Hangman" game""")
print("Rules: Guess a word, if right You Win, if wrong draw on every wrong answer step-by-step rope, head, hands, body, and legs")
print("The game is over when all body parts are drawn")
print("-----------------------------")

print("Question")
print("--------")
print(question)
print(guessAnswer, end = "")

guess = input()
count = 0
draw_items = ["|", "_", "O", "/", '\\']
while guess != answer and count <= 3:
	for a in range(10):
		print(draw_items[1], end = "")
	print()
	for b in range(6):
		if b == 0:
			print("|     |", end = "")
			print()
		elif b == 1 and count >= 1:
			print("|     O", end = "")
			print()
		elif b == 2 and count >= 2:
			print("|    /|\\", end = "")
			print()
		elif b == 3 and count >= 3:
			print("|    / \\", end = "")
			print()
		else:
			print(draw_items[0])
	if count >= 3:
		print("Game over!")
		break
	count += 1
	print()
	guess = input()
	
if guess == answer:
	print("You win!")