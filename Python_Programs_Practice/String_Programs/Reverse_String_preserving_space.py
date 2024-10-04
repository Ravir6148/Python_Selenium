# code for reverse
# Input ='I am ravi'
# Output ='i va rmaI'


s = "I am ravi"
n = len(s)
# Generating a list with zro and holding the space for length of given string
reverse = [0] * n

# 1st preserving the space in list
for i in range(n):
    if s[i] == ' ':
        reverse[i] = ' '
# now adding string where space is not available in list
j = n - 1
for i in range(n):

    if s[i] != ' ':
        # if space is available then just decrease the value of j.
        if reverse[j] == ' ':
            j -= 1
        # If space is not there then add the string char to the list by using the index value.
        reverse[j] = s[i]
        j -= 1
# Converting the list into the string and printing the result.
print(''.join(reverse))
