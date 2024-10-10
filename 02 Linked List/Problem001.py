# Q1. what is single linked list ?

# circuler queue is your home work


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, element):
        new_node = Node(element)
        # data = 30 ,next = None
        # (data= 10 ,next = (data= 20, next = None))

        if self.head is None:  # true or false

            self.head = new_node
            return
        last = self.head
        while last.next:  # true
            last = last.next
            # last = data = 20 ,next = None
        last.next = new_node
        # self.head (data= 10 ,next = (data= 20, next = (data = 30 ,next = none)))

    def display(self):
        info = self.head
        while info:
            print(f"{info.data} -> ", end=" ")
            info = info.next
        print("None")

    def insertAtStart(self, element):
        # self.head = data = 10 , next(data = 20, next(data = 30 ,next = none))
        new_node = Node(element)
        # data = "Radha" ,next(data = 10 , next(data = 20, next(data = 30 ,next = none))
        new_node.next = self.head
        self.head = new_node

    def delete(self, element):
        # element = 20
        if self.head.data == element:
            self.head = self.head.next
            return

        # Radha ->  10 ->  20 ->  30 ->  None
        temp = self.head
        prev = None

        while temp and temp.data != element:
            prev = temp
            # prev =  10 ->  20 ->  30 ->  None
            temp = temp.next
            # temp =  20 ->  30 ->  None

        if temp:
            prev.next = temp.next
            # 10 ->  30 ->  None
        else:
            print(f"{element} does not exist")

    def update(self, element, update):

        if self.head.data == element:
            self.head.data = update
            return
        temp = self.head
        while temp.next:
            if temp.data == element:
                temp.data = update
                return
            temp = temp.next
        print(f"{element} not found")


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insertAtStart("Radha")
obj.delete(20)
obj.update("Radha", "Radha Rani")
obj.update(10, "jd")
obj.display()


# concept 1

# empty,None = falsy value


# concept 2


# class A:
#     def __init__(self, name):
#         self.name = name

#     def method1(self):
#         print("method")

#     def info(self):
#         print("info")


# obj = A("Radha")
# obj.info()
# obj.method1()
# print(obj.name)
