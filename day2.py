from math import sqrt

""" Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number
Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98') """


def exercise1():
    user_list = input(
        "Introduce a sequence of numbers comma separated... ").split(",")
    print(user_list)
    print(tuple(user_list))


print("\nExercise 1: ")
exercise1()

""" Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
 """


class printIO:
    user_input = None

    def getString(self):
        self.user_input = input("Write something... ")

    def printString(self):
        print(self.user_input)


def exercise2():
    print_io = printIO()
    print_io.getString()
    print_io.printString()


print("\n\nExercise 2: ")
exercise2()

""" Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:

100,150,180

The output of the program should be:

18,22,24 """


def exercise3():
    C, H = 50, 30
    user_list = input(
        "Introduce a sequence of numbers comma separated... ").split(",")

    for num in user_list:
        D = int(num)
        print(int(sqrt(2*C*D/H)), end=",")


print("\n\nExercise 3: ")
exercise3()

""" Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i * j.

Note: i=0,1.., X-1; j=0,1,Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] """


def exercise4():
    user_list = input(
        "Provide 2 numbers comma separated... ").split(",")
    X = int(user_list[0])
    Y = int(user_list[1])
    list_dim1 = []

    for i in range(X):
        list_dim2 = []
        for j in range(Y):
            list_dim2.append(i*j)
        list_dim1.append(list_dim2)

    print(list_dim1)


print("\n\nExercise 4: ")
exercise4()

""" Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
bag,hello,without,world
 """

def exercise5():
    user_list = input(
        "Provide a comma separated list of words... ").split(",")
    user_list.sort()
    print(",".join(user_list))

print("\n\nExercise 5: ")
exercise5()

""" Write a program that accepts sequence of lines as input and prints
the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT """

def exercise6():
    user_list = []
    user_input = None

    while (user_input != ""):
        user_input = input("Provide a phrase... ")
        if(user_input == ""):
            break
        user_list.append(user_input)

    for phrase in user_list:
        print(phrase.upper())

print("\n\nExercise 6: ")
exercise6()