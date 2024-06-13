# Proyecto-Integrador-ISPC

Integrantes: Grupo 28.

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
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
- Eliminar Préstamo
  
Gestionar Categorias
- Registrar Categoria
- Ver Categoria
- Eliminar Categoria
Salir

### Variables
Option1: número entero. Registra la opción "Gestionar Libros"

Option2: numero entero. Registra la opción "Gestionar Usuarios"

Option3: numero entero. Registra la opción "Gestionar Préstamos"

Option4: numero entero. Registra la opción "Gestionar Categorias"

Option5: numero entero. Registra la opción "Salir"

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Sistema de Gestión de Biblioteca
Esta aplicación está diseñada siguiendo un enfoque modular, lo que significa que está dividida en varios archivos que cumplen funciones específicas, separando el proyecto en partes. Los archivos se encuentran organizados en la carpeta Aplicación para facilitar su identificación y mantener el orden.

## Carpeta aplicacion
Aqui contiene los archivos .py donde se encuentran distribuidas las funciones e implementaciónes que componen nuestra aplicación Gestion de Biblioteca. Se describrira brevemente el propósito de cada archivo:
### Estructura del Proyecto
### index.py
**Descripción:**
Archivo principal que contiene el menú principal de la aplicación.

**Objetivo:**
- Proporcionar una interfaz de usuario para acceder a las diferentes opciones del sistema.
- Dirigir a los usuarios a las funcionalidades específicas basadas en sus selecciones (gestión de libros, usuarios, préstamos y categorías).

### libros.py
**Descripción:**
Contiene las funciones para gestionar libros, incluyendo agregar, ver, actualizar y eliminar libros.

**Objetivo:**
- **Agregar libros:** Permite añadir nuevos libros a la base de datos.
- **Ver libros:** Proporciona una lista de todos los libros disponibles en la biblioteca.
- **Actualizar libros:** Permite modificar la información de los libros existentes.
- **Eliminar libros:** Facilita la eliminación de libros de la base de datos.

### usuarios.py
**Descripción:**
Contiene las funciones para gestionar usuarios, incluyendo agregar, ver, actualizar y eliminar usuarios.

**Objetivo:**
- **Agregar usuarios:** Permite registrar nuevos usuarios en la biblioteca.
- **Ver usuarios:** Muestra una lista de todos los usuarios registrados.
- **Actualizar usuarios:** Permite actualizar la información de los usuarios existentes.
- **Eliminar usuarios:** Facilita la eliminación de usuarios del sistema.

### prestamos.py
**Descripción:**
Contiene las funciones para gestionar préstamos, incluyendo registrar préstamos, ver préstamos y registrar devoluciones.

**Objetivo:**
- **Registrar préstamos:** Permite registrar nuevos préstamos de libros a los usuarios.
- **Ver préstamos:** Proporciona una lista de todos los préstamos actuales y pasados.
- **Registrar devoluciones:** Permite registrar la devolución de libros prestados.

### categorias.py
**Descripción:**
Contiene las funciones para la gestión de categorías como agregar, ver categorías y eliminar categorías.

**Objetivo:**
- **Agregar categorías:** Permite añadir nuevas categorías de libros a la base de datos.
- **Ver categorías:** Muestra una lista de todas las categorías existentes.
- **Eliminar categorías:** Facilita la eliminación de categorías de la base de datos.

### Estructura de Archivos
Programación / Gestion_Biblioteca / index.py / libros.py / usuarios.py / prestamos.py / categorias.py

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Carpeta Base de Datos

Diagrama Entidad Realción Notación de Chen.png / Proceso de gestion de biblioteca.

Diagrama Crow Foot.mwb / DiagramaCrowFoot.png / Contiene la base de datos utilizada en la implementación final.

script_bd.sql Archivo que contiene el esquema de la base de datos utilizada en el programa.

DML.sql Este archivo contiene todas las consultas realizadas a la base de datos para poder lograr las funciones implementadas en la el programa.

datos.sql Datos alojados en la database, daots ficticios insertados en la base de datos para probar su funcionamiento.

### Requisitos para su funciónamiento.
Antes de iniciar el programa es necesario tener instalado python, la libreria de python mysql.connector; y mysql. Esta aplicación no cuenta con una interfaz gráfica por lo que debe ser ejecutada desde consola.

### Paso a paso
1.Instale las dependencias requeridas.
  
2.Clone el repositorio en un repositorio local.
  
3.Haciendo uso de los archivos .sql importer la base de datos en mysql workbench.
  
4.Desde mySQL Workbench genere una nueva conexión.
  
5.Edite el codigo fuente con sus credenciales de conexión con la base de datos.
  
6.Inicialice el archivo index.py.
