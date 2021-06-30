
def becas(etnia,estrato,ingreso):
    puntaje = (etnia*4 + estrato*5 + ingreso*6)/(15)
    if puntaje >= 20:
        return 1
    else:
        return 0


def seleccion(cant_Aspirantes,tab_Etnias,tab_Estratos,tab_Ingresos):
    puntaje_etnicos = [0, 0, 12, 15, 18, 21, 24]
    puntaje_estratos = [0, 30, 24, 18, 6, 0, 0]
    puntaje_ingresos = [45, 27, 21, 12, 0, 0]
    smlv = 908526
    etnias_Dias = []
    estratos_Dias = []
    ingresos_Dias = []
    cont_Becas = []
        
    for k in range(7):
        i = 0
        etnias_Dias.append([])
        for j in range(len(tab_Etnias)):
            etnias_Dias[k].append(int(tab_Etnias[i][k]))
            i += 1
    
    for k in range(7):
        i = 0
        estratos_Dias.append([])
        for j in range(len(tab_Estratos)):
            estratos_Dias[k].append(int(tab_Estratos[i][k]))
            i += 1
    
    for k in range(7):
        i = 0
        ingresos_Dias.append([])
        for j in range(len(tab_Ingresos)):
            ingresos_Dias[k].append(int(tab_Ingresos[i][k]))
            i += 1
    
    for k in range(7):
        cont_Becas.append(0)
        for j in range(cant_Aspirantes):
            
            puntaje_etnicos[1], puntaje_estratos[5], puntaje_estratos[6] = 1, 1, 1
            
            try:
                if 0 <= puntaje_etnicos[etnias_Dias[k][j]] <= 24 and 0 <= puntaje_estratos[estratos_Dias[k][j]] <= 30:
                    puntaje_etnicos[1], puntaje_estratos[5], puntaje_estratos[6] = 0, 0, 0
                    
                    if ingresos_Dias[k][j] > 0 and ingresos_Dias[k][j] < smlv:
                        beca = becas(puntaje_etnicos[etnias_Dias[k][j]], puntaje_estratos[estratos_Dias[k][j]], puntaje_ingresos[0])
                        cont_Becas[k] += beca
                    elif ingresos_Dias[k][j] >= smlv and ingresos_Dias[k][j] < (smlv*2):
                        beca = becas(puntaje_etnicos[etnias_Dias[k][j]], puntaje_estratos[estratos_Dias[k][j]], puntaje_ingresos[1])
                        cont_Becas[k] += beca
                    elif ingresos_Dias[k][j] >= (smlv*2) and ingresos_Dias[k][j] < (smlv*4):
                        beca = becas(puntaje_etnicos[etnias_Dias[k][j]], puntaje_estratos[estratos_Dias[k][j]], puntaje_ingresos[2])
                        cont_Becas[k] += beca
                    elif ingresos_Dias[k][j] >= (smlv*4) and ingresos_Dias[k][j] < (smlv*5):
                        beca = becas(puntaje_etnicos[etnias_Dias[k][j]], puntaje_estratos[estratos_Dias[k][j]], puntaje_ingresos[3])
                        cont_Becas[k] += beca
                    elif ingresos_Dias[k][j] >= (smlv*5):
                        beca = becas(puntaje_etnicos[etnias_Dias[k][j]], puntaje_estratos[estratos_Dias[k][j]], puntaje_ingresos[4])
                        cont_Becas[k] += beca
            except:
                continue
    
    return cont_Becas
    

