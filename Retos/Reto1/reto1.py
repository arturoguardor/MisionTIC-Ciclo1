etnia = input().lower()
estrato = input()
ingreso = int(input())

puntaje_etnicos = {"sin reconocimiento": 0, "afrodescendiente": 12, "indigena": 15, "raizal": 18, "palenquero": 21, "gitano": 24}
puntaje_estratos = { "1": 30, "2": 24, "3": 18, "4": 6, "5": 0, "6": 0}

error1 = 0
for key in puntaje_etnicos:
    if etnia == key:
        break
    else:
        error1 += 1

error2 = 0
for key in puntaje_estratos:
    if estrato == key:
        break
    else:
        error2 += 1

error3 = False
if ingreso > 0 and ingreso < 908526:
    ingreso = 45
elif ingreso >= 908526 and ingreso < 1817052:
    ingreso = 27
elif ingreso >= 1817052 and ingreso < 3634104:
    ingreso = 21
elif ingreso >= 3634104 and ingreso < 4542630:
    ingreso = 12
elif ingreso >= 4542630:
    ingreso = 0
else:
    error3 = True

if error1 == 6 or error2 == 6 or error3 == True:
    print("Se presento un error")
else:
    puntaje = (puntaje_etnicos[etnia]*4 + puntaje_estratos[estrato]*5 + ingreso*6)/(15)
    if puntaje >= 20:
        print("El candidato continua en el proceso de seleccion")
    else:
        print("El candidato no continua en el proceso de seleccion")