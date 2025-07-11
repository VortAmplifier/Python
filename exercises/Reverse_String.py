# reverse() method reverses a list
# #Signifies a comment
# Example string: "Python is great" print "great is Python"

enter_string = input("Enter string: ") # assign string to enter_string variable

def reverseString(enter_string):
    split_word = enter_string.split() # Split the words from a string

    split_word.reverse() # Reverse the list split_word and permanently changed it
    
    for word in split_word: # for loop to loop through words
        print(word, end = ' ') # print the word on every loop cycle

reverseString(enter_string) # call the function reverseString with an argument a string
