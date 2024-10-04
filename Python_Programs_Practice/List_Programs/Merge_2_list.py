# List1=[10,20,30,40]  List2=[100,200,300,400]
#
# Expected Output
#
# 10 400
# 20 300
# 30 200
# 40 100

List1 = [10, 20, 30, 40]
List2 = [100, 200, 300, 400]

for x, y in zip(List1[::], List2[::-1]):
    print(x, y)