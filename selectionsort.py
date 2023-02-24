x = [2, 5, -3, 11, 13, 4]
new_list = []

a = 0
b = 0
for n in x:
    if n < a:
        a = n
        new_list.append(a)
        x.remove(a)
    elif n < b:
        b = n
        new_list.append(b)
        x.remove(b)


print(new_list)
print(x)