# Draw fort / Problem SoftUni
# https://python-book.softuni.org/chapter-06-nested-loops-exam-problems.html
n = int(input("Enter fortress size "))

print("/", end = "")
for exp in range(n // 2):
    print("^", end = "")
print("\\", end = "")
if (n / 2) > 2:
    for underscore in range(n // 2):
        print("_", end = "")
print("/", end = "")
for exp1 in range(n // 2):
    print("^", end = "")
print("\\", end = "")
print()
for row in range(n - 2):
    print("|", end = "")
    if row == (n - 3) and (n / 2) > 2:
        for spaces in range(n // 2 + 1):
            print(" ", end = "")
        for underscore1 in range(n // 2):
            print("_", end = "")
        for spaces1 in range(n // 2 + 1):
            print(" ", end = "")
        print("|")
    else:
        if (n / 2) > 2:
            for spaces1 in range(3 * (n // 2) + 2):
                print(" ", end = "")
        else:
            for spaces1 in range((n // 2) * 2 + 2):
                print(" ", end = "")
        print("|")
print("\\", end = "")
for bottom in range(n // 2):
    print("_", end = "")
print("/", end = "")
if (n / 2) > 2:
    for space2 in range(n // 2):
        print(" ", end = "")
print("\\", end = "")
for bottom1 in range(n // 2):
    print("_", end = "")
print("/")
        
        
           
