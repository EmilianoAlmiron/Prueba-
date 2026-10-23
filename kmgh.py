numSecr = 50
numIng = None

while numSecr != numIng :
    numIng = int(input("Dame el numero que estas pensando: \n 01-Saludar \n Chau"))
    
    if numIng > numSecr :
        print("Mas bajo")
    elif numIng < numSecr:
        print("Mas alto")

print("Ganaste")