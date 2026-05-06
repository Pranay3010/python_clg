list1 = [1,2,3,4,1,5,2,4,6]
list1.sort()
print(list1)

i = 0
while i < len(list1):
    j = i + 1
    while j < len(list1):
        if list1[i] == list1[j]:
            list1.pop(j)   
        else:
            j += 1
    i += 1

print(list1)