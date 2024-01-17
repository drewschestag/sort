
array = [6, 4, 9, 0, 2, 8, 11, 16, 19]
subArray = [6, 4, 9, 0, 2, 8, 11, 16, 19]

for i in range(0, len(subArray)):
    location = i
    minimum = subArray[i]
    for x in range(0, len(subArray)):
        if minimum > subArray[x]:
            minimum = subArray[x]
            location = x
        # print(minimum) de-comment if needed

    temperal = subArray[i]
    subArray[i] = subArray[location]
    subArray[location] = temperal

print(array)
print(subArray)

