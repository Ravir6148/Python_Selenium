n = int(input("Please enter the number in range of 1<=n>=100: "))
b = n
a = n % 2
if a != 0:
    print("Wired")
elif a == 0:
    if b >= 2 and b < 5:
        print("Not Wired")
    elif b >= 6 and b < 20:
        print("Wired")
    elif b > 20:
        print("Not Wired")