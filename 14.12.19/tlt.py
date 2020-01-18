import turtle as t
t.speed(0)
t.delay()

def draw_square(n):
    for i in range(4):
        t.forward(n)
        t.left(90)

def draw_squares_by_circle(n,m):
    deg = 360 / n
    for i in range(n):
        draw_square(m)
        t.left(deg)


draw_squares_by_circle(10,100)
t.mainloop()