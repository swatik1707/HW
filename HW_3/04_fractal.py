# -*- coding: utf-8 -*-

import simple_draw as sd


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
root_point = sd.get_point(300, 20)

def draw_branches(root_point,angle,length,step):
    if length < .5:
        return
    v_root = sd.get_vector(root_point, angle,length)
    v_root.draw()
    v_branch = sd.get_vector(v_root.end_point, angle+step, v_root.length*(sd.random_number(80,88)*0.01))
    v_branch.draw()
    v_bb1 = sd.get_vector(v_branch.end_point, angle+step+sd.random_number(18,42),v_branch.length*(sd.random_number(80,88)*0.01))
    v_bb1.draw()
    v_bb2 = sd.get_vector(v_branch.end_point, angle+step-sd.random_number(18,42),v_branch.length*(sd.random_number(80,88)*0.01))
    v_bb2.draw()
    draw_branches(v_bb1.end_point, v_bb1.angle+sd.random_number(18,42), v_bb1.length*(sd.random_number(80,88)*0.01), step=step+sd.random_number(5,10))
    draw_branches(v_bb2.end_point, v_bb2.angle - sd.random_number(18,42), v_bb2.length*(sd.random_number(80, 88) * 0.01), step=step + sd.random_number(5, 10))
    # v_branch1 = sd.get_vector(v_root.end_point, (angle + sd.random_number(18, 43)), (length * (sd.random_number(6,10)*0.1)))
    # v_branch1.draw()
    # v_branch2 = sd.get_vector(v_root.end_point, (angle - sd.random_number(18, 43)), (length * (sd.random_number(6,10)*0.1)))
    # v_branch2.draw()
    # draw_branches(v_branch1.end_point, (v_branch1.angle + sd.random_number(18, 43)), (v_branch1.length * (sd.random_number(6,10)*0.1)))
    # draw_branches(v_branch2.end_point, (v_branch2.angle - sd.random_number(18, 43)), (v_branch2.length * (sd.random_number(6,10)*0.1)))

for delta in range(-70, 71, sd.random_number(5,15)):
    draw_branches(root_point,90,90,step=delta)



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


