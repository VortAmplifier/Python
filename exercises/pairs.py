A = [1, 2, 3, 4, 5]
index = 0
lst1 = []
for i in A:
    for j in range(index + 1, len(A)):
        tup = (i, A[j])
        lst1.append(tup)
    index += 1

print(lst1)

# This code generates pairs such as (1,2),(1,3),(1,4)...(4,5) and stores them in a list
