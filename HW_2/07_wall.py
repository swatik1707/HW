# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

a = 100
b = 50
i = 0
x,u = -800, -800
y = 0
while i < 20:
    x = u = u + 50
    m = 0
    while m < 20:
        bot_left = sd.get_point(x, y)
        top_righth = sd.get_point(x + 100, y + 50)
        sd.rectangle(bot_left, top_righth, sd.COLOR_WHITE, 6)
        x += 100
        m += 1
        print('m = ',m)
    print('x = ',x)
    y+=50
    print('i = ',i)
    i+=1
    print('y = ',y)



sd.pause()
