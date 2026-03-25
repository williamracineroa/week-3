#Programa de inventario

from servicios import *

#Empezamos dandole la bienvenida al usuario al programa 

print("\n BIENVENIDO AL SISTEMA DE INVENTARIO \n")


# Hacemos un ciclo repetido con while para que este se repita siempre y cuando se cumplas las condiciones 
inventario=[]
val=1
while val == 1:
    
    menu()
    
    option=int(input("Ingrese el numero de la accion que desea realizar (1-9):"))

    #Creamos un condicional en caso de que el usuario ingrese un numero que no esta en el menu 
    if option < 1 or option > 9:    
        print("Algo salio mal! , inserte una opcion valida (1-9)")
    
    #Creamos condiciones para cada una de las opciones del menu
    #En este caso las condiciones estan inportadas desde el archivo de funciones  

    elif option == 1:
        nombre=input("nombre del producto : ")
        precio=float(input("Ingrese el precio del producto: $ "))

        cantidad=int(input("Ingrese la cantidad del producto:  "))
        
        agregar_producto(inventario,nombre,precio, cantidad)
       

    elif option == 2:
        mostrar_inventario(inventario)

    elif option == 3:
        nombre = input("ingrese el nombre del producto: ")
        print(buscar_producto(inventario, nombre))

    elif option == 4:
        nombre = input("Ingresa el nombre de del producto que quieres actualizar: ")
        nuevo_nombre = input("ingrese el nuevo nombre: ")
        nuevo_precio = float(input("ingrese nuevo precio: "))
        nueva_cantidad = int(input("ingrese la cantidad de producto: "))
        
        print(actualizar_producto(inventario, nombre,nuevo_nombre, nuevo_precio, nueva_cantidad))       
        print(inventario)

    elif option == 5:
        nombre = input("ingresa el nombre del producto que deseas eliminar: ")
        
        eliminar_producto(inventario, nombre)
        print("Se ah eliminado correctamente")
        
    #
        

    elif option == 6:
        print (calcular_estadisticas(inventario))

    #Si la opcion es 9 entonces:
    #Este saldra del programa 
    else:
        print("SALIENDO..")
        break
