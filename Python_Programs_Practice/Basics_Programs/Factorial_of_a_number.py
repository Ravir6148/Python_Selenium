def facto(num):
    if num == 0:
        return 1
    else:
        return num * facto(num - 1)


num = int(input("Please enter your number: "))
result = facto(num)
print("The factorial of", num, "is:", result)
