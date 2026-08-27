import random
num_pe = random.randint(1, 10)
bandera= True 
print("¡Adivina que número estoy pensando!")
while (bandera):
    n = int(input("Ingresar número: "))
    if( n > num_pe):
         print(" El número que pense es más bajo")
    elif( n < num_pe):
        print("EL número que pense es más alto")
    else:
        # es igual
        print("Felicidades, el", num_pe ,"es el número que pense")
        bandera=False