lst = [1,2,3,4,5,6,1,2,4]
lst.sort()
print(lst)

i = 0
while i < len(lst) - 1:
    if lst[i] == lst[i + 1]:
        lst.pop(i + 1)
    else:
        i += 1

print(lst)


# # use set() to remove also if you want
lst = [10,2,2,3,45,6,6,6]

lst = list(set(lst))
print(lst)
