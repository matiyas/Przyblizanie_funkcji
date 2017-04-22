#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange


x = np.arange(0, 10)
y = np.sin(x)
l1 = plt.plot(x, y, marker='.', color='b', markersize=12, linestyle='None')

linear = interp1d(x, np.sin(x), kind="linear")
x = np.arange(0, 10, 0.1)
lagrange = lagrange(x, np.sin(x))
nearest = interp1d(x, np.sin(x), kind="nearest")
zero = interp1d(x, np.sin(x), kind="zero")

plt.plot(x, linear(x))
plt.plot(x, lagrange(x))
plt.plot(x, nearest(x))
plt.plot(x, zero(x))

plt.xlabel(u"Wartości $x$", fontsize=23)
plt.ylabel(u"Interpolacja wartości $y$", fontsize=23)
plt.grid(color=(0.7, 0.8, 1.0), linestyle="solid")
plt.legend((l1, linear, lagrange, nearest, zero), ("punkty", "linear", "Lagrange", "nearest", "zero"), loc="lower left", ncol=1)
plt.show()
