def multiplicador():
    condicion = True

    while condicion:
        numero = int(input("Dame un numero para multiplicar: "))
        
        if numero >= 1 and numero <= 10:
            for i in range(1,11):
                print(numero * i)
                condicion = False
        else:
            print("Los numeros son del 1 al 10")

multiplicador()