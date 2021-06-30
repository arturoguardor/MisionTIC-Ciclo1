import math

area = float(input())
ant_old = int(input())
type_new = input()
area_old = 4800

if ant_old >= 0:
    if type_new == 'a':
        print(max(0, math.ceil((area - area_old * ant_old) / 11400)))
    elif type_new == 'b':
        print(max(0, math.ceil((area - area_old * ant_old) / 12600)))
    elif type_new == 'c':
        print(max(0, math.ceil((area - area_old * ant_old) / 41100)))
    elif type_new == 'd':
        print(max(0, math.ceil((area - area_old * ant_old) / 14700)))
    elif type_new == 'e':
        print(max(0, math.ceil((area - area_old * ant_old) / 38000)))
    else:
        print('error en los datos')
else:
    print('error en los datos')