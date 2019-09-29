def generate(n):
    a = []
    def dfs(s = '', left = 0, right = 0):
        if len(s) == 2 * n:
            a.append(s)
            return
        if left < n:
            dfs( s + '(', left + 1, right)
        if right < left:
            dfs( s + ')', left, right + 1)
    dfs()
    return a

print(generate(0))
print(generate(1))
print(generate(3))
