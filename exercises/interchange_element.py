# A program to interchange the first and last elements of a list
# https://www.geeksforgeeks.org/python-list-exercise/#

list1 = [12, 35, 9, 56, 24] # list1

print("Original list: ") # Original list 
print(list1)             # print list1

copy_last = list1[len(list1) - 1] # copy last element of list1
copy_first = list1[0]      # copy first element of list1
list1.pop()                # pop last element of list1

list1.append(copy_first)   # append copy of first element to list1
del list1[0]               # delete first element
list1.insert(0, copy_last) # Insert at position 0 last element of original list

print("Modified list")  # Print
print(list1) # Print list

