# Sistema de Inventario con CRUD y Persistencia CSV

Este proyecto es un **sistema de gestión de inventario** desarrollado en Python que permite agregar, mostrar, buscar, actualizar y eliminar productos, así como guardar y cargar el inventario desde archivos CSV. También incluye estadísticas y validaciones de entrada.

---

## Estructura del proyecto


#### inventario
-  app.py # Archivo principal con el menú de usuario
-  servicios.py # Funciones CRUD y cálculo de estadísticas
-  archivos.py # Funciones para guardar y cargar CSV
- README.md # Documentación del proyecto


---

## Funciones principales

### CRUD de productos

- **Agregar producto**  
  Permite agregar un producto con nombre, precio y cantidad.

- **Mostrar inventario**  
  Lista todos los productos en un formato legible.

- **Buscar producto**  
  Busca un producto por nombre y muestra sus detalles.

- **Actualizar producto**  
  Permite modificar el precio y/o la cantidad de un producto existente.

- **Eliminar producto**  
  Elimina un producto del inventario por nombre.

### Estadísticas

- `unidades_totales`: suma de todas las cantidades.  
- `valor_total`: suma de precio × cantidad de todos los productos.  
- `producto_mas_caro`: producto con mayor precio.  
- `producto_mayor_stock`: producto con mayor cantidad.

### Persistencia CSV

- **Guardar CSV**:  
  - Valida que el inventario no esté vacío.  
  - Permite incluir encabezado opcional.  
  - Maneja errores de escritura y permisos.

- **Cargar CSV**:  
  - Valida encabezado y formato de filas.  
  - Convierte precio a `float` y cantidad a `int`.  
  - Omite filas inválidas y muestra un contador de errores.  
  - Pregunta si se desea **sobrescribir** o **fusionar** el inventario actual.

---

## Estructura de datos

El inventario se mantiene en memoria como una **lista de diccionarios**:


inventario = [
    {"nombre": "Producto1", "precio": 100.0, "cantidad": 5},
    {"nombre": "Producto2", "precio": 50.0, "cantidad": 10},
]

**Cada diccionario contiene:**

nombre (str) – Nombre del producto
precio (float) – Precio unitario
cantidad (int) – Cantidad disponible
### Requisitos
- Python 3.x
- Módulos estándar: csv
## Uso
Ejecutar el archivo principal:
python app.py
Seleccionar una opción del menú:
1. Agregar
2. Mostrar
3. Buscar
4. Actualizar
5. Eliminar
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir

- Seguir las instrucciones en pantalla para cada operación.
- El programa continuará hasta seleccionar Salir.

**Validaciones**

- Opciones del menú: numéricas entre 1 y 9.
- Precio y cantidad: numéricos y no negativos.
- Manejo de errores: entradas inválidas, archivos inexistentes, errores de lectura/escritura.

**Notas**

Al fusionar inventarios desde CSV, si un producto ya existe:

- Se suma la cantidad.
- Se actualiza el precio al nuevo valor del archivo cargado.
- Los mensajes de error y confirmación permiten al usuario continuar sin cerrar el programa.

# diagrama de flujo

<img width="1959" height="1491" alt="WEEK 301 drawio" src="https://github.com/user-attachments/assets/40e5978a-bfe2-4712-b800-b2ead0dd91ff" />


## link de git hub
**URL:**
https://github.com/williamracineroa/week-3.git
