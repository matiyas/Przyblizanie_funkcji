#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange

x = np.linspace(0, 9, num=10, endpoint=True)
y = np.sin(x)
linear = interp1d(x, np.sin(x), kind="linear")
lagr = lagrange(x, np.sin(x))
nearest = interp1d(x, np.sin(x), kind="nearest")
zero = interp1d(x, np.sin(x), kind="zero")

xnew = np.linspace(0, 9, num=100, endpoint=True)
plt.plot(x, y, '.b', markersize=8)
plt.plot(xnew, linear(xnew), '-r')
plt.plot(xnew, lagr(xnew), '-b')
plt.plot(xnew, nearest(xnew), '-y')
plt.plot(xnew, zero(xnew), '-c')

plt.xlabel(u"Wartości $x$", fontsize=23)
plt.ylabel(u"Interpolacja wartości $y$", fontsize=23)
plt.grid(color=(0.7, 0.8, 1.0), linestyle="solid")
plt.legend(("punkty", "linear", "Lagrange", "nearest", "zero"), loc="lower left", ncol=1)
plt.show()
