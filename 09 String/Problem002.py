# Q2. Accessing characters in Python String ?


# name = "my name is jai"
# l1 = name.split()
# print(l1)
# print(l1[1])


def access(string, index):
    l1 = string.split()
    if len(l1) < index:
        print("out of range")
    else:
        print(l1[index - 1])


# access("this is your python class", 2)

# time complexity = o(1)
# space complexity = o(1)

# l1 = [10, 20, 30, 40, 50]
# print(l1[3])
