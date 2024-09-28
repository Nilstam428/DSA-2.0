# Q7. what is the use of deque from collections module ?


from collections import deque

stack = deque()
stack.append(70)
stack.append(10)
stack.append(10)
stack.append(80)
stack.popleft()
stack.pop()
print(stack)
# time complexity = o(1)
# space complexity = o(1)


# overall
# time complexity = o(1)
# time complexity = o(n)
