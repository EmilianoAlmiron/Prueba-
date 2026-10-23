contrasena = None

while contrasena:
    conTemp = input("Ingresa la contrasena: ")
    
    if conTemp == "Codearla":
        print("Contrasena correcta")
        contrasena = False
    else:
        print("Contrasena incorrecta")

print("Chau")