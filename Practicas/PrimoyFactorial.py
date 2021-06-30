# Actividad 5: Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. 
# Por cada número primo, mostrar la suma de sus dígitos. También solicitar al usuario un digito e informar la cantidad de veces 
# que aparece en el número(frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.

def esPrimo(num1):
    for i in range(2, num1):
        if num1 % i == 0:
            return False
    return num1 > 1


def busDigitos(num1,num2):
    i = 0
    k = 0
    while num2 > 0:
        j = num2 % 10
        k += j
        if num1 == j:
            i += 1
        num2 = num2 // 10 
    return k, i


def factorial(num1):
    return num1 if num1 == 2 else num1 * factorial(num1 - 1)


# def factorial(num1):
#     i = 1
#     fac = 1
#     while i <= num1:
#         fac *= i
#         i += 1
#     return fac


# def es_primo(num1):
#     j = 0
#     if num1 == 1:
#         return False
#     else:
#         for i in range (2,num1+1, 1):
#             if num1 % i == 0:
#                 j += 1
#                 if j > 1:
#                     break
#     if j == 1:
#         return True
#     else:
#         return False


def run():
    
    while True:
        num1 = int(input("Digite un número primo:\n-> "))
        if esPrimo(num1):
            print(f"Escribe un digito que quieras saber cuantas veces se repite en {num1}")
            num2 = int(input("-> "))
            j,k = busDigitos(num1,num2)
            print(f"La suma de los digitos de {num1} es {j}.")
            print(f"La cantidad de digitos igual a {num1} en {num2} es {k}.")
            print(f"El factorial de {num1} es {factorial(num1)}")
        break


if __name__ == '__main__':
    run()
