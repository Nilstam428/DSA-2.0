arr=[10,20,30,40,50]
print("Original array:",arr)
print("Length of the array:",len(arr))
print(arr[0])  # 10
print(arr[4])  # 50
arr.append(60)
print("Updated array:",arr)

# 4️⃣ Memory Representation (DSA View)
# Index:   0   1   2   3   4
# Value:  10  20  30  40  50

# Creating Arrays in Python
# a) Static-like initialization
l1=[1,2,3,4,5]
print("Static-like initialized array:",l1)

# b) Dynamic initialization
l2=[]
for i in range(5):
    l2.append(i*10)
print("Dynamically initialized array:",l2)
l3=list(range(1,11,2))
print("Array using list and range:",l3)


# c) Using list comprehension
l4=[x**2 for x in range(1,6)]
print("Array using list comprehension:",l4)

# Traversing an Array
for i in range(len(arr)):
    print(f"Element at index {i} is {arr[i]}")

for i in arr:
    print(i)
