## -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

class Point:   # класс точка
    def __init__(self, point_array):    # конструктор
        self.coord = point_array
        self.dim = len(point_array)
        #self.strfunc = function
        self.func = 0
    def __str__(self):
        return f'point: {self.coord}, func = {self.func:5.8f}'
    def rand(self, dim, r):             # создание случайной точки
        self.dim = dim
        self.coord = np.random.randint(0, r, dim)
        self.func = 0
    def calc(self, function):
        self.func = Func2(function, self)


def Func2(func, point):
    dim = point.dim
    if dim == 2:
        x = point.coord[0]
        y = point.coord[1]
        rez = eval(func, {"x":x, "y" : y})
        return rez
    else:
        return -1

def Func3(func, point):
    dim = point.dim
    if dim == 3:
        x = point.coord[0]
        y = point.coord[1]
        z = point.coord[2]
        rez = eval(func, {"x":x, "y" : y, "z":z})
        return rez
    else:
        return -1


def centr(simplex, n):    # вычисление центра тяжести
    rez = np.zeros(n)
    for i in range(n):
        rez += simplex[i].coord
    return Point(rez/n)


def reflection(x_centr, x_worst, alfa):     # отражение
    rez = (1 + alfa) * x_centr.coord - alfa * x_worst.coord
    return Point(rez)


def extension(x_c, x_r, gamma):         # растяжение
    rez = (1 - gamma) * x_c.coord + gamma * x_r.coord
    return Point(rez)


def squeeze(x_w, x_c, beta):           # сжатие
    rez = beta * x_w.coord + (1 - beta) * x_c.coord
    return Point(rez)


def squeeze_best(x_i, x_b):       # глобальное сжатие к лучшей точке
    rez = x_b.coord + (x_i.coord - x_b.coord) / 2
    return Point(rez)


def nelder_mead(dim, iter_count, function):
    simplex = []
    alfa = 1
    beta = 0.5
    gamma = 2
    r = 10
    
    for i in range(dim + 1):    # создание начального симплекса случайным образом
        x = Point(np.zeros(dim))
        x.rand(dim, r)
        x.calc(function)
        simplex.append(x)
    for j in range(iter_count):
        simplex.sort(key=lambda point: point.func)     # сортировка по значению
        #print("\nsimplex:")
        #for i in range(dim + 1):
           # print(simplex[i].__str__())
        x_best = simplex[0]
        x_worst = simplex[dim]
        x_good = simplex[dim-1]
        x_centr = centr(simplex, dim)
       # print("centr: ", x_centr.__str__())
        x_r = reflection(x_centr, x_worst, alfa)
        x_r.calc(function)
        if x_r.func < x_best.func:
            x_e = extension(x_centr, x_r, gamma)
            x_e.calc(function)
            if x_e.func < x_r.func:
                x_worst = x_e
                simplex[dim] = x_worst
            else:
                x_worst = x_r
                simplex[dim] = x_worst
            continue
        if (x_best.func < x_r.func) and (x_r.func < x_good.func):
            x_worst = x_r
            simplex[dim] = x_worst
            continue
        if (x_good.func < x_r.func) and (x_r.func < x_worst.func):
            x_worst, x_r = x_r, x_worst
        x_s = squeeze(x_worst, x_centr, beta)
        x_s.calc(function)
        if x_s.func < x_worst.func:
            x_worst = x_s
            simplex[dim] = x_worst
        else:
            for i in range(1, dim + 1):
                simplex[i] = squeeze_best(simplex[i], x_best)
    print("answer: ", simplex[i].__str__())
    return simplex[i]

# def main():
#     function = "(1 - x) ** 2 + 100 * (y - x ** 2) ** 2"
#     ans = nelder_mead(2, 50, function)
    
# main()
# input()
