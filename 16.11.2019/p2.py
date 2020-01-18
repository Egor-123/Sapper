def draw_stairs(a):
    res = ''

    for i in range(a):
        res += i*' ' + 'I\n'
    return res

print(draw_stairs(10))
#return 'I\n I\n  I'