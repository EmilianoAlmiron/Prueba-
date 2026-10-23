condicion= True

while condicion :
    edad = int(input("Dame tu edad: "))
    dni = input("Trajiste DNI: ")
    
    if edad >= 18 and dni == "si" or dni == "Si":
        print("Podes pasar al cuarto oscuro")
        
    else:
        print("No podes VOTAR")