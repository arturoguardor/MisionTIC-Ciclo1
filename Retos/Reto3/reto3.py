import operator
def becas(etnia,estrato,ingreso):
    puntaje = (etnia*4 + estrato*5 + ingreso*6)/(15)
    if puntaje >= 20:
        return 1, 0
    else:
        return 0, 1


def seleccion(etnia, estrato, ingreso):
    puntaje_etnicos = {"sin reconocimiento": 1, "afrodescendiente": 12, "indigena": 15, "raizal": 18, "palenquero": 21, "gitano": 24}
    puntaje_estratos = { "1": 30, "2": 24, "3": 18, "4": 6, "5": 1, "6": 1}
    puntaje_ingresos = {"bajo":45,"medio-bajo":27,"medio":21,"medio-alto":12,"alto":0}
    smlv = 908526
    beca, no_Beca = 0, 0
    cont_Becas, cont_Nobecas = 0, 0
        
    if 0 <= int(puntaje_etnicos.get(etnia) or 25) <= 24 and 0 <= int(puntaje_estratos.get(estrato) or 31) <= 30:
        puntaje_etnicos["sin reconocimiento"] = 0
        puntaje_estratos["5"],puntaje_estratos["6"] = 0, 0
        if ingreso > 0 and ingreso < smlv:
            beca, no_Beca = becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["bajo"])
            cont_Becas += beca
            cont_Nobecas += no_Beca
        elif ingreso >= smlv and ingreso < (smlv*2):
            beca, no_Beca = becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["medio-bajo"])
            cont_Becas += beca
            cont_Nobecas += no_Beca
        elif ingreso >= (smlv*2) and ingreso < (smlv*4):
            beca, no_Beca = becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["medio"])
            cont_Becas += beca
            cont_Nobecas += no_Beca
        elif ingreso >= (smlv*4) and ingreso < (smlv*5):
            beca, no_Beca = becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["medio-alto"])
            cont_Becas += beca
            cont_Nobecas += no_Beca
        elif ingreso >= (smlv*5):
            beca, no_Beca = becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["alto"])
            cont_Becas += beca
            cont_Nobecas += no_Beca
        return cont_Becas, cont_Nobecas, etnia, 1, 0
    else:
        return cont_Becas, cont_Nobecas, "sin reconocimiento", 0, 1
    


def run():
    beca, no_Becas, error = 0, 0, 0
    cont_Becas, cont_Nobecas, cont_errores = 0, 0, 0
    etnia = ""
    cont_etnicos = 0
    salida_Etnias = {"sin reconocimiento": 0, "afrodescendiente": 0, "indigena": 0, "raizal": 0, "palenquero": 0, "gitano": 0}
    cant_Candidatos = int(input())
    i = 1
    while i <= cant_Candidatos:
            datos = input().split(sep=",")
            beca, no_Becas, etnia, cont_etnicos, error = seleccion(datos[0].lower(),datos[1],int(datos[2]))
            cont_Becas += beca
            cont_Nobecas += no_Becas
            cont_errores += error
            salida_Etnias[etnia] += cont_etnicos 
            etnia = ""
            i += 1
    print(f"{cont_Becas} {cont_Nobecas} {cont_errores}")
    salida_Etnias = dict(sorted(salida_Etnias.items(), reverse=True))
    salida_Etnias = dict(sorted(salida_Etnias.items(), key=operator.itemgetter(1), reverse=True))
    for key,value in salida_Etnias.items():
        print(key,value)


if __name__ == '__main__':
    run()
    