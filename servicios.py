# En este archivo creamos funciones para nuestro programa
# Creamos un menu con las opciones que tiene el usuario dentro del programa 
def menu():
    print("-----MENU-----")
    print("1. Agregar producto.")
    print("2. Mostrar inventario.")
    print("3. Buscar en inventario.")
    print("4. Actualizar producto.")
    print("5. Eliminar producto.")
    print("6. Calcular estadisticas.")
    print("7. Salir.")

#Creamos una funcion para la opcion 1 
#Si la opcion es 1 entonces el programa Continua pidiendole los datos del producto al usuario(nombre del producto, precio y cantidad)
def agregar_producto(inventario, nombre, precio, cantidad):

    

            #Colocamos condiciones que queremos que se cumplan, en este caso que el precio y la cantidad sean numeros positivos, 
            #Si no se cumplen se le dara un mensaje de error al usuario y se le pedira que ingrese un valor valido.

    if precio < 0:
        print("Error: El precio y la cantidad deben ser números positivos.ejemplo(1, 2, 3...)")
        print("Por favor, ingrese un precio válido.")
    elif cantidad < 0:
        print("Error: El precio y la cantidad deben ser números positivos.(ejemplo: 1, 2, 3...)")
        print("Por favor, ingrese una cantidad válida.")
            
            #Si los numeros son positivos entonces:
            #El programa continua agregando los productos en diccionarios los cuales estan agrupados  a una lista llamada invetario como lo vimos en las primeras lineas del codigo

    else:
        producto={"nombre":nombre ,"precio":precio ,"cantidad":cantidad}
        inventario.append(producto)
        print(inventario)
        
#Si la opcion es 2 entonces el prorama imprimira los produstos agregados 
#Si el usuario no ah agregado ningun producto el progama se lo hara saber 
def mostrar_inventario(inventario):        
    if len(inventario) == 0:
        print("El inventario esta vacio")
    else:
        for i in inventario:
            print(f"Nombre: {i['nombre']} | Precio: ${i['precio']} | Cantidad: {i['cantidad']}")

#definimos una funcion para buscar el producto dentro del invetario

def buscar_producto(inventario, nombre):
    for i in inventario:
        if i.get("nombre") == nombre:
            return i
    return None
   
#creamos una funcion para actualizar los datos de los productos ingresados en el inventario

def actualizar_producto(inventario, nombre, nuevo_nombre, nuevo_precio=None, nueva_cantidad=None):
    for i in inventario:
        if i.get("nombre").lower().strip() == nombre.lower().strip():
            if nuevo_nombre is not None:
                i["nombre"] = nuevo_nombre.lower().strip()
            if nuevo_precio is not None:
                i["precio"] = nuevo_precio
            if nueva_cantidad is not None:
                i["cantidad"] = nueva_cantidad
            return i
    return None
            
def eliminar_producto(inventario, nombre):               
    eliminar = input("deseas eliminar? (y/n): ").lower().strip()
    if eliminar == "y" :
        for i in inventario:
            if i.get("nombre").lower().strip()== nombre.lower().strip():
                inventario.remove(i)  
                return i  
    



            
            

#Mostrara la cantidad de productos en el inventario 
#Sumara el total de los productos agregados al invetario
            
def calcular_estadisticas(inventario):
    if len(inventario)== 0:
        print("No hay elementos para calcular")
        return None
    else:
        total_value = 0
        cant_total = 0
        for i in inventario:
            cant_total += i["cantidad"]
            total_value += i["precio"] * i["cantidad"]
        return{
            "Cantidad de productos":cant_total,
            "Precio Total de productos":total_value
            }