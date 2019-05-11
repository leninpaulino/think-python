import turtle

bob = turtle.Turtle()
print(bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    polygon(t, r, 360)


def arc(t, r, angle):
    polygon(t, r, 360/angle)


arc(bob, 1, 15)





turtle.mainloop()
