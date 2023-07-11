import os
precios = [[3800, 3000, 2800, 3500] for a in range(10)]
estado = [[True for a in range(4)] for a in range(10)]
compradores = []
letras = ["A", "B", "C", "D"]
fecha = "11/07/2023"

def mostrar_menu():
    print("Bienvenido a la inmobiliaria Casa Feliz")
    print("Seleccione una opción:")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    opcion = input("Ingrese su opción: ")
    return opcion

def validar_opcion(opcion):
    try:
        opcion = int(opcion)
        if opcion < 1 or opcion > 5:
            raise ValueError
        return True
    except ValueError:
        return False

def validar_piso(piso):
    try:
        piso = int(piso)
        if piso < 1 or piso > 10:
            raise ValueError
        return True
    except ValueError:
        return False

def validar_tipo(tipo):
    if len(tipo) == 1 and tipo.isalpha():
        tipo = tipo.upper()
        if tipo in letras:
            return True
    return False

def validar_run(run):
    if len(run) == 8 and run.isdigit():
        return True
    return False

def comprar_departamento():
    mostrar_departamentos()
    piso = input("Ingrese el piso del departamento a comprar (1-10): ")
    tipo = input("Ingrese el tipo del departamento a comprar (A-D): ")
    if validar_piso(piso) and validar_tipo(tipo):
        piso = int(piso) - 1
        tipo = letras.index(tipo.upper())
        if estado[piso][tipo]:
            run = input("Ingrese el RUN del comprador (sin puntos ni dígito verificador): ")
            if validar_run(run):
                estado[piso][tipo] = False
                compradores.append((run, piso + 1, tipo + 1))
                print(f"La compra del departamento {letras[tipo]}{piso + 1} se ha realizado correctamente.")
            else:
                print("El RUN ingresado no es válido. Intente nuevamente.")
        else:
            print(f"El departamento {letras[tipo]}{piso + 1} no está disponible. Intente con otro.")
    else:
        print("El piso o tipo de departamento no son validos, por favor comprueba, e intenta nuevamente.")
        


def mostrar_departamentos():
    print("Departamentos disponibles:")
    print("Piso\tA\tB\tC\tD")
    for i in range(10):  
        print(f"{i + 1}", end="\t")
        for j in range(4):
            if estado[i][j]:
                print(letras[j], end="\t")
            else:
                print("X", end="\t")
        print()

def ver_compradores():
    compradores.sort()
    print("Listado de compradores:")
    print("RUN\t\tDepartamento")
    for run, piso, tipo in compradores:
        print(f"{run}\t{letras[tipo - 1]}{piso}")

def mostrar_ganancias():
    cantidades = [0, 0, 0, 0]
    totales = [0, 0, 0, 0]
    for _, piso, tipo in compradores:
        tipo -= 1
        cantidades[tipo] += 1
        totales[tipo] += precios[piso][tipo]
    print("Ganancias totales:")
    print("Tipo de Departamento\tCantidad\tTotal")
    for i in range(4):
        print(f"{letras[i]}\t\t\t{cantidades[i]}\t\t{totales[i]} UF")
    total_general = sum(totales)
    print(f"TOTAL\t\t\t{len(compradores)}\t\t{total_general} UF")

def salir():
    print(f"Gracias por usar nuestro programa inmobiliario Casa Feliz. Mi nombre es Ivan Fuentes y hoy es {fecha}. Que tenga un buen dia!.")

continuar = True

while continuar:
    opcion = mostrar_menu()
    if validar_opcion(opcion):
        opcion = int(opcion)
        if opcion == 1:
            os.system("cls")
            comprar_departamento()
        elif opcion == 2:
            os.system("cls")
            mostrar_departamentos()
        elif opcion == 3:
            os.system("cls")
            ver_compradores()
        elif opcion == 4:
            os.system("cls")
            mostrar_ganancias()
        elif opcion == 5:
            os.system("cls")
            salir()
            continuar = False
    else:
        print("La opción ingresada no es válida. Intente nuevamente.")