# Proyecto-Integrador-ISPC - Grupo 28

Integrantes.
Nombre: Ian Denis
Apellido: Marini
DNI: 38.409.531
Link: https://github.com/IanMarini
Mail: mariniiandenis@gmail.com

Nombre: Abril Maria Lourdes
Apellido: Sampieri Baldor
DNI: 43.284.820
Link:https://github.com/AbrilSampieri
Mail: abril.sampieri@gmail.com

## Proyecto: Sistema de Gestión de Biblioteca

### Descripción
El proyecto elegido es un Sistema de Gestión de Biblioteca. Este sistema permitirá a los bibliotecarios y usuarios gestionar los préstamos y devoluciones de libros de manera eficiente. Las funcionalidades principales incluyen la creación, lectura, actualización y eliminación de información sobre libros, usuarios y préstamos. Además, se proporcionarán herramientas para buscar libros, ver su disponibilidad y gestionar usuarios.

### Objetivo del Proyect
El objetivo principal del proyecto es desarrollar un sistema de gestión de biblioteca que permita a los usuarios realizar operaciones relacionadas con libros, usuarios y préstamos de manera eficiente y efectiva.

### Alcance del Proyecto
- Gestión de Libros:
Agregar nuevos libros al sistema.
Ver la lista de libros disponibles.
Actualizar la información de los libros existentes.
Eliminar libros del sistema.

- Gestión de Usuarios:
Agregar nuevos usuarios al sistema.
Ver la lista de usuarios registrados.
Actualizar la información de los usuarios existentes.
Eliminar usuarios del sistema.

- Gestión de Préstamos:
Registrar préstamos de libros a usuarios.
Ver la lista de préstamos activos.
Registrar la devolución de libros prestados.

### Configuración de las Tablas
Libros
- ID (Primary Key)
- Título
- Autor
- ISBN
- Editorial
- Año de Publicación
- Disponibilidad

Usuarios
- ID (Primary Key)
- Nombre
- Dirección
- Teléfono
- Email

Préstamos
- ID (Primary Key)
- ID_Libro (Foreign Key)
- ID_Usuario (Foreign Key)
- Fecha de Préstamo
- Fecha de Devolución

Categorías
- ID (Primary Key)
- Nombre

Libros_Categorías (Tabla de relación N:M)
- ID_Libro (Foreign Key)
- ID_Categoría (Foreign Key)

### Entidades
Libros: Almacena la información de los libros en la biblioteca.
- Atributos: ID (Clave primaria), Título, Autor, ISBN, Editorial, Año de Publicación, Disponibilidad.

Usuarios: Contiene los detalles de los usuarios de la biblioteca.
- Atributos: ID (Clave primaria), Nombre, Dirección, Teléfono, Email.

Préstamos: Registra los préstamos de libros a los usuarios.
- Atributos: ID (Clave primaria), Fecha de Préstamo, Fecha de Devolución.

Categorías: Almacena las categorías a las que pueden pertenecer los libros. 
- Atributos: ID (Clave primaria), Nombre.

### Relaciones y Cardinalidades

Relación Usuario-Préstamo:
Descripción: Un usuario puede realizar múltiples préstamos.
Cardinalidad:
- 1 a N (Un usuario puede tener varios préstamos).
- N a 1 (Un préstamo pertenece a un solo usuario).
  
Relación Libro-Préstamo:
Descripción: Un préstamo está asociado a un libro.
Cardinalidad:
- 1 a N (Un libro puede estar asociado a varios préstamos).
- N a 1 (Un préstamo se asocia a un solo libro).
  
Relación Libro-Categoría:
Descripción: Un libro puede pertenecer a una o varias categorías.
Cardinalidad:
- N a N (Un libro puede pertenecer a múltiples categorías y una categoría puede tener múltiples libros asociados).

### Menú de Navegación

Gestionar Libros
- Agregar Libro
- Ver Libros
- Actualizar Libro
- Eliminar Libro
    
Gestionar Usuarios
- Agregar Usuario
- Ver Usuarios
- Actualizar Usuario
- Eliminar Usuario
    
Gestionar Préstamos
- Registrar Préstamo
- Ver Préstamos
- Registrar Devolución

Salir

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Sistema de Gestión de Biblioteca
### Descripción
Esta es una aplicación modularizada para gestionar una biblioteca. Está dividida en varios archivos `.py` que contienen diferentes partes de la funcionalidad del sistema.

### Estructura del Proyecto
- `index.py`: Archivo principal que contiene el menú principal de la aplicación.
- `libros.py`: Contiene las funciones para gestionar libros, incluyendo agregar, ver, actualizar y eliminar libros.
- `usuarios.py`: Contiene las funciones para gestionar usuarios, incluyendo agregar, ver, actualizar y eliminar usuarios.
- `prestamos.py`: Contiene las funciones para gestionar préstamos, incluyendo registrar préstamos, ver préstamos y registrar devoluciones.
- `categorias.py`: Contiene las funciones para la gestión de categorías como agregar, ver categorías y eliminar categorías.

### Estructura de Archivos
Programación / Gestion_Biblioteca / index.py / libros.py / usuarios.py / prestamos.py / categorias.py
