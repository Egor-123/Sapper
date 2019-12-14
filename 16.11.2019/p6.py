# def f(a,b):
#     return a + g(b)
#
# def g(c):
#     return c//2
#
# print(f(2,3))

# def f(s):
#     g = s[:len(s)-1]
#
#     if len(g) == 0:
#         return 1
#
#     return 1 + f(g)

def fact(n):
    if n == 0:
        return 1

    return n * fact(n-1)

print(fact(4))