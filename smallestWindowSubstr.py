import math

def smallestWindow(S, T):
    shortest = [0, math.inf]
    required = {}
    window = {}
    # Initialize Dictionaries
    for char in T:
        required[char] = required.get(char, 0) + 1
        window[char] = 0
    missingChars = len(window)
    slow = 0
    for fast in range(len(S)):
        key = S[fast]
        if key in window:
            window[key] += 1
            if window[key] == required[key]:
                missingChars -= 1
        while missingChars == 0:
            if fast - slow < shortest[1] - shortest[0]:
                shortest[0] = slow
                shortest[1] = fast
            key = S[slow]
            if key in window:
                window[key] -= 1
                if window[key] < required[key]:
                    missingChars += 1
            slow += 1
    return "No substring found" if shortest[1] == math.inf else search[shortest[0] : shortest[1] + 1]

search = "BBACBDFFACEB"
pattern = "ABCB"

print(smallestWindow(search, pattern))
