n = int(input("Please enter the terms of fibonacci: "))

n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter positive value for Fibonacci sequence")
elif n == 1:
    print("The fibonacci sequence of", n, "is", n1)
else:
    print("The fibonacci sequence of", n, "are:")
    while count < n:
        print(n1, end=" ")
        fibonacci = n1 + n2
        n1 = n2
        n2 = fibonacci
        count += 1