def menor_Asistencia(tab_Etnias):
    contador = []
    asistencia = []
    menor = []
    posicion = []
    baja_Asistencia = [0,0,0,0,0,0]
    
    for k in range(7):
        i = 0
        contador.append([])
        for j in range(len(tab_Etnias)):
            contador[k].append(int(tab_Etnias[i][k]))
            i += 1

    for k in range(len(contador)):
        asistencia.append([])
        for j in range(1,7):
            asistencia[k].append(contador[k].count(j))
    
    for k in range(len(asistencia)):
        menor.append(0)
        posicion.append(0)
        organizado = asistencia[k].copy()
        organizado.sort(reverse=True)
        menor[k] = organizado[0]
        posicion[k] = asistencia[k].index(organizado[0])
        for j in range(len(asistencia[k])):
            baja_Asistencia[j] += asistencia[k][j]
            if asistencia[k][j] != 0:
                if asistencia[k][j]< menor[k] and asistencia[k][j] > 0:
                    menor[k] = asistencia[k][j]
                    posicion[k] = j
    

    organizado2 = baja_Asistencia.copy()
    organizado2.sort(reverse=True)
    menor2 = organizado2[0]
    posicion2 = baja_Asistencia.index(organizado2[0])
    for k in range(len(baja_Asistencia)):
        if baja_Asistencia[k] != 0:
                if baja_Asistencia[k] < menor2 and baja_Asistencia[k] > 0:
                    menor2 = baja_Asistencia[k]
                    posicion2 = k
    
    return posicion, posicion2


def mayor_Asistencia(tab_Etnias):
    contador = []
    asistencia = []
    mayor = []
    posicion = []
    alta_Asistencia = [0,0,0,0,0,0]

    for k in range(7):
        i = 0
        contador.append([])
        for j in range(len(tab_Etnias)):
            contador[k].append(int(tab_Etnias[i][k]))
            i += 1

    for k in range(len(contador)):
        asistencia.append([])
        for j in range(1,7):
            asistencia[k].append(contador[k].count(j))
    
    for k in range(len(asistencia)):
        mayor.append(0)
        posicion.append(0)
        organizado = asistencia[k].copy()
        organizado.sort(reverse=True)
        mayor[k] = organizado[0]
        posicion[k] = asistencia[k].index(organizado[0])
        for j in range(len(asistencia[k])):
            alta_Asistencia[j] += asistencia[k][j]
            if asistencia[k][j] != 0:
                if asistencia[k][j]> mayor[k] and asistencia[k][j] > 0:
                    mayor[k] = asistencia[k][j]
                    posicion[k] = j
        
    organizado2 = alta_Asistencia.copy()
    organizado2.sort(reverse=True)
    mayor2 = organizado2[0]
    posicion2 = alta_Asistencia.index(organizado2[0])
    for k in range(len(alta_Asistencia)):
        if alta_Asistencia[k] != 0:
                if alta_Asistencia[k] > mayor2 and alta_Asistencia[k] > 0:
                    mayor2 = alta_Asistencia[k]
                    posicion2 = k

    return posicion, posicion2


def run():
    salida_Etnias = ["sin reconocimiento", "afrodescendiente", "indigena", "raizal", "palenquero", "gitano"]
    tab_Etnias = []
    tab_Estratos = []
    tab_Ingresos = []

    cant_Aspirantes = int(input())
    for j in range(cant_Aspirantes):
        tab_Etnias.append(input().split(sep=" "))
    for j in range(cant_Aspirantes):
        tab_Estratos.append(input().split(sep=" "))
    for j in range(cant_Aspirantes):
        tab_Ingresos.append(input().split(sep=" "))

    etnias_Menor,etnias_Baja = menor_Asistencia(tab_Etnias)
    
    for j in range(7):
        print(salida_Etnias[etnias_Menor[j]],end="")
        if j != 6:
            print(",",end="")
        else:
            print()
            print(salida_Etnias[etnias_Baja])

    etnias_Menor,etnias_Alta = mayor_Asistencia(tab_Etnias)
    for j in range(7):
        print(salida_Etnias[etnias_Menor[j]],end="")
        if j != 6:
            print(",",end="")
        else:
            print()
            print(salida_Etnias[etnias_Alta])

    lista_Becas = seleccion(cant_Aspirantes,tab_Etnias,tab_Estratos,tab_Ingresos)
    for k in range(len(lista_Becas)):
        print(lista_Becas[k],end="")
        if k != 6:
            print(" ",end="")
        else:
            print()


if __name__ == '__main__':
    run()
