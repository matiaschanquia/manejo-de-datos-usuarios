import unicodedata
import opciones


def convertirArchivoArray(contenido):
    datos = contenido.read().split("\n")

    for i in range(len(datos)):
        datos[i] = datos[i].split(",")

    return datos


def main():
    print("-"*50 + " Bienvenido! " + "-"*50)
    try:
        contenido = open("./datosUsuarios.csv", mode="r", encoding="utf-8")
    except FileNotFoundError:
        print("Se produjo un error al abrir el archivo. Programa finalizado")
        return

    datos = convertirArchivoArray(contenido)

    contenido.close()

    opcion = ""
    while opcion != 0:
        opcion = ""
        print()
        print("1) Nombres con sus respectivas apariciones")
        print("2) Apellidos con sus respectivas apariciones")
        print("3) Provincias con sus respectivas cantidades")
        print("4) Buscar si existe alguien por su nombre y apellido")
        print("0) Salir")
        print()
        while not opcion.isdigit():
            opcion = input("Ingrese una opción: ")
            if not opcion.isdigit():
                print("La opcion ingresada no es un número")
        print()
        opcion = int(opcion)

        if opcion == 1:
            opciones.opcion1(datos)
        elif opcion == 2:
            opciones.opcion2(datos)
        elif opcion == 3:
            opciones.opcion3(datos)
        elif opcion == 4:
            opciones.opcion4(datos)
        elif opcion == 0:
            print("Programa finalizado")
        else:
            print("Opción incorrecta")


if __name__ == "__main__":
    main()
