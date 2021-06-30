#Actividad 1:  Ahora vamos a elaborar un algoritmo que pida un número al
# usuario, e imprima todos los números pares desde 2 hasta el número.

# num = int(input("Digite un numero: "))
# i = 0
# while i <= num:
#     if i % 2 == 0:
#         print(i)
#     i += 1

#Actividad 2: Escribe el código de un ciclo para obtener el número de dígitos 
# de un número ingresado por el usuario.

# num = int(input("Digite un número: "))
# i = 0
# num2 = abs(num)
# while 0 != num2:
#     i += 1
#     num2 //= 10

# if num == 0:
#     i = 1
# print(i)

#Actividad 3: Escribe el código que solicite números al usuario hasta que 
# éste ingrese -1. Cuando se ingrese -1, el programa debe imprimir el
# promedio de todos los números ingresados hasta ese momento 
# (sin contar con el -1).
# i = -1
# num = 0
# sumNum = 0
# while num != -1:
#     sumNum += num
#     num = int(input("Digite un número: "))
#     i += 1
# print(f"El promedio es: {sumNum/i:.0f}")


# Actividad 4: Convierta a mayúscula inicial las palabras que se reciban 
# por teclado, hasta que digiten 'Salir'
# Método: capitalize()
# Retorna: una copia de la cadena con la primera letra en mayúsculas.

# Metodo 1
# while True:
#     word = input("Digite su palabra: ")
#     word = word.capitalize()
#     print(f"Palabra corregida {word}")
#     if word == "Salir":
#         break


# # Metodo 2
# word2 = ""
# while word2 != "Salir":
#     word2 = input("Digite su palabra: ")
#     word2 = word2.capitalize()
#     print(f"Palabra corregida {word2}")

# Actividad 5.
# Escribe un programa usando el ciclo Mientras Que (while) que, dado un número
# por parte del usuario genere la tabla de multiplicar del 1 al 12 para ese 
# número. 

# num = int(input("Digite un número: "))
# i = 0
# while i < 12: 
#     i += 1
#     print(num*i)

# Actividad 6: Escribe un programa que calcule el factorial de un número 
# ingresado por el usuario.
# Pista: El factorial de un número es la multiplicación del 1 hasta el 
# número; 4! = 1 * 2 * 3 * 4 = 24. Si aún tienes dudas busca en Google u 
# otro motor de búsqueda la definición de factorial.

# num = int(input("Digite un número: "))
# i = 1
# fac = 1
# while i <= num:
#     fac *= i
#     i += 1
# print(f"{num}! = {fac}")

# Actividad 7: Dado un conjunto de números ingresados por teclado, determine ç
# cuantos fueron positivos y cuantos fueron negativos, hasta que se ingrese 
# el número 0

# par = 0
# impar = 0
# num = int(input("Digite un número: "))
# while num != 0:
#     if num % 2 == 0:
#         par += 1
#     else:
#         impar += 1
#     num = int(input("Digite un número: "))
# print("Numeros pares:",par,"\nNumeros impares:",impar)

# Actividad 8: 5 amigos desean hacer una vaca para una fiesta, hacer un 
# algoritmo que pida la donación de cada uno de los participantes y diga
# total recaudado.

# i = 1
# total = 0
# while i < 6:
#     num = int(input(f"Digite la donación de amigo {i}: $"))
#     total += num
#     i += 1
# print(f"Total recaudado ${total}")

# Actividad 9: Martha ha diseñado un juego para que reciba un valor y un 
# total de vidas y determine si un jugador Gana o Pierde. El número de 
# vidas, determina el total de números que se van a utilizar en el cálculo
# de forma regresiva comenzando desde el valor entregado. Se determina el 
# promedio y si ese promedio es divisible por 2, la persona gana sino, 
# pierde.

# Por ejemplo, si enviamos el valor = 27 y un total de vidas = 4, el juego
# calcularía el promedio de (27+26+25+24)/4 = 25.5. 25.5 no es divisible 
# por 2 así que el juego retornaría "Pierde". Pero si enviáramos el 
# valor = 15  y el total de vidas = 7, (15+14+13+12+11+10+9)/7 = 12. 
# 12 es divisible por 2 así que el juego retornaría "Gana".

# Diseña el código para que un jugador que desconoce las reglas envíe el 
# valor y el número de vidas y le retorne si Gana o Pierde. 

# Pista: El ciclo se ejecutará tantas veces como vidas haya ingresado 
# el jugador.

# valor = int(input("Digite un valor: "))
# vidas = int(input("Digite número de vidas: "))
# sumValor = 0
# i = vidas
# while i > 0:
#     sumValor += valor
#     valor -= 1
#     i -= 1
# prom = sumValor / vidas

# if prom % 2 == 0:
#     print("Gana")
# else:
#     print("Pierde")

# Actividad 10: La empresa IPS SALUD en el programa de promoción y 
# prevención organiza un club con afiliados que están con obesidad y Cinco
# miembros de este club contra la obesidad desean saber cuánto han bajado 
# o subido de peso desde la última vez que se reunieron. Para esto se debe
# realizar un ritual de pesaje en donde cada uno se pesa en diez básculas 
# distintas para así tener el promedio más exacto de su peso. Si existe 
# diferencia positiva entre este promedio de peso y el peso de la última 
# vez que se reunieron, significa que subieron de peso. Pero si la 
# diferencia es negativa, significa que bajaron. Lo que el problema 
# requiere es que por cada persona se imprima un letrero que diga: “SUBIO”
# o “BAJO” y la cantidad de kilos que subió o bajo de peso.

i = 1
while i <= 5:
    try:
        while True:
            lastWeight = float(input(f"Digite el peso del miembro No. {i} registrado la última vez: "))
            if lastWeight > 5:
                j = 1
                sumWeight = 0
                while j <= 10:
                    try:
                        weight = float(input(f"Digite el peso registrado en báscula No. {j}: "))
                        while weight <= 5:
                            print(weight)
                            print("Error. Vulve a intentarlo.")
                            weight = float(input(f"Digite el peso registrado en báscula No. {j}: "))
                        print(weight<5)
                        sumWeight += weight
                    except Exception:
                        print("Error. Vuelve a intentarlo.")
                        continue
                    j += 1
                
                prom = sumWeight / 10
                if prom > lastWeight:
                    print(f"Miembro No. {i} SUBIO")
                elif prom < lastWeight:
                    print(f"Miembro No. {i} PERDIO")
                else:
                    print(f"Miembro No. {i} IGUAL")
                i += 1
                break
            else:
                print("Error. Vuelve a intenrtalo.")
    except Exception:
        print("Error. Vuelve a intentarlo.")
        continue
    
