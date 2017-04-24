#!/usr/bin/env python2 -tt
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def my_interpolation(list_x, list_y, kind="linear"):
    def interpolation(new_x):
        new_y = []
        vals = zip(list_x, list_y)
        i = 0
        
        for x in new_x:
            if kind == "lagrange":
                new_y.append(sum([yk * np.prod([float(x - xi) / (xk - xi) for xi in list_x if xi != xk]) for xk, yk in vals]))
            elif kind == "linear" or kind == "zero":
                while i + 1 < len(list_x) and x >= list_x[i + 1]:
                    i += 1
                
                if i < len(list_x) and (kind == "nearest" or kind == "zero"):
                    new_y.append(list_y[i])
                    
            elif kind == "nearest":


def lagrange_interpolation(list_x, list_y):
    """Funkcja zwraca funkcję będącą interpolacją liniową funkcji podanej w postaci wartości x, oraz y.
        
    Argumenty:
        list_x (list):  Lista wartości x interpolowanej funkcji.
        list_y (list):  Lista wartości y interpolowanej funkcji.
    """
    def interpolation(new_x):
        """Funkcja zwraca listę wartości y, utworzoną na podstawie podanych wartości x.
        
        Argumenty:
            new_x (list):   Lista argumentów funkcji.
        """
        new_y = []
        vals = zip(list_x, list_y)
        
        # Dla każdego nowego punktu x oblicz wartości punktów y interpolacji wielomianowej
        for x in new_x:
            new_y.append(sum([yk * np.prod([float(x - xi) / (xk - xi) for xi in list_x if xi != xk]) for xk, yk in vals]))

        return new_y
    return interpolation


def linear_interpolation(list_x, list_y):
    """Funkcja zwraca funkcję będącą interpolacją liniową funkcji podanej w postaci wartości x, oraz y.
        
    Argumenty:
        list_x (list):  Lista wartości x interpolowanej funkcji.
        list_y (list):  Lista wartości y interpolowanej funkcji.
    """
    def interpolation(new_x):
        """Funkcja zwraca listę wartości y, utworzoną na podstawie podanych wartości x.
        
        Argumenty:
            new_x (list):   Lista argumentów funkcji.
        """
        new_y = []
        i = 0
        for x in new_x:
            while i + 1 < len(list_x) and x > list_x[i + 1]:
                i += 1
            
            # Dodaj punkt znajdujący się pomiędzy dwoma punktami na wykresie, będący współlinowy z tymi punktami
            if i + 1 < len(list_x):
                new_y.append(list_y[i] + (list_y[i + 1] - list_y[i]) / (list_x[i + 1] - list_x[i]) * (x - list_x[i]))
        return new_y
    return interpolation


def nearest_interpolation(list_x, list_y):
    """Funkcja zwraca funkcję będącą interpolacją liniową funkcji podanej w postaci wartości x, oraz y.
        
    Argumenty:
        list_x (list):  Lista wartości x interpolowanej funkcji.
        list_y (list):  Lista wartości y interpolowanej funkcji.
    """
    def interpolation(new_x):
        """Funkcja zwraca listę wartości y, utworzoną na podstawie podanych wartości x.
        
        Argumenty:
            new_x (list):   Lista argumentów funkcji.
        """
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
    """Funkcja zwraca funkcję będącą interpolacją liniową funkcji podanej w postaci wartości x, oraz y.
        
    Argumenty:
        list_x (list):  Lista wartości x interpolowanej funkcji.
        list_y (list):  Lista wartości y interpolowanej funkcji.
    """
    def interpolation(new_x):
        """Funkcja zwraca listę wartości y, utworzoną na podstawie podanych wartości x.
        
        Argumenty:
            new_x (list):   Lista argumentów funkcji.
        """
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
    """Funkcja prezentująca działanie różnych funkcji interpolacji.
    
    Funkcja wyświetla na ekranie wykres funkcji, na której znajdują się: wybrane punkty z danej funkcji, interpolacja liniowa,
    interpolacja Lagrange'a, interpolacja nearest, oraz interpolacja zero.
    """
    # Lista punktów funkcji
    x = np.linspace(1, 10, num=10, endpoint=True)
    y = np.sin(x)
    
    # Interpolacje funkcji
    linear = linear_interpolation(x, y)
    lagr = lagrange_interpolation(x, y)
    nearest = nearest_interpolation(x, y)
    zero = zero_interpolation(x, y)

    # Nowa lista wartości x po której mają zostać rysowane interpolacje
    xnew = np.linspace(1, 10, num=100, endpoint=True)
    
    # Rysuj funkcje na wykresie
    plt.plot(x, y, '.b', markersize=8, label="punkty")
    plt.plot(xnew, linear(xnew), '-r', linewidth=1.5, label="linear")
    plt.plot(xnew, lagr(xnew), '-b', linewidth=1.5, label="Lagrange")
    plt.plot(xnew, nearest(xnew), '-y', linewidth=1.5, label="nearest")
    plt.plot(xnew, zero(xnew), '-c', linewidth=1.5, label="zero")

    # Ustawienie etykiet na osiach współrzędnych
    plt.xlabel(u"Wartości $x$", fontsize=23)
    plt.ylabel(u"Interpolacja wartości $y$", fontsize=23)
    
    # Siatka wykresu
    plt.grid(color=(0.7, 0.8, 1.0), linestyle="solid", )
    
    # Legenda wykresu
    plt.legend(loc="lower left", ncol=1)
    
    plt.show()
    return 0

if __name__ == '__main__':
    main()
