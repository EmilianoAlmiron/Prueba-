usuario = None
contrasena = None

usuarioG = "Emiliano"
contrasenaG = "1234"

while usuario != usuarioG and contrasena != contrasenaG :
    usuario = input("Dame el usuario: ")
    contrasena = input("Dame la contrasena: ")
    
    if usuario == usuarioG and contrasena == contrasenaG :
        print("Usuario y Contrasena Correctos, podes pasar")
    else:
        print("Usuario o Contrasena incorrectos")