# For mula A = P(1 + R/100)^t
# compound interest is A-P

p = int(input("Please enter the pure money: "))
r = int(input("Please enter the rate of interest: "))
t = int(input("Please enter the time duration: "))

# A = p* pow((1+(r/100)),t)
A = p * ((1+(r/100))**t)
print(A)

compInt = A-p
print(compInt)