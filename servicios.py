def menu():
    """Muestra el menú principal"""
    print("\n----- MENU -----")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")


def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un producto al inventario"""
    if precio < 0 or cantidad < 0:
        print("Error: valores inválidos")
        return

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })


def mostrar_inventario(inventario):
    """Muestra todos los productos"""
    if not inventario:
        print("Inventario vacío")
        return

    for p in inventario:
        print(f"{p['nombre']} | ${p['precio']} | {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """Busca un producto por nombre"""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio o cantidad de un producto"""
    producto = buscar_producto(inventario, nombre)

    if not producto:
        print("Producto no encontrado")
        return None

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    return producto


def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario"""
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        return producto
    return None


def calcular_estadisticas(inventario):
    """Calcula estadísticas del inventario"""
    if not inventario:
        return None
    else :
        subtotal = lambda p: p["precio"] * p["cantidad"]

        unidades_totales = sum(p["cantidad"] for p in inventario)
        valor_total = sum(subtotal(p) for p in inventario)

        producto_mas_caro = max(inventario, key=lambda p: p["precio"])
        producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": {
            "nombre": producto_mas_caro["nombre"],
            "precio": producto_mas_caro["precio"]
        },
        "producto_mayor_stock": {
            "nombre": producto_mayor_stock["nombre"],
            "cantidad": producto_mayor_stock["cantidad"]
        }
    }