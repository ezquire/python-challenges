def numberOfRotations(arr):
    count = 0
    while count < len(arr) - 1 and arr[count] < arr[count + 1]: 
        count += 1
    return count + 1 if count + 1 != len(arr) else 0
    
def binarySearch(arr):
    l, r = 0, len(arr) - 1
    while l + 1 < r:
        mid = l + (r - l) >> 1
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid + 1
        elif arr[mid] < arr[r]:
            r = mid - 1
        else:
            l = mid + 1
    return 0

        
            
            
    
            
        
a = [2, 4, 5, 6, 8, 9, 10]
b = [1]
c = [2, 1]
d = [10, 2, 4, 5, 6, 8, 9]

print(binarySearch(a))
print(binarySearch(b))
print(binarySearch(c))
print(binarySearch(d))
