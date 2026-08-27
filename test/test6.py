#RECURSIVIDAD
#FACTORIAL
def factorial(numero):
    #Condicion que rompa la recursividad
    if numero <= 1:
        return 1
    return numero * factorial(numero - 1)


n = int(input("Ingresar número: "))
i = factorial(n)
print("La factorial de", n, "es", i)