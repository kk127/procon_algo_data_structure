from collections import namedtuple
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

Point = namedtuple("Point", "x y")





def koch(n, p1, p2):
    if n == 0:
        return ""
    
    x3 = (2 * p1.x + p2.x) / 3
    y3 = (2 * p1.y + p2.y) / 3
    x4 = (p1.x + 2 * p2.x) / 3
    y4 = (p1.y + 2 * p2.y) / 3

    x5 = (3 * (p1.x + p2.x) + math.sqrt(3) * (p1.y - p2.y)) / 6
    y5 = (math.sqrt(3) * (- p1.x + p2.x) + 3 * (p1.y + p2.y)) / 6

    p3 = Point(x3, y3)
    p4 = Point(x4, y4)
    p5 = Point(x5, y5)

    koch(n-1, p1, p3)
    X.append(x3)
    Y.append(y3)
    koch(n-1, p3, p5)
    X.append(x5)
    Y.append(y5)
    koch(n-1, p5, p4)
    X.append(x4)
    Y.append(y4)
    koch(n-1, p4, p2)


p1 = Point(0, 0)
p2 = Point(100, 0)

print(p1.x, p1.y)

ims = []
fig = plt.figure()

for i in range(1,7):

    X = []
    Y = []
    X.append(0)
    Y.append(0)
    koch(i, p1, p2)
    X.append(100)
    Y.append(0)

    im, = plt.plot(X, Y, "b")
    plt.axes().set_aspect("equal")
    # plt.title("Number of recursions: {}".format(i))
    # plt.xlim((0,100))
    ims.append([im])
    # plt.show()


# ani = animation.ArtistAnimation(fig, ims, interval=200)
ani = animation.ArtistAnimation(fig, ims, interval=1000)
print(ims)
ani.save("test.mp4")

