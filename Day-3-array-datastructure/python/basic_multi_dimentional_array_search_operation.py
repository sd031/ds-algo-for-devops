# Creating a 2D array
arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(arr_2d[0][1])  # Output: 2
print(arr_2d[2][2])  # Output: 9

# Traversing a 2D array
for row in arr_2d:
    for elem in row:
        print(elem, end=' ')
# Output: 1 2 3 4 5 6 7 8 9
