import math

n =  int(input())
ant_a, ant_b, ant_c, ant_d, ant_e = 0, 0, 0, 0, 0

for i in range(n):
    area = float(input())
    ant_old = int(input())
    type_new = input()
    area_old = 4800

    if ant_old >= 0:
        if type_new == 'a':
            ant_a += max(0, math.ceil((area - area_old * ant_old) / 11400))
        elif type_new == 'b':
            ant_b += max(0, math.ceil((area - area_old * ant_old) / 12600))
        elif type_new == 'c':
            ant_c += max(0, math.ceil((area - area_old * ant_old) / 41100))
        elif type_new == 'd':
            ant_d += max(0, math.ceil((area - area_old * ant_old) / 14700))
        elif type_new == 'e':
            ant_e += max(0, math.ceil((area - area_old * ant_old) / 38000))

ant_tot = ant_a + ant_b + ant_c + ant_d + ant_e

if ant_tot > 0:
    print(ant_tot)
    print('a {:.2f}%'.format(ant_a / ant_tot * 100))
    print('b {:.2f}%'.format(ant_b / ant_tot * 100))
    print('c {:.2f}%'.format(ant_c / ant_tot * 100))
    print('d {:.2f}%'.format(ant_d / ant_tot * 100))
    print('e {:.2f}%'.format(ant_e / ant_tot * 100))
else:
    print(ant_tot)
    print('a 0.00%')
    print('b 0.00%')
    print('c 0.00%')
    print('d 0.00%')
    print('e 0.00%')