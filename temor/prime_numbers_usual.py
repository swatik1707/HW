max_num = 2**13
prime_list = []
for i in range(2,max_num):
    k = 0
    for t in range(2,i):
        if i%t == 0:
            k+=1
        else:
            continue
    if k==0:
        prime_list.append(i)
print('Gotovo!')