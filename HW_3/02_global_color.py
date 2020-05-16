# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

point_3angle = sd.get_point(100, 50)
point_4angle = sd.get_point(100,300)
point_6angle = sd.get_point(400, 50)
point_5angle = sd.get_point(400, 300)

def optiangle(angle_count, point, angle, length, step, the_color):
    #sd.background_color = (255, 255, 255)
    if angle_count == 1:
        length = length+0
        angle = angle+2
    if angle_count < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length = length, width=3)
    v1.draw(color=the_color)

    optiangle(angle_count = angle_count-1, point=v1.end_point, angle=angle+step, length = length, step=step, the_color=the_color)

optiangle(3, point_3angle, 30, 75, 120, sd.random_color())
optiangle(4, point_4angle, 30, 75, 90, sd.random_color())
optiangle(5, point_5angle, 30, 75, 72, sd.random_color())
optiangle(6, point_6angle, 30, 75, 60, sd.random_color())

sd.pause()
