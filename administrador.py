# Programa: Administrador de Lista de Compras

def mostrar_menu():
    print("\nBienvenido al Administrador de Lista de Compras")
    print("Menú:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Ver artículos")
    print("4. Ordenar artículos")
    print("5. Salir")

def agregar_articulo(lista):
    nombre = input("Ingrese el nombre del artículo: ").strip()
    cantidad = input("Ingrese la cantidad del artículo: ").strip()
    if cantidad.isdigit():
        cantidad = int(cantidad)
        lista.append({"nombre": nombre, "cantidad": cantidad})
        print(f"Artículo '{nombre}' agregado con éxito.")
    else:
        print("Cantidad inválida. Debe ser un número.")

def eliminar_articulo(lista):
    nombre = input("Ingrese el nombre del artículo a eliminar: ").strip()
    for articulo in lista:
        if articulo['nombre'].lower() == nombre.lower():
            lista.remove(articulo)
            print(f"Artículo '{nombre}' eliminado con éxito.")
            return
    print(f"Artículo '{nombre}' no encontrado en la lista.")

def ver_articulos(lista):
    if lista:
        print("\nLista de compras:")
        for articulo in lista:
            print(f"{articulo['nombre']}: {articulo['cantidad']}")
    else:
        print("La lista de compras está vacía.")

def ordenar_articulos(lista):
    if not lista:
        print("La lista de compras está vacía.")
        return

    criterio = input("Ordenar por (nombre/cantidad): ").strip().lower()
    if criterio == 'nombre':
        lista.sort(key=lambda x: x['nombre'].lower())
        print("Lista ordenada por nombre.")
    elif criterio == 'cantidad':
        lista.sort(key=lambda x: x['cantidad'])
        print("Lista ordenada por cantidad.")
    else:
        print("Criterio inválido. Debe ser 'nombre' o 'cantidad'.")

def main():
    lista_compras = []
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ").strip()
        if opcion == '1':
            agregar_articulo(lista_compras)
        elif opcion == '2':
            eliminar_articulo(lista_compras)
        elif opcion == '3':
            ver_articulos(lista_compras)
        elif opcion == '4':
            ordenar_articulos(lista_compras)
        elif opcion == '5':
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()