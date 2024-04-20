
"""""
def nombre(nombre):

    print(f"Mi nombre es: {nombre}")


name=input("Ingresa tu nombre: ")

nombre(name)
"""""


def suma(num1,num2):

    resultado = num1 + num2

    return resultado

def resta(num1,num2):
    
    resultado= num1 - num2
    return resultado

print(resta(1,2))
print("\n")
print(resta(2,1))


def matematica (num1,num2):

    resultado= (f"{suma(num1,num2)} , {resta(num1,num2)}")
    return resultado

numero1= int(input("Ingresa el numero 1 "))
numero2= int(input("Ingresa el numero 2 "))

print (f"{suma(numero1,numero2)},{resta(numero1,numero2)}")

print ("\n")

print(matematica(numero1,numero2))