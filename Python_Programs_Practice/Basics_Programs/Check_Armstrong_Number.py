num = int(input("Please enter the number: "))

s = num
l = len(str(num))
sum1 = 0

while num != 0:
    r = num % 10
    sum1 = sum1 + (r ** l)
    num = num // 10
if s == sum1:
    print(s, "is a Armstrong num")
else:
    print(s, "is not a Armstrong num")
