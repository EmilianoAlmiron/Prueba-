salida = "0"
valor = None

while salida != valor :
    valor = input(" 1-Saludar \n 2-Fecha \n 3-Msj \n 0-Salir \n Esciba su opcion: ")
    
    if valor == "1":
        print("Hola como estas?")
        
    else:
        print("tiene que ser del 0 al 3")