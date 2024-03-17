# This is parts inventory program written in Python

class Menu:
	def __init__(self):											# __init__ method gets called on instantiating the object later in main function
		print('Enter choice')									# lines 5 to 11 are print statements showing the menu overview			
		print('------------')
		print('1. Insert')
		print('2. Search')
		print('3. Update')
		print('4. Print')
		print('------------')
	
	def enterChoice(self):
		choice = int(input("Enter choice: "))	# assign return value from input to choice (int value casted)
		return choice													# return choice selection
		
class Product:															# defining class Product
	def __init__(self, pnumber, pname):				# __init__ function 
		self.pnumber = pnumber									# pnumber product number
		self.pname = pname											# pname product name
		self.next = None												# next initiated to None

class ProductLL:														# Product Linked List
	def __init__(self):												# __init__ method gets called on ProductLL instantiation
		self.head = None												# self.head initially None
		
	def insert(self, pnumber, pname):					# insert head -> node1 -> node2
		new_node = Product(pnumber, pname)			# instantiating a new node
		if self.head is None:										# when at the beginning self.head is None	
			self.head = new_node									# assign self.head new_node
		else: 																	# if self.head already assigned node
			current_node = self.head							# current_node assigned self.head
			while current_node.next is not None:	# while current_node.next is not None but "points" to a node
				current_node = current_node.next		# loop until current_node is None which means end of the linked list reached so ready to append a new node
			current_node.next = new_node					# append a new node to the end of the list
			
	def printInventory(self):									# function that prints inventory
		current_node = self.head								# assign self.head to current_node that will be the first product in the linked list to print
		# count = 0
		while current_node is not None:					# while current_node is not None
			print('Product#: ', end = '') 			  #	print Product#: and end the print statement with empty string or no space or newline
			print(current_node.pnumber)						# print product number		
			print('ProductName: ', end = '')			# print ProductName and end the print statement with empty string or no space or newline
			print(current_node.pname)							# print product name
			current_node = current_node.next			# traverse through the next node and in the while condition check to see if it is None which means the end of the link list is reached
			
# main function starts here
def main():		
	menu = Menu()
	productLL = ProductLL()																						# product linked list
	
	select = menu.enterChoice() 																			# assign the choice as an int to variable select
	
	if select == 1:
		productNumber = int(input('Enter product number: '))
		productName = input('Enter product name: ')
		productLL.insert(productNumber, productName)										# call productLL method insert
		flag = input('Do you wish to continue (Y/N): ')
		while flag.lower() != 'n':
			if flag.lower() == 'y':
				productNumber = int(input('Enter product number: '))
				productName = input('Enter product name: ')
				productLL.insert(productNumber, productName)								# call productLL method insert
				flag = input('Do you wish to continue (Y/N): ')
			else:
				print('Invalid choice')
	
	productLL.printInventory()																				# print inventory

if __name__ == '__main__':
	main()