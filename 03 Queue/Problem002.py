# Q2. implement queue with function ?


queue = []


# 1. different data types (store)
# 2. muttable
def enqueue(element):
    queue.append(element)


def dequeue():
    if not is_empty():
        queue.pop(0)
    else:
        print("queue is empty")


def is_empty():
    return len(queue) == 0


def peek():
    if not is_empty():
        print(queue[0])
    else:
        print("queue is empty")


def size():
    print(len(queue))


enqueue(10)
enqueue(10)
enqueue(10)
enqueue(10)
enqueue(20)
enqueue(30)
size()
print(is_empty())
print(queue)


# ctrl + enter
# alt + shift + down arrow

# undo = ctrl + z
# redo = ctrl + shift + z


# print(x)
# x = 10  # error
