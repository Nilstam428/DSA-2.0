# Q5. find error in this code ?
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, element):
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def print(self):
        info = self.head
        while info:
            print(f"{self.head.data} -> ", end=" ")
            info = info.next
        print("None")


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.print()
