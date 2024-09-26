# Q7. how to delete element of string ?


# steps
# 1. charchter exist or not
# 2. if exist = delete
# 3. display


def deleteChar(string, char):
    l1 = list(string)
    l2 = []
    if char in l1:
        index = l1.index(char)
        print(f"{char} found at {index +1} positon")
        for i in l1:
            if i == char:
                pass
            else:
                l2.append(i)
        string = "".join(l2)
        print("Updated String :")
        print(string)
    else:
        print(f"{char} not found !")


string = "String is very important for dsa"
char = "v"
deleteChar(string, char)
