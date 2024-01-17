
'''\# Binary Search algorithm (python)


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
'''  # less than is left of the middle number and greater than is right of the middle number in an array
# We can show this with two formulas
user_input = int(input("please tell me a value to look for: "))
array = [3, 4, 5, 6, 7, 8, 9, 11, 16]
low = 0
high = len(array) - 1
# Every time I get a new middle, use this formula
mid = 0
while user_input != array[mid]:
    mid = int((low + high) / 2)
    if user_input > array[mid]:
        low = mid + 1
        print("Your value is present at index: " + str(mid))

        # high = mid - 1 (if it were less than)
    if user_input < array[mid]:
        high = mid - 1
        print("Your value is present at index: " + str(mid))

    if user_input == array[mid]:
        print("Value already found")
        break

array = [6, 4, 9, 0, 2, 8, 11, 16, 19]