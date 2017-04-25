#!/usr/bin/env python2 -tt
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def interpolate(list_x, list_y, kind):
    """Funkcja zwraca funkcję będącą interpolacją, typu podanego w argumencie, funkcji podanej w postaci wartości x, oraz y.
        
    Argumenty:
        list_x (list):  Lista wartości x interpolowanej funkcji.
        list_y (list):  Lista wartości y interpolowanej funkcji.
        kind (str):     Typ interpolacji funkcji (linear, lagrange, nearest, zero).

    Przykład użycia:
        x = numpy.linspace(0, 10, num=10)
        y = numpy.sin(x)
        linear = interpolate(x, y, "linear")
        new_x = numpy.linspace(0, 10, num=100)
        linear(new_x)

    """
    def interpolation(new_x):
        """Funkcja zwraca listę wartości y, utworzoną na podstawie podanych wartości x.
        
        Argumenty:
            new_x (list):   Lista argumentów funkcji.
        """
        new_y = []
        i = 0

        if kind == "linear":
            for x in new_x:
                # Szukam wartości x interpolowanej funkcji, równej lub większej od nowej wartości x
                while i + 1 < len(list_x) and x > list_x[i + 1]:
                    i += 1
            
                # Oblicz wartość y, która tworzy z nową wartością x punkt współliniowy do dwóch kolejnych punktów interpolowanej funkcji
                if i + 1 < len(list_x):
                    new_y.append(list_y[i] + (list_y[i + 1] - list_y[i]) / (list_x[i + 1] - list_x[i]) * (x - list_x[i]))

        if kind == "lagrange":
            # Dla każdego nowego punktu x oblicz wartości punktów y interpolacji wielomianowej
            for x in new_x:
                new_y.append(sum([yk * np.prod([float(x - xi) / (xk - xi) for xi in list_x if xi != xk])
                             for xk, yk in zip(list_x, list_y)]))
        
        if kind == "nearest":
            for x in new_x:
                # Szukam wartości x, znajdującego się pomiędzy dwoma kolejnymi punktami interpolowanej funkcji, większego od nowej wartości x
                while i + 1 < len(list_x) and x >= float(list_x[i + 1] - list_x[i]) / 2 + list_x[i]:
                    i += 1
                if i < len(list_x):
                    new_y.append(list_y[i])
        
        if kind == "zero":
            for x in new_x:
                # Szukam wartości x interpolowanej funkcji, większej od nowej wartości x
                while i + 1 < len(list_x) and x >= list_x[i + 1]:
                    i += 1
                if i < len(list_x):
                    new_y.append(list_y[i])

        return new_y
    return interpolation


def main():
    """Funkcja prezentująca działanie różnych funkcji interpolacji.
    
    Funkcja wyświetla na ekranie wykres funkcji, na której znajdują się: wybrane punkty z danej funkcji, interpolacja liniowa,interpolacja 
    Lagrange'a, interpolacja nearest, oraz interpolacja zero.
    """
    # Lista punktów funkcji
    x = np.linspace(0, 9, num=10, endpoint=True)
    y = np.sin(x)
    
    # Interpolacje funkcji
    linear = interpolate(x, y, "linear")
    lagr = interpolate(x, y, "lagrange")
    nearest = interpolate(x, y, "nearest")
    zero = interpolate(x, y, "zero")

    # Nowa lista wartości x po której mają zostać rysowane interpolacje
    xnew = np.linspace(0, 9, num=100, endpoint=True)
    
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
