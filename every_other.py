def every_other(s):
    new = ""
    i = 0
    while( i < len(s)):
        new += s[i]
        i += 2
    return new

print(every_other("hous"))
