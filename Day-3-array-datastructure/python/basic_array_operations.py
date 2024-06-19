# Creating an array
arr = [1, 2, 3, 4, 5]

# Accessing elements
print(arr[0])  # Output: 1
print(arr[2])  # Output: 3

# Inserting an element (inefficient in lists, used as a reference)
arr.insert(2, 10)  # Inserts 10 at index 2
print(arr)  # Output: [1, 2, 10, 3, 4, 5]

# Deleting an element
arr.pop(2)  # Removes element at index 2
print(arr)  # Output: [1, 2, 3, 4, 5]

# Searching for an element
index = arr.index(3) if 3 in arr else -1
print(index)  # Output: 2

# Updating an element
arr[1] = 20
print(arr)  # Output: [1, 20, 3, 4, 5]
