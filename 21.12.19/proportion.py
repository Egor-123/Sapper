def solve(a,b,c,d):
    if not a: #a == None
        return c * b / d
    if not b:
        return a * d / c
    if not c:
        return a * d / b
    if not d:
        return c * b / a


print(solve(300, 3.3, 500, None))