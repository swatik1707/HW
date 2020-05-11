#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2
M_L_dist = ((550-510)**2 + (370 - 510)**2)**.5
M_P_dist = ((550 - 480)**2 + (370-480)**2)**.5
M_M_dist = 0
distances = {"Moscow ": M_M_dist, "Paris ": M_P_dist, "London ": M_L_dist}



print(distances)




