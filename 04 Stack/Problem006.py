# Q6. find time and space complexity of stack when implement wihtin class ?


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        # self.stack.append(element)
        self.stack += [None]
        self.stack[len(self.stack) - 1] = element
        # time complexity = o(1)
        # space complexity = o(1)

    def is_empty(self):
        return len(self.stack) == 0
        #

    def size(self):
        print(len(self.stack))

    def top(self):
        if not self.is_empty():
            print(self.stack[len(self.stack) - 1])

        else:
            print("stack is empty ")

    def pop(self):
        if not self.is_empty():
            print("element deleted :", self.stack.pop())
        else:
            print("stack is underflow")

    def display(self):
        print("length of stack :", len(self.stack))
        print(self.stack)


obj = Stack()
obj.display()


# overall time complexity = o(1)
# space complexity = o(n)
# l1 = [10]
# l1[len(l1)-1] = 50
# print()

# def push(self, element):
#     self.stack = self.stack + [None]
#     self.stack[len(self.stack) - 1] = element
