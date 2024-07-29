import json

def mostrar_menu():
    print("\nBienvenido al Administrador de Lista de Compras")
    print("Menú:")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Ver artículos")
    print("4. Ordenar artículos")
    print("5. Guardar lista")
    print("6. Cargar lista")
    print("7. Salir")

def agregar_articulo(lista):
    nombre = input("Ingrese el nombre del artículo: ").strip()
    cantidad = input("Ingrese la cantidad del artículo: ").strip()
    if cantidad.isdigit():
        cantidad = int(cantidad)
    else:
        print("Cantidad inválida. Debe ser un número.")
        return

    categoria = input("Ingrese la categoría del artículo: ").strip()
    precio = input("Ingrese el precio del artículo: ").strip()
    try:
        precio = float(precio)
    except ValueError:
        print("Precio inválido. Debe ser un número.")
        return

    lista.append({"nombre": nombre, "cantidad": cantidad, "categoria": categoria, "precio": precio})
    print(f"Artículo '{nombre}' agregado con éxito.")

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
        total = 0
        for articulo in lista:
            print(f"{articulo['nombre']}: {articulo['cantidad']} (Categoría: {articulo['categoria']}, Precio: {articulo['precio']:.2f})")
            total += articulo['cantidad'] * articulo['precio']
        print(f"Total: {total:.2f}")
    else:
        print("La lista de compras está vacía.")

def ordenar_articulos(lista):
    if not lista:
        print("La lista de compras está vacía.")
        return

    criterio = input("Ordenar por (nombre/cantidad/precio): ").strip().lower()
    if criterio == 'nombre':
        lista.sort(key=lambda x: x['nombre'].lower())
        print("Lista ordenada por nombre.")
    elif criterio == 'cantidad':
        lista.sort(key=lambda x: x['cantidad'])
        print("Lista ordenada por cantidad.")
    elif criterio == 'precio':
        lista.sort(key=lambda x: x['precio'])
        print("Lista ordenada por precio.")
    else:
        print("Criterio inválido. Debe ser 'nombre', 'cantidad' o 'precio'.")

def guardar_lista(lista):
    filename = input("Ingrese el nombre del archivo para guardar la lista (con extensión .json): ").strip()
    try:
        with open(filename, 'w') as f:
            json.dump(lista, f, indent=4)
        print(f"Lista guardada en '{filename}'.")
    except Exception as e:
        print(f"Error al guardar la lista: {e}")

def cargar_lista():
    filename = input("Ingrese el nombre del archivo para cargar la lista (con extensión .json): ").strip()
    try:
        with open(filename, 'r') as f:
            lista = json.load(f)
        print(f"Lista cargada desde '{filename}'.")
        return lista
    except Exception as e:
        print(f"Error al cargar la lista: {e}")
        return []

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
            guardar_lista(lista_compras)
        elif opcion == '6':
            lista_compras = cargar_lista()
        elif opcion == '7':
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 7.")

if __name__ == "__main__":
    main()
