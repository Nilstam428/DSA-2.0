# Q3. implement stack with function using while loop ?

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


def menu():
    while True:
        print("1. Push")
        print("2. pop")
        print("3. check empty or not")
        print("4. size")
        print("5. top")
        print("6. exit :")

        choice = int(input("enter your choice : "))

        if choice == 1:
            item = input("enter element :")
            push(item)
        elif choice == 2:
            pop()
        elif choice == 3:
            print(is_empty())
        elif choice == 4:
            print("size of stack :")
            size()
        elif choice == 5:
            peek()
        elif choice == 6:
            print("Exiting ....")
            break
        else:
            print("Invalid input")


menu()
