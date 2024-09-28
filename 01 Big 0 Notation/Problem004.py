# Q4. compare element of list with another list ?


def compare(l1, l2, l3):

    for i in l1:
        for j in l2:
            if i > j:
                l3.append(i)
                print(i)
            else:
                print(j)
    print(l3)


# time complexity = 0(n^2)
# space complexity = o(1)


l1 = [10, 20, 30]
l2 = [5, 15, 25]

compare(l1, l2, l3=[])

# Q which element is gretest ?


# l1 = []
# l1.append("jai")
# print(l1)
