f = open("Demo file.txt", "a+")
f.write("Hi This is demo file. Hellow Ravi, How are you?")
f.close()
g = open("Demo file.txt", "r")
a = g.read()
c = a.count(g.read())
print(c)
