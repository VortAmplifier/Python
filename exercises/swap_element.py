# Swap two elements of a list
# https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
list1 = [23, 65, 19, 90] # define a list1
print(list1) # print list1
pos1 = int(input("Enter position in the list 0, 1, 2 etc")) # input pos1
pos2 = int(input("Enter another position in the list 0, 1, 2 etc")) # input pos2

copy_item_pos1 = list1[pos1] # copy element of list1 at pos1
list1.insert(pos1, list1[pos2]) # insert element at pos1
del list1[pos1 + 1] # delete next element it will be as copy_item_pos1

list1.insert(pos2, copy_item_pos1) # insert item at pos2
del list1[pos2 + 1]                # delete next element it will be as list1[pos2]

print("Modified list") # print modified list        

print(list1) # print list1

