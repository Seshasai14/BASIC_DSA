def linear_search(arr, target):
    #Used Enumerate to zip the index and element together to get the index of the element
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1



arr = [1, 3, 5, 7, 9]
target = 10
result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")