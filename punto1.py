## Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no. 

def comprobar_primo (numero):
    if numero <= 1:
        print("El número ingresado no es primo")
    else:
        es_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            print(f'El número {numero} es primo')
        else:
            print("El número ingresado no es primo")

try:
    numero = int(input("Escribí un número "))
    comprobar_primo(numero)
except ValueError:
    print("Ingresá un número entero válido.")