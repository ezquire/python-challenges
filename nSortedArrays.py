def intersection(array):
    intersection = array[0]
    for arr in array:
        i, j = 0, 0;
        current = []
        while i < len(intersection) and j < len(arr):
            if intersection[i] < arr[j]:
                i += 1
            elif intersection[i] > arr[j]:
                j += 1
            else:
                current.append(arr[j])
                i += 1
                j += 1
        intersection = current
    return intersection

array = [[1, 4, 5, 6, 8, 20], [1, 2, 3, 20], [1, 20]]

print(intersection(array))
