""" Write a program which will find all such numbers which are divisible
by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on
a single line. """


def exercise1():
    for num in range(2000, 3201):
        if (num % 7 == 0 and num % 5 != 0):
            print(num, end=",")


print("\nExercise 1: ")
exercise1()

""" Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be:40320 """


def exercise2(num):
    factorial = 1
    for next_num in range(1, num + 1):
        factorial *= next_num
    print(factorial)


print("\n\nExercise 2: ")
exercise2(8)

""" With a given integral number n, write a program to generate
a dictionary that contains (i, i x i) such that is an integral
number between 1 and n (both included). and then the program should
print the dictionary.Suppose the following input is supplied to the program: 8
Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} """


def exercise3(num):
    result = {}
    for next_num in range(1, num + 1):
        result[next_num] = next_num**2
    print(result)

print("\n\nExercise 3: ")
exercise3(8)
