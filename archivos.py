import csv


def guardar_csv(inventario, ruta, incluir_header=True):
    """Guarda inventario en CSV"""
    if not inventario:
        print("Inventario vacío")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except Exception:
        print("Error al guardar archivo")


def cargar_csv(ruta):
    """Carga inventario desde CSV"""
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            encabezado = next(reader, None)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido")
                return []

            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue

                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"Productos cargados: {len(inventario)}")
        print(f"Filas inválidas: {errores}")

        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")
        return []