def registrar_producto(inventario):
    while True:
        codigo = input("Ingrese el código único del producto: ").strip().upper()
        if codigo in inventario:
            print("❌ Ese código ya existe. Intente con otro.")
            continue

        nombre = input("Nombre del producto: ").strip()
        categoria = input("Categoría (Hombre/Mujer/Niño): ").strip().capitalize()
        talla = input("Talla (S/M/L/XL): ").strip().upper()

        try:
            precio = float(input("Precio unitario (Q): "))
            if precio <= 0:
                print("❌ El precio debe ser mayor que Q0.00.")
                continue
        except ValueError:
            print("❌ Ingrese un número válido para el precio.")
            continue

        try:
            cantidad = int(input("Cantidad en stock: "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser positiva.")
                continue
        except ValueError:
            print("❌ Ingrese un número entero válido para la cantidad.")
            continue

        # Guardar en el inventario
        inventario[codigo] = {
            "nombre": nombre,
            "categoria": categoria,
            "talla": talla,
            "precio": precio,
            "cantidad": cantidad
        }
        print("✅ Producto registrado exitosamente.")
        break


def mostrar_productos(inventario):
    print("\n📦 Lista de productos en inventario:")
    for codigo, datos in inventario.items():
        print(f"- Código: {codigo}")
        for clave, valor in datos.items():
            print(f"  {clave.capitalize()}: {valor}")
        print("")


def buscar_producto(inventario):
    codigo = input("\n🔎 Ingrese el código del producto a buscar: ").strip().upper()
    if codigo in inventario:
        print(f"\n📌 Detalles del producto '{codigo}':")
        for clave, valor in inventario[codigo].items():
            print(f"{clave.capitalize()}: {valor}")
    else:
        print("❌ Producto no encontrado.")


def calcular_valor_total(inventario):
    total = sum(prod["precio"] * prod["cantidad"] for prod in inventario.values())
    print(f"\n💰 Valor total del inventario: Q{total:.2f}")


def contar_por_categoria(inventario):
    conteo = {}
    for datos in inventario.values():
        categoria = datos["categoria"]
        conteo[categoria] = conteo.get(categoria, 0) + 1

    print("\n📊 Productos por categoría:")
    for categoria, cantidad in conteo.items():
        print(f"{categoria}: {cantidad}")


