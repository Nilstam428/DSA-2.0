def delete_at_index(arr, index):
    if index < 0 or index >= len(arr):
        return "Index out of bounds"
    
    # Logic: Shift all elements to the left starting from the index
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    
    # In a fixed-size array, we'd null the last spot. 
    # In Python lists, we pop the now-duplicate last element.
    arr.pop() 
    return arr

test_arr = [10, 20, 30, 40, 50]
result = delete_at_index(test_arr, 1)
print(f"Logic Result: {result}")