l = [2, 3, 5, 7, 11, 13, 17, 19]
count = True

for i in l:
    for j in range(2, i):
        result = i % j
        if result == 0:
            count = False
if count:
    print(l, "is a prime list")
else:
    print(l, "is not a prime list")
