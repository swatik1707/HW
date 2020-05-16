# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
import simple_draw as sd

point_center = sd.get_point(300, 300)

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

user_angle = input('Выберите фигуру :\n1.3angl\n2.4angl\n3.5angl\n4.6angl\n\n')
if user_angle == '1':
    optiangle(3, point_center, 30, 75, 120, sd.random_color())
elif user_angle == '2':
    optiangle(4, point_center, 30, 75, 90, sd.random_color())
elif user_angle == '3':
    optiangle(5, point_center, 30, 75, 72, sd.random_color())
elif user_angle == '4':
    optiangle(6, point_center, 30, 75, 60, sd.random_color())
else:
    print('Mudak')

sd.pause()

