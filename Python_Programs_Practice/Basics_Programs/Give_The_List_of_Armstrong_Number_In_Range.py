num = int(input("Please enter the number: "))

for i in range(num):
    s = i
    l = len(str(i))
    sum1 = 0
    while i != 0:
        r = i % 10
        sum1 = sum1 + (r ** l)
        i = i // 10
    if s == sum1:
        print(s, "is a Armstrong num")
