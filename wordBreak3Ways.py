def wordBreakDP(word, dic):
    n = len(word)
    if word in dic:
        return True
    if len(dic) == 0:
        return False
    dp = [False for i in range(n + 1)]
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if dp[j] == True:
                substring = word[j:i]
                if substring in dic:
                    dp[i] = True
                    break
    return dp[-1]

def wordBreakRecursive(word, dic, startIndex=0):
    if word in dic:
        return True
    if len(dic) == 0:
        return false
    if startIndex == len(word):
        return True
    for endIndex in range(startIndex + 1, len(word) + 1):
        if word[startIndex: endIndex] in dic and wordBreakRecursive(word, dic, endIndex):
            return True
    return False
    
def wordBreakMemo(word, dic, startIndex=0, memo=None):
    if word in dic:
        return True
    if len(dic) == 0:
        return False
    if memo == None:
        memo = dict()
    if startIndex in memo:
        return memo[startIndex]
    for endIndex in range(startIndex + 1, len(word) + 1):
        if word[startIndex: endIndex] in dic and wordBreakRecursive(word, dic, endIndex):
            memo[startIndex] = True
            return memo[startIndex]
    memo[startIndex] = False
    return memo[startIndex]

word = "papapapokerface"
dic = {"pa", "poker", "face"}    
    
print(wordBreakDP(word, dic))
print(wordBreakRecursive(word, dic))
print(wordBreakMemo(word, dic))
