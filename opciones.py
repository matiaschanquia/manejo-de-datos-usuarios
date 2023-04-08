import unicodedata


def opcion1(datos):
    apariciones_nombres = {}

    for i in range(len(datos)):
        if apariciones_nombres.__contains__(datos[i][1]):
            apariciones_nombres[datos[i][1]] += 1
        else:
            apariciones_nombres[datos[i][1]] = 1

    for nombre in apariciones_nombres:
        print("Existe/n " + str(apariciones_nombres[nombre]) + " " + nombre)


def opcion2(datos):
    apariciones_apellidos = {}

    for i in range(len(datos)):
        if apariciones_apellidos.__contains__(datos[i][0]):
            apariciones_apellidos[datos[i][0]] += 1
        else:
            apariciones_apellidos[datos[i][0]] = 1

    for apellido in apariciones_apellidos:
        print("Existe/n " + str(apariciones_apellidos[apellido]) + " " + apellido)


def opcion3(datos):
    apariciones_provincias = {}

    for i in range(len(datos)):
        if apariciones_provincias.__contains__(datos[i][3]):
            apariciones_provincias[datos[i][3]] += 1
        else:
            apariciones_provincias[datos[i][3]] = 1

    for provincia in apariciones_provincias:
        print("Existe/n " + str(apariciones_provincias[provincia]) + " personas de " + provincia)


def opcion4(datos):
    print("Aclaración: se debe buscar sin tildes y la letra ñ como la n")
    nombre = input("Ingrese el nombre a buscar: ").lower()
    apellido = input("Ingrese el apellido a buscar: ").lower()

    print()
    contador = 0
    for i in range(len(datos)):
        apellido_sin_tildes = ''.join(
            c for c in unicodedata.normalize('NFD', datos[i][0].lower()) if unicodedata.category(c) != 'Mn')
        nombre_sin_tildes = ''.join(
            c for c in unicodedata.normalize('NFD', datos[i][1].lower()) if unicodedata.category(c) != 'Mn')

        if apellido_sin_tildes == apellido and nombre_sin_tildes == nombre:
            contador += 1
            print(datos[i])

    if contador == 0:
        print("No existe ninguna persona con ese nombre y apellido")
    else:
        print("Se obtuvo " + str(contador) + " resultado/s")
