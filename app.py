from servicios import *
from archivos import *

inventario = []
option = 0
print("SISTEMA DE INVENTARIO")

while option !=9:
    menu()

    try:
        opcion = int(input("Seleccione opción (1-9): "))

        if opcion == 1:
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            nombre = input("Buscar: ")
            print(buscar_producto(inventario, nombre))

        elif opcion == 4:
            nombre = input("Producto a actualizar: ")

            nuevo_precio = input("Nuevo precio (enter omitir): ")
            nueva_cantidad = input("Nueva cantidad (enter omitir): ")

            
            if nuevo_precio: 
                nuevo_precio = float(nuevo_precio) 
            else :
                None
           
            if nueva_cantidad: 
                 nueva_cantidad = int(nueva_cantidad) 
            else: 
                None

            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

        elif opcion == 5:
            nombre = input("Producto a eliminar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == 6:
            estadisticas = calcular_estadisticas(inventario)
            print(estadisticas)

        elif opcion == 7:
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == 8:
            ruta = input("Ruta archivo: ")
            nuevos = cargar_csv(ruta)

            if nuevos:
                opcion_merge = input("¿Reemplazar? (S/N): ").upper()

                if opcion_merge == "S":
                    inventario = nuevos
                else:
                    inventario += nuevos

        elif opcion == 9:
            print("Saliendo...")
            break

    except:
        print("Error en entrada")
