
"""""
closet = ["Pantalon", "Camisa", "Harina pan"]
#closet = 0                1                  2
#Para crear un indice: (Es de orden ascendiente, el pantalon es 0, camisa 1 y asi va)

print (closet)"""""
#Se declara el nombre de la lista y sus componentes
Netflix = ["Batman","Simon", "Ley de los audaces"]
running = True

while running:
    
    print("1.Anadir \n2. Ver lista \n3. Borrar elemento \n4.Salir \n")

    opcion=int(input("Ingrese una opcion: "))

    if opcion == 1:
        pelicula=input ("Anade una pelicula: ")
        Netflix.append(pelicula)

    if opcion == 2:
        print(Netflix)

    if opcion == 3:
        indice = int(input("Ingrese el nombre que desea borrar:" ))
        Netflix.remove(indice)
#Pero si quieres borrar un numero se usa el .pop (El pop permite solo numeros)
#En cambio el .remove es para palabras
    if opcion == 4:
        print("Vuelva pronto")
        running = False
#El sort sirve para ordenar alfabeticamente los numeros (Organiza las listas)
    print("\n")