from random import randint


class Point:   # класс точка
    def __init__(self, x, y, z):    # конструктор
        self.x = x
        self.y = y
        self.z = z
        self.func = self.x ** 2 + self.y ** 2 + self.z ** 2
    def rand(self, r):             # создание случайной точки
        self.x = randint(0, r)
        self.y = randint(0, r)
        self.z = randint(0, r)
        self.func = self.x ** 2 + self.y ** 2 + self.z ** 2
    def print_point(self):
        print("(", self.x, ",", self.y, ",", self.z, ")", "f =", self.func)


def centr(simplex, n):    # вычисление центра тяжести
    x = y = z = 0
    for i in range(n):
        x += simplex[i].x
        y += simplex[i].y
        z += simplex[i].z
    return Point(x/n, y/n, z/n)


def centr2(best, good):
    x = y = z = 0
    x = (best.x + good.x) / 2
    y = (best.y + good.y) / 2
    z = (best.z + good.z) / 2
    return Point(x, y, z)


def reflection(x_centr, x_worst, alfa):     # отражение
    x = (1 + alfa) * x_centr.x - alfa * x_worst.x
    y = (1 + alfa) * x_centr.y - alfa * x_worst.y
    z = (1 + alfa) * x_centr.z - alfa * x_worst.z
    return Point(x, y, z)


def extension(x_c, x_r, gamma):         # растяжение
    x = (1 - gamma) * x_c.x + gamma * x_r.x
    y = (1 - gamma) * x_c.y + gamma * x_r.y
    z = (1 - gamma) * x_c.z + gamma * x_r.z
    return Point(x, y, z)


def squeeze(x_w, x_c, beta):           # сжатие
    x = beta * x_w.x + (1 - beta) * x_c.x
    y = beta * x_w.y + (1 - beta) * x_c.y
    z = beta * x_w.z + (1 - beta) * x_c.z
    return Point(x, y, z)


def squeeze_best(x_i, x_b):       # глобальное сжатие к лучшей точке
    x = x_b.x + (x_i.x - x_b.x) / 2
    y = x_b.y + (x_i.y - x_b.y) / 2
    z = x_b.z + (x_i.z - x_b.z) / 2
    return Point(x, y, z)


def main():
    simplex = []
    n = 3
    alfa = 1
    beta = 0.5
    gamma = 2
    for i in range(n+1):    # создание начального симплекса случайным образом
        x = Point(0, 0, 0)
        x.rand(5)
        simplex.append(x)
    for j in range(30):
        simplex.sort(key=lambda point: point.func)     # сортировка по значению
        print("\nsimplex:")
        for i in range(n + 1):
            simplex[i].print_point()
        x_best = simplex[0]
        x_worst = simplex[n]
        x_good = simplex[n-1]
        x_centr = centr(simplex, n)
        # x_centr = centr2(x_best, x_good)
        print("centr: ")
        x_centr.print_point()
        x_r = reflection(x_centr, x_worst, alfa)
        if x_r.func < x_best.func:
            x_e = extension(x_centr, x_r, gamma)
            if x_e.func < x_r.func:
                x_worst = x_e
                simplex[n] = x_worst
            else:
                x_worst = x_r
                simplex[n] = x_worst
            continue
        if (x_best.func < x_r.func) and (x_r.func < x_good.func):
            x_worst = x_r
            simplex[n] = x_worst
            continue
        if (x_good.func < x_r.func) and (x_r.func < x_worst.func):
            x_worst, x_r = x_r, x_worst
        x_s = squeeze(x_worst, x_centr, beta)
        if x_s.func < x_worst.func:
            x_worst = x_s
            simplex[n] = x_worst
        else:
            for i in range(1, n+1):
                simplex[i] = squeeze_best(simplex[i], x_best)
    print("answer: ")
    simplex[0].print_point()


main()
input()
