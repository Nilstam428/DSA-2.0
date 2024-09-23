# 1. Linear Time Complexity: Big O(n) Complexity ?

# Q find specific element in list ?


# list1 = [10, 20, 30, 40, 50]


# for i in list1: # i will change 5 times o(5) = 0(1)
#     value = False
#     if i == 35:
#         print("30 found ")
#         value = True
#         break
# if value == False:
#     print("30 not found")


# def findElement(l1, value):
#     if value in l1:
#         print(f"{value} found")
#     else:
#         print(f"{value} not found")  # o(n)


def findElement(l1, value):
    flag = True
    for i in l1:
        if i == value:
            print(f"{value} found")
            flag = False
    if flag == True:
        print(f"{value} not found")  # o(n)


findElement([10, 20, 30, 40, 50, 60, 70], 70)
