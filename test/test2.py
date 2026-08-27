#algoritmo que indique si el número es par o impar pero que pregunte indifinidamente

bandera = True
while bandera:
    n = int(input("Ingresar número: "))

    if(n % 2 == 0):
        print("Es un número par")
    else:
        print("Es un número impar")

    r = input("¿Quieres continuar (SI/NO)?: ")
    if( r in ["NO","No","no","nO","n","N"]):
        #Terminar el programa
        bandera=False