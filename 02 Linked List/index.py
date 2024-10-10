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
            print(f"{info.data} -> ", end=" ")
            info = info.next
        print("None")

    def insertAtStart(self, element):
        newNode = Node(element)
        newNode.next = self.head
        self.head = newNode

    def delete(self, key):
        if self.head and self.head.data == key:
            self.head = self.head.next
            return
        temp = self.head
        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
        else:
            print(f"{key} Not found in linked list")

    def update(self, key, updateValue):
        if self.head and self.head.data == key:
            self.head.data = updateValue
            return
        last = self.head
        while last.next:
            if last.next.data == key:
                last.next.data = updateValue
                return
            last = last.next
        print(f"{key} Not found !")

    def insertAtIndex(self, index, element):
        newNode = Node(element)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        temp = self.head
        current_index = 0

        while temp and current_index < index - 1:
            temp = temp.next
            current_index += 1

        if temp is None:
            print(f"Index {index} is out of range.")
            return
        newNode.next = temp.next
        temp = self.head
        temp.next = newNode


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insertAtIndex(3, "jp")
obj.insertAtIndex(2, 50)
obj.print()


# steps 1. anaconda install
# steps 2. juptyter notebook
