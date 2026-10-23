#1-Calcular en area de un rectanguno y el perimetro del mismo

def area_rec(base, altura):
    area = base * altura
    return area

b= int(input("Dame la base del rectangulo: "))
a = int(input("Dame la altura del rectangulo: "))

resultado= area_rec(b,a)
print("Tu area del rectangulo es: ", resultado)


#2- Crea una funcion es_par(numero) que reciba un numero
#y devuelva si es par o impar

#ayuda= operador %

#3-Calculadora / funciones:sumar-restar-multiplicar y dividir

def suma(num1,num2):
    sumar= num1 + num2
    return sumar
