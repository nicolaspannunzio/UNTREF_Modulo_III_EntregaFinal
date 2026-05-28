## Escribir una función que, dado el ingreso de 3 variables (a, b, c), 
## retorne las raíces resultantes de una ecuación cuadrática.

def discriminante (a, b, c):
    resultado_disc = b ** 2 - 4 * a * c
    if a == 0:
        return "El primer valor ingresado no puede ser cero"
    if resultado_disc > 0:
        raiz_cuadrada = resultado_disc ** 0.5
        primer_resultado = (- b + raiz_cuadrada) / (2 * a)
        segundo_resultado = (- b - raiz_cuadrada) / (2 * a)
        return f'La ecuación cuadrática tiene dos resultados posibles {primer_resultado:.3f} y {segundo_resultado:.3f}'
    elif resultado_disc == 0:
        tercer_resultado = (-b) / (2 * a)
        return f'El resultado de la función cuadrática es {tercer_resultado}'
    else:
        return "La ecuación no tiene solución para los numeros ingresados"


a = int(input("Ingresá el primer número "))
b = int(input("Ingresá el segundo número "))
c = int(input("Ingresá el tercer número "))
print(discriminante(a,b,c))