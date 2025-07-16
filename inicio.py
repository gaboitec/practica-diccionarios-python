def registrar_producto(inventario):
    while True:
        precio = 0
        cantidad = 0
        codigo = input("Ingrese el código único del producto: ")
        if codigo in inventario:
            print("Ese código ya existe. Intente con otro.")
            break

        nombre = input("Nombre del producto: ")
        categoria = input("Categoría (Hombre/Mujer/Niño): ")
        talla = input("Talla (S/M/L/XL): ")

        try:
            precio = float(input("Precio unitario (Q): "))
            if precio <= 0:
                print("El precio debe ser mayor que Q0.00.")
                continue
        except ValueError:
            print("Ingrese un número válido para el precio.")
            continue

        try:
            cantidad = int(input("Cantidad en stock: "))
            if cantidad <= 0:
                print("La cantidad debe ser positiva.")
                continue
        except ValueError:
            print("Ingrese un número entero válido para la cantidad.")
            continue

        # Guardar en el inventario
        inventario[codigo] = {
            "nombre": nombre,
            "categoria": categoria,
            "talla": talla,
            "precio": precio,
            "cantidad": cantidad
        }
        print("Producto registrado exitosamente.")
        break


def mostrar_productos(inventario):
    print("\nLista de productos en inventario:")
    for codigo, datos in inventario.items():
        print(f"- Código: {codigo}")
        for clave, valor in datos.items():
            print(f"  {clave}: {valor}")
        print("")


def buscar_producto(inventario):
    codigo = input("\nIngrese el código del producto a buscar: ")
    if codigo in inventario:
        print(f"\nDetalles del producto '{codigo}':")
        for clave, valor in inventario[codigo].items():
            print(f"{clave}: {valor}")
    else:
        print("Producto no encontrado.")


def calcular_valor_total(inventario):
    total = sum(prod["precio"] * prod["cantidad"] for prod in inventario.values())
    print(f"\nValor total del inventario: Q{total:.2f}")


def contar_por_categoria(inventario):
    conteo = {}
    for datos in inventario.values():
        categoria = datos["categoria"]
        conteo[categoria] = conteo.get(categoria, 0) + 1

    print("\nProductos por categoría:")
    for categoria, cantidad in conteo.items():
        print(f"{categoria}: {cantidad}")


inventario = {}

while True:
    cantidad = 0
    try:
        cantidad = int(input("¿Cuántos productos deseas ingresar? (0 para salir): "))
    except ValueError:
        print("Ingrese un número válido.")

    for _ in range(cantidad):
        registrar_producto(inventario)

    mostrar_productos(inventario)
    buscar_producto(inventario)
    calcular_valor_total(inventario)
    contar_por_categoria(inventario)
