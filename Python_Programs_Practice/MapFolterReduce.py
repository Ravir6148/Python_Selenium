from functools import reduce

data = [1, 2, 3, 4, 5]

doubled_values = list(map(lambda x: x * 2, data))
print("Doubled values:", doubled_values)

even_numbers = list(filter(lambda x: x % 2 == 0, data))
print("Even numbers:", even_numbers)


product = reduce(lambda x, y: x * y, data)
print("Product of all values:", product)

