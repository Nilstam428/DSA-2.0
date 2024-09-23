# Q3. find element in list using binary search ?


def BinarySearch(l1, target):
    start = 0
    end = len(l1) - 1

    while start <= end:
        mid = (start + end) // 2

        if l1[mid] == target:
            return f"{target} found"
        elif l1[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return f"{target} not found"


# time complexity = o(log n)
print(BinarySearch([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 80))


# concept 1
# how to find mid value

# l1=[10,20,30,40,50]

# start = 0
# end = len(l1)-1

# mid = (start+end)//2
