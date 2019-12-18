# 1. Write the following code: a = 1/0;
# try:
#     a = 1/0
# except ZeroDivisionError as e:
#     print("something got wrong")

# 2. Build a corresponding try-except block to avoid exceptions
# try:
#     a = input("press b")
#     if(a == "b"):
#         raise BaseException("Boom!")
# except BaseException as e:
#     print(e.args)

# 3. Is the following code legal?
# Yes

# 4. What exception types can be caught by the following handler?
# ZeroDivisionError, NameError, TypeError

# 5. not clear

# 6. What exceptions can be caught by the following handlers?
# IOError - opening file issue
# ZeroDivisionError - division by zero

# 7+8 +9
def write_words(word):
    f = open("words.txt", "w+")
    f.write(word)
    f.close()
    f = open("words.txt", "r", encoding="utf-8")
    print(f.read())

write_words(input("put some words in Hebrew"))
