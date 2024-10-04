def greet(name):
    print("Hello", name)


greet("Ravi")


# Multiple Argument

def greet(name1, name2):
    print("Hello", name1, "and", name2)


greet("Ravi", "Amit")


# Func with return

def add_two_num(num1, num2):
    result = num1 + num2
    return result


num1 = 44.5
num2 = 30.4
resul = add_two_num(num1, num2)
print(resul)
