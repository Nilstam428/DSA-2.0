# Q2. implement stack with function ?


stack = []


def push(item):
    stack.append(item)


def is_empty():
    if len(stack) == 0:
        return True
    #     print("stack is empty")
    else:
        #     print("stack is not empty")
        return False
    # return len(stack) == 0


def pop():
    if not is_empty():
        stack.pop()
    else:
        print("stack is empty")


def size():
    print(len(stack))


def peek():
    if not is_empty():
        print(stack[-1])
    else:
        print("stack is empty")


push(10)
push(20)
push(30)
pop()
print(is_empty())
size()
peek()
print(stack)

# concept 1


# def add():
#     print(number * 3)


# number = 2
# print(number)
# add()


# print(100 == 10)
