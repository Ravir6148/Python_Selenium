s = input("Please enter the string: ")

s1 = s.split()
l = len(s1) * -1

reverse_ord = ""

for i in range(-1, l - 1, -1):
    reverse_ord = reverse_ord + s1[i] + " "

print(reverse_ord)
