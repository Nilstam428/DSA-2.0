class Node:
    def __init__(self, data):
        self.data = data
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

    def delete(self, element):
        if self.head.data == element:
            self.head = self.head.next
            return
        temp = self.head
        prev = None
        while temp and temp.data != element:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
        else:
            print(f"{element} not found")

    def update(self, element, update):
        if self.head.data == element:
            self.head.data = update
            return
        last = self.head
        while last:
            if last.data == element:
                last.data = update
                return
            last = last.next
        print(f"{element} Not found")

    def insertByIndex(self, index, element):
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
        if temp:
            newNode.next = temp.next
            temp.next = newNode
        else:
            print(f"{element} Not found")


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insertAtStart("Radha")
obj.insertByIndex(1, "krishna")
obj.update("Radha", "Radha Rani")
obj.delete(20)
obj.print()
