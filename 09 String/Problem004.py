# Q4. write a program to Check word in string ?


def checkString(string, word):
    l1 = string.split()
    if word in l1:
        print(f"{word} found ")
    else:
        print("not found")


string = "my name is jai and i am 20 years old"
word = "years"
checkString(string, word)

# time complexity = o(n)
# space complexity = o(1)


# l1 = [10, 20, 30, 40, 50]
# print(10 in l1)
