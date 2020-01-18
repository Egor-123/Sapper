def take(a,n):
    res = []
    if n > len(a):
        return a
    for i in range(n):
        res.append(a[i])
    return res


print(take([0,1,2,3,4,5,6,7], 10))