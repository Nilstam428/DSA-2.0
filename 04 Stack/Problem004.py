# Q4. implement stack with class ?


# concept 1
# we can make only 2 variable = myth
# class A:
#     def __init__(self,name, age,height ):
#         self.n = name
#         self.age = age


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def is_empty(self):
        return len(self.stack) == 0

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
        print(self.stack)


obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.pop()
# print(obj.is_empty())
# obj.size()
obj.top()
obj.display()
