
'''
JSON
Es un formato que almacena información estructurada y se utiliza principalmente 
para transferir datos entre un servidor y un cliente.
Un objeto JSON comienza y termina con llaves {}. 
Puede tener dos o más pares de claves/valor dentro, con una coma para separarlos. 
Así mismo, cada key es seguida por dos puntos para distinguirla del valor.

Ejemplo: {"ciudad":"Nueva York", "país":"Estados Unidos"}

Aquí tenemos dos pares de clave:valor: 
ciudad y país son las claves; 
Nueva York y Estados Unidos son los valores.

'''
#[{nombre:ccc, edad:22, correo:xxxx},{nombre:ccc, edad:22, correo:xxxx},{nombre:ccc, edad:22, correo:xxxx}]
#Ejercicio 1. Crear un archivo Json

import json
def ejercicio1():
    base_de_datos = []
    for i in range(3):
        persona={}
        name=input("Ingrese nombre: ")
        age=input("Ingrese edad: ")
        email=input("Ingrese correo: ")
        persona["Nombre"]=name
        persona["Edad"]=age
        persona["Correo"]=email
        base_de_datos.append(persona)
    print(base_de_datos)
    #print(base_de_datos[0]["Nombre"])

    with open("contactos.json", mode="w",encoding="utf-8") as archivo:
        json.dump(base_de_datos,archivo)
        print("Archivo exportado")

#ejercicio1()

#Ahora leemos el archivo ya generado
def ejemplo2():
    with open("contactos.json", mode="r",encoding="utf-8") as archivo:
        contacto = json.load(archivo)
        print("Archivo cargado con éxito")
        print(contacto)
    
#ejemplo2()

#Menú de opciones
import os
creada=0
def menu():
    ruta="G:\Mi unidad\Mision TIC 2022\Ciclo 1 - Fundamentos de Programación\Practicas\S19"
    if os.path.isfile(ruta):
        creada=True
    else:
        creada=False
    print(f"Valor de creada ruta {creada} ")
    while True:
        opciones=("1. Adicionar\n2. Buscar\n3. Eliminar\n4. Listar\n5. Salir")
        print(opciones)
        opcion=int(input("Digite su opción: "))
        if opcion == 1:
            adicionar(creada)
            creada=True
        elif opcion == 2:
            if creada:
                buscar()
            else:
                print("Archivo no creado, debe crearlo")
        elif opcion == 3:
            if creada:
                eliminar()
            else:
                print("Archivo no creado, debe crearlo")
            
        elif opcion == 4:
            if creada:
                listar()
            else:
                print("Archivo no creado, debe crearlo")
        else:
            break
    
def adicionar(creada):
    if creada:
        with open("contactosMenu.json","r") as archivo:
            try:
                base_de_datos=json.load(archivo)
            except :
                print("Archivo vacio")
                base_de_datos=[]
    else:
        base_de_datos=[]
    print(f"Creada de la funcion adicionar {creada}")
    
    cant=int(input("Digite cantidad de contactos a añadir: "))
    for i in range(cant):
        persona={}
        nombre=input("Digite nombre: ")
        cc = input("Digite cédula: ")
        persona["Nombre"] = nombre
        persona["Cedula"] = cc
        base_de_datos.append(persona)
    
    with open("contactosMenu.json","w") as archivo:
        json.dump(base_de_datos, archivo)
        print("Registro agregado")
    
def buscar():
    try:
        sw=False
        dato=input("Digite cédula a buscar: ")
        with open("contactosMenu.json","r") as archivo:
            contacto=json.load(archivo)
            
        for c in contacto:
            if dato in c["Cedula"]:
                print(c["Nombre"])
                sw = True
                break
                
        if sw == False:
            print("Cédula no encontrada")
    except :
        print("Archivo vacio")

def eliminar():
    try:
        sw=False
        dato=input("Digite cédula a eliminar: ")
        with open("contactosMenu.json","r") as archivo:
            contacto=json.load(archivo)

            for i in range(len(contacto)):
                if dato in contacto[i]["Cedula"]:
                    contacto.pop(i)
                    print("Registro eliminado")
                    sw=True
                    break
        if sw:
            with open("contactosMenu.json","w") as archivo:
                json.dump(contacto,archivo)
        else:
            print("Cédula no encontrada")
    except:
        print("Archivo vacio")
                
def listar():
    try:
        with open("contactosMenu.json","r") as archivo:
            contacto=json.load(archivo)
            
            for c in contacto:
                print(f"Nombre: {c['Nombre']} Cédula: {c['Cedula']} ")
    except:
        print("Archivo vacio")
    
            

menu()




"""
Este es el Archivo Generado por el ejemplo que sigue:
datos.json
{
    "sesiones": 
     [
        {
            "id": "S18",
            "Semana": 6,
            "Tema": "Archivos txt",
            "Fecha": "2021-06-10",
            "Estado": "E"
        },
        {
            "id": "S19",
            "Semana": 6,
            "Tema": "Archivos Json",
            "Fecha": "2021-06-12",
            "Estado": "E"
        },
        {
            "id": "S20",
            "Semana": 6,
            "Tema": "Archivos csv",
            "Fecha": "2021-06-15",
            "Estado": "P"
        }
    ]
}
"""
