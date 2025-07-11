string1 = input("Enter string: ")
list1 = []
count = 0
new_string = string1
for i in range(len(string1)):
    if string1[i] == " ":
        list1.append(i)
        count += 1

for j in range(count + 1):
    if list1 != []:
        print(new_string[max(list1)+1:] + " ", end = "")
        new_string = string1[:max(list1)]
        list1.pop()
print(new_string, end = "")
    
    
    
