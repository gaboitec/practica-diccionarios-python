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

