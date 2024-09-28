# Q3. implememnt queue without inbuilt function ?queue = []

queue = []


def enqueue(element):
    global queue
    queue += [None]
    queue[len(queue) - 1] = element
    # queue.append(element)


def is_empty():
    return len(queue) == 0


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
enqueue(20)
dequeue()
print(queue)
# x = 10


# def modify():
#     global x
#     x = 20


# print(x)
# modify()
# print(x)


# l1 = []

# for i in range(10, 100, 10):
#     l1.append(i)

# print(l1)

# numebr = 2

# l1 = [10 * 10] + numebr  # l1 = [10][10] ,[10,10] ,[20] ,invalid

# print(l1)

# l1 = [10, 20]
# l3 = [40, 50]
# l2 = l1 + l3
# print(l2)


# concept 1

# name = "radha"
# print(name * 2)
# n = 5
# for i in range(n):
#     print("jd" * i)


# concept 3

# l1 = [10, 20, 30, 40]
# l2 = []
# for i in range(1, len(l1)):
#     l2.append(l1[i])
# print(l2)
