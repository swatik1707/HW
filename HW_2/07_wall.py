# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = [1500,900]
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# a = 100
# b = 50
# i = 0
# x,u = -800, -800
# y = 0
# while i < 20:
#     x = u = u + 50
#     m = 0
#     while m < 20:
#         bot_left = sd.get_point(x, y)
#         top_righth = sd.get_point(x + 100, y + 50)
#         sd.rectangle(bot_left, top_righth, sd.COLOR_DARK_RED, 6)
#         x += 100
#         m += 1
#         #print('m = ',m)
#     #print('x = ',x)
#     y+=50
#     #print('i = ',i)
#     i+=1
#     #print('y = ',y)
row = 0
brick_x, brick_y = 100, 50
for y in range(0, sd.resolution[1], brick_y):
    row+=1
    for x in range(0, sd.resolution[0], brick_x):
        x0 = x if row%2 else x + brick_x // 2
        left_bottom = sd.get_point(x0,y)
        right_top = sd.get_point(x0 + brick_x, y + brick_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1, color=sd.COLOR_DARK_YELLOW)

sd.pause()
