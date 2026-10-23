print("Hola comprador, esta es una remera de $1000")

remera = 2000

desicion= input("con que vas a pagar, efectivo o tarjeta?: ")

if desicion == "efectivo":
    print("Tu remera tiene un despuento del 10% y te queda en $900")
else:
    cuotas = int(input("Tenemos 3+15%, 6+30%, 12+45% y 24+60%, cada una tiene un interes"))
    if cuotas == 3:
        print("Tu remera queda con un 15% mas")
    elif cuotas == 6:
        print("Tu remera queda con un 30% mas")
    elif cuotas == 12:
        print("Tu remera queda con un 45% mas")
    else:
        print("Tu remera queda con un 60% mas")