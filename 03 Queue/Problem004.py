# Q4. find time and space complexity ?
queue = []


def enqueue(element):
    global queue
    queue += [None]
    queue[len(queue) - 1] = element
    # queue.append(element)

    # time complexity = o(1)
    # space complexity = o(1)


def is_empty():
    return len(queue) == 0
    # time complexity = o(1)
    # space complexity = o(1)


def dequeue():
    global queue
    if not is_empty():
        new_queue = []
        for i in range(1, len(queue)):
            new_queue.append(queue[i])
        queue = new_queue
        # queue.pop(0)
    else:
        print("queue is empty")
    # time complexity = o(n)
    # space complexity = o(n)


def peek():
    if not is_empty():
        print(queue[0])
    else:
        print("queue is empty")
    # time complexity = o(1)
    # space complexity = o(1)


def size():
    print(len(queue))
    # time complexity = o(1)
    # space complexity = o(1)
