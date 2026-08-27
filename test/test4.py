#Funciones
#Contar Vocales
def contar_vocales(Texto):
    contador = 0 
    vocal=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U" ]
    for y in range(len(Texto)):
        if Texto[y] in vocal:
            contador = contador + 1
    return contador
tex=input("Ingresar Texto: ")
cantidad = contar_vocales(tex) 
print("El Texto que ingreso, tiene", cantidad, "Vocales")
