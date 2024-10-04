s = "ABCABCABBCDE"
result = {}

for i in s:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
for k, v in result.items():
    print("{}{},".format(k, v), end="")
