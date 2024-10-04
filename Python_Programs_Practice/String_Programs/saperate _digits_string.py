s = input("Please Enter your alphanumeric value here: ")
a = ''
b = ''
for i in s:
    if i.isdigit():
        a = a + i
    else:
        b = b + i

print("The int values are = ", int(a))
print("The str values are = ", b)
