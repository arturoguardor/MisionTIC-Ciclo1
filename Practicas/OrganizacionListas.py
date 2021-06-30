# Funciones de ayuda
def primer_valor(arr):
    return arr[0]
def segundo_valor(arr):
    return arr[1]
#
puntajes=[8,8,15,14,10,16,30,29]
equipos=["Zunior","Aacional","Santa fe","Dep Cali","Millonarios","Tolima","Equidad","America"]
punt_equipo=[]
for i in range(len(equipos)):
    punt_equipo.append([puntajes[i], equipos[i]])
print("Sin Ordenar")
print(punt_equipo)
print("-----------------------------------------")
print("Ordenado")
punt_equipo.sort(key=segundo_valor, reverse=True)
punt_equipo.sort(key=primer_valor, reverse=True)
print("-----------------------------------------")

for elem in punt_equipo:
    print(elem[1], elem[0], sep=" ")