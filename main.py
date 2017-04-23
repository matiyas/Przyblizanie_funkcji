#!/usr/bin/env python2 -tt
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def lagrange_interpolation(list_x, list_y):
    def interpolation(new_x):
        new_y = []
        tmp = zip(list_x, list_y)
        for x in new_x:
            new_y.append(sum([yk * np.prod([float(x - xi) / (xk - xi) for xi in list_x if xi != xk]) for xk, yk in tmp]))

        return new_y
    return interpolation


def linear_interpolation(list_x, list_y):
    def interpolation(new_x):
        new_y = []
        i = 0
        for x in new_x:
            while i + 1 < len(list_x) and x > list_x[i + 1]:
                i += 1
            if i + 1 < len(list_x):
                new_y.append(list_y[i] + (list_y[i + 1] - list_y[i]) / (list_x[i + 1] - list_x[i]) * (x - list_x[i]))
        return new_y
    return interpolation


def nearest_interpolation(list_x, list_y):
    def interpolation(new_x):
        new_y = []
        i = 0
        for x in new_x:
            while i + 1 < len(list_x) and x >= float(list_x[i + 1] - list_x[i]) / 2 + list_x[i]:
                i += 1
            if i < len(list_x):
                new_y.append(list_y[i])
        return new_y
    return interpolation


def zero_interpolation(list_x, list_y):
    def interpolation(new_x):
        new_y = []
        i = 0
        for x in new_x:
            while i + 1 < len(list_x) and x >= list_x[i + 1]:
                i += 1
            if i < len(list_x):
                new_y.append(list_y[i])
        return new_y
    return interpolation


def main():
    x = np.linspace(1, 10, num=10, endpoint=True)
    y = np.sin(x)

    # linear = interp1d(x, y, kind="linear")
    # lagr = lagrange(x, y)
    # nearest = interp1d(x, y, kind="nearest")
    # zero = interp1d(x, y, kind="zero")

    linear = linear_interpolation(x, y)
    lagr = lagrange_interpolation(x, y)
    nearest = nearest_interpolation(x, y)
    zero = zero_interpolation(x, y)

    xnew = np.linspace(1, 10, num=100, endpoint=True)
    plt.plot(x, y, '.b', markersize=8, label="punkty")
    plt.plot(xnew, linear(xnew), '-r', linewidth=1.5, label="linear")
    plt.plot(xnew, lagr(xnew), '-b', linewidth=1.5, label="Lagrange")
    plt.plot(xnew, nearest(xnew), '-y', linewidth=1.5, label="nearest")
    plt.plot(xnew, zero(xnew), '-c', linewidth=1.5, label="zero")

    plt.xlabel(u"Wartości $x$", fontsize=23)
    plt.ylabel(u"Interpolacja wartości $y$", fontsize=23)
    plt.grid(color=(0.7, 0.8, 1.0), linestyle="solid", )
    plt.legend(loc="lower left", ncol=1)
    plt.show()

    return 0

if __name__ == '__main__':
    main()
