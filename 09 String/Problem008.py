# Q8. how to delete a word from string ?


def deleteChar(string, word):
    l1 = string.split()
    l2 = []
    if word in l1:
        index = l1.index(word)
        print(f"{word} found at {index +1} positon")
        for i in l1:
            if i == word:
                pass
            else:
                l2.append(i)
        string = " ".join(l2)
        print("Updated String :")
        print(string)
    else:
        print(f"{word} not found !")


string = "String is very important for dsa"
word = "very"
deleteChar(string, word)
