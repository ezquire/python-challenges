from collections import Counter

def jobOffers(scores, lowerLimits, upperLimits):
    scores.sort()
    res = [0]*len(lowerLimits)
    i = 0
    j = scores.index(lowerLimits[0])
    while j < len(scores) and i < len(lowerLimits):
        if scores[j] <= upperLimits[i]:
            res[i] += 1
            j += 1
        if scores[j] > upperLimits[i]:
            i += 1
            if i < len(lowerLimits):
                while scores[j] < lowerLimits[i]:
                    j += 1
    return res

scores = [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
lowerLimits = [2, 6]
upperLimits = [4, 9]
expected = [5, 4]

actual = jobOffers(scores, lowerLimits, upperLimits)

print("expected:", expected)
print("acutal:", actual)
