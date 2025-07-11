# Reverse a list without using reverse() or slicing

list1 = [1,2,3,4,5]

print(f"Original: {list1}")

for i in range(len(list1) // 2):
    temp = list1[i]
    list1[i] = list1[-i - 1]
    list1[-i - 1] = temp

print(f"Reversed: {list1}")
