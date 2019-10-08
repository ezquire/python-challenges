# // Given an immutable array of integers a and an integer size, this array has below invariance:

# // any integer inside subarray with size is unique each other. 
# // for example:
# // A = [1, 2, 5, 6, 4, 13, 50, 17, 6] size = 5
 
# // The question is:

# // implement a function:
# //       boolean canRemove(int[] a, int size, int index);
# // after removing index-th location integer in the given array, if the invariance is still maintained, return true, otherwise return false

# // for above example:
#               0  1  2  3  4  5   6   7   8
# // canRemove([1, 2, 5, 6, 4, 13, 50, 17, 6], 5, 6) -> false
#                     i             r  j

# // canRemove([....0, 1, 2, 3, 6, 13, 5, 50, 17, 6, ... ] 5, 5000 ) -> true
#                      ^            ^  ^
#                      i          5000 j
                                   
                                 
def canRemove(arr, size, index):
    i = max(0, (index - size) + 1)
    j = index + 1
    while j < len(arr):
        if arr[i] == arr[j]:
            return False
        i += 1
        j += 1
    return True;

arr = [1, 2, 5, 6, 4, 13, 50, 17, 6]
size = 5
index = 6

print(canRemove(arr, size, index))
