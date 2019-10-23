def dutchFlag(arr):
    r = 0
    b = len(arr) - 1
    i = 0
    while i <= b:
        if arr[i] == 'R':
            arr[i], arr[r] = arr[r], arr[i]
            i += 1
            r += 1
        elif arr[i] == 'G':
            i += 1
        else:
            arr[i], arr[b] = arr[b], arr[i]
            b -= 1
    return arr

balls = ['G', 'B', 'G', 'G', 'R', 'B', 'R', 'G']

print(dutchFlag(balls))
