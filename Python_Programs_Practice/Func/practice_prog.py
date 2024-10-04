def sum_marks(mark):
    total_marks = sum(mark)
    total_sub = len(mark)
    average_marks = total_marks / total_sub
    return average_marks


def grade(resul):
    if resul >= 80:
        print("Congratulation You scored grade A")
    elif 60 <= resul < 80:
        print("Congratulation You scored grade B")
    elif 50 <= resul < 60:
        print("Congratulation You scored grade c")
    else:
        print("You scored grade F")


marks = [55, 64, 75, 80, 65]
result = sum_marks(marks)
print("Your total scored marks is", result)

grade(result)


