# 1. Create two variables name X and Y.
# 2. Print “BIG” if X is bigger than Y .
# 3. Print “small” if X is smaller than Y.
x = 10
y = 20
if(x > y):
    print("Big")
elif(x < y):
    print("small")


# 1. Run a “for” loop 5 times.
# 2. Print iteration number every time.
for i in range(5):
    print(i)

# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable.
# 3. print the season name accordingly:
x = 3
if(x == 1):
    print("suumer")
elif (x == 2):
    print("winter")
elif (x == 3):
    print("fall")
elif (x == 4):
    print("spring")

# 1. how many times will the following loop run?
# # 2. what will be printed last?
print("The loop will run 10 times")
print("56 will print last")

# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number the
# user entered.

def getphonenumber():
    number = input("please provide your phone number..")
    print("phone number is: " + number)


# Write a program with the following:
# 1. Method named printHello() that prints the word “hello”.
# 2. Method named calculate() which adds 5+3.2 and prints the
# result.
def printHello():
    print("hello")
def calculate():
    print("5 + 3")

# Write a program with the following:
# 1. Method that receive your name and prints it.
# 2. Method that receive a number, divide it by 2, and prints the
# result.

def getmyname():
    myName = input("provide your name")
    print(myName)


def dividenumber():
    number = input("provide a number")
    print(number / 2 )


# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the
# sum.
# 2. Method that receive two Strings, add space between them,
# and return one spaced string.
def dividenumber():
    numberone = input("provide a number")
    numbertwo = input("provide a number")
    return  numberone + numbertwo

def spacestring():
    stringone = input("provide a string")
    stringtwo = input("provide a string")
    return  stringone + " " + stringtwo


# Create a nested for loop (loop inside another loop) to create
# a pyramid shape:
simbool = "#"
for i in range (5):
    print(simbool)
    simbool = simbool + "#"


# Write a program with the following:
# 1. Method that gets a number from the user (using input).
# 2. Method that receive the number from the first method, and
# computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)


def getnumber():
    numberinput = input("Please insert a number...")
    return numberinput


def calculate():
    number = getnumber()
    div = 1
    sum = 0
    for digit in number:
        sum = sum + int(digit)
        div = div * 10
    print(sum)


calculate()
getphonenumber()
print(spacestring())