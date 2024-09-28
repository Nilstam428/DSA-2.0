# Q7. what is the use of deque from collections module ?

from collections import deque


queue = deque()
queue.append(10)
queue.popleft()  # time complexity = 0(1)
print(queue)


# home work = why time complexity is 0(1)
