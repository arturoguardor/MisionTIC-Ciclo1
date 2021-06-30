import math

def list_divide(a, b):
    c = []
    for i in range(len(a)):
        c.append(0) if b[i] == 0 else c.append(a[i] / b[i])
    return c


def get_elem_index(a, elem=None):
    if elem == 'min':
        return min(a), a.index(min(a))
    elif elem == 'max':
        return max(a), a.index(max(a))
    else:
        return elem, a.index(elem)


def main():
    n = 0
    while n < 1:
        initial_data = input().split(' ')
        n, m = int(initial_data[0]), int(initial_data[1])
    acum_ant, acum_a_ant = [], []

    for i in range(n):
        acum_ant.append(0)
        acum_a_ant.append(0)

    area_old = 4800

    for i in range(m):
        ant_old = -1
        while ant_old < 0:
            input_data = input().split(' ')
            depart, area, ant_old, type_new = int(input_data[0]), float(input_data[1]), int(input_data[2]), input_data[3]

        if 0 < depart <= n:
            if type_new == 'a':
                acum_ant[depart - 1]   += max(0, math.ceil((area - area_old * ant_old) / 11400))
                acum_a_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 11400))
            elif type_new == 'b':
                acum_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 12600))
            elif type_new == 'c':
                acum_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 41100))
            elif type_new == 'd':
                acum_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 14700))
            elif type_new == 'e':
                acum_ant[depart - 1] += max(0, math.ceil((area - area_old * ant_old) / 38000))

    min_, index_min = get_elem_index(acum_ant, elem='min')
    max_, index_max = get_elem_index(acum_ant, elem='max')

    print(index_min + 1, min_)
    print(index_max + 1, max_)
    
    porc_a_ant = list_divide(acum_a_ant,acum_ant)
    for i in range(n):
        print('{:} {:.2f}%'.format(i + 1, porc_a_ant[i] * 100))


if __name__ == "__main__":
    main()
