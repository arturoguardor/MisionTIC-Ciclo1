
def becas(etnia,estrato,ingreso):
    puntaje = (etnia*4 + estrato*5 + ingreso*6)/(15)
    if puntaje >= 20:
        return 1
    else:
        return 0


def seleccion(etnia, estrato, ingreso):
    puntaje_etnicos = {"sin reconocimiento": 1, "afrodescendiente": 12, "indigena": 15, "raizal": 18, "palenquero": 21, "gitano": 24}
    puntaje_estratos = { "1": 30, "2": 24, "3": 18, "4": 6, "5": 1, "6": 1}
    puntaje_ingresos = {"bajo":45,"medio-bajo":27,"medio":21,"medio-alto":12,"alto":0}
    cont_etnicos = "None"
    smlv = 908526
    cant_Becas = 0
    
    if 0 <= int(puntaje_etnicos.get(etnia) or 25) <= 24 and 0 <= int(puntaje_estratos.get(estrato) or 31) <= 30:
        puntaje_etnicos["sin reconocimiento"] = 0
        puntaje_estratos["5"],puntaje_estratos["6"] = 0,0
        if ingreso > 0 and ingreso < smlv:
            cant_Becas += becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["bajo"])
        elif ingreso >= smlv and ingreso < (smlv*2):
            cant_Becas += becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["medio-bajo"])
        elif ingreso >= (smlv*2) and ingreso < (smlv*4):
            cant_Becas += becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["medio"])
        elif ingreso >= (smlv*4) and ingreso < (smlv*5):
            cant_Becas += becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["medio-alto"])
        elif ingreso >= (smlv*5):
            cant_Becas += becas(puntaje_etnicos[etnia],puntaje_estratos[estrato],puntaje_ingresos["alto"])
        cont_etnicos = etnia

    return cant_Becas, cont_etnicos


def run():
    beca = 0
    salida_Becas = 0
    etnia = ""
    salida_Etnias = {"sin reconocimiento": 0, "afrodescendiente": 0, "indigena": 0, "raizal": 0, "palenquero": 0, "gitano": 0}
    cant_Candidatos = int(input())
    i = 1
    while i <= cant_Candidatos:
            beca,etnia = seleccion(input().lower(),input(),int(input()))
            salida_Becas += beca
            if etnia != "None":
                salida_Etnias[etnia] += 1
            i += 1

    print(salida_Becas)
    for key,value in salida_Etnias.items():
        print(key,value)


if __name__ == '__main__':
    run()