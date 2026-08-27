#El usuario ingresa el número y tu devuelves el valor de la factorial
def factorial(número):
    mul = 1
    for i in range(1,número+1):
        mul = mul * i
    return mul


n = int(input("ingresar número: "))
respuesta = factorial(n)
print("El facrtorial de", n, "es", respuesta)