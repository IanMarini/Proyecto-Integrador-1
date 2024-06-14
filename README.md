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

### Video Proyecto Integrador

https://drive.google.com/file/d/1xwUeZeiSp0866iEfkUs8h-5K8Wq6SiS9/view?usp=sharing

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

## Carpeta Aplicacion
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

# Base de Datos del Proyecto
## Carepta Base de Datos
Este repositorio contiene los archivos relacionados con la base de datos del proyecto, incluyendo su estructura, diagramas y consultas SQL.

## Archivos Incluidos:

1. **Base de datos del proyecto, sus diagramas y SQL..pdf**
   - **Descripción:** Documento PDF que contiene la descripción de la base de datos del proyecto, sus diagramas y ejemplos de consultas SQL.
   - **Objetivo:** Proporcionar una documentación detallada de la estructura y contenido de la base de datos del proyecto.

2. **Conexión a BD.py**
   - **Descripción:** Archivo Python con código relacionado con la conexión a la base de datos.
   - **Objetivo:** Establecer y gestionar la conexión con la base de datos desde la aplicación.

3. **Consultas SQL.sql**
   - **Descripción:** Archivo SQL con consultas para interactuar con la base de datos.
   - **Objetivo:** Proporcionar consultas predefinidas utilizables en la aplicación.

4. **Crear TablasSQL.sql**
   - **Descripción:** Archivo SQL con consultas para crear las tablas de la base de datos.
   - **Objetivo:** Definir la estructura inicial de la base de datos creando las tablas necesarias.

5. **Diagrama Lógico Físico (Notación Crow Foot).mwb**
   - **Descripción:** Archivo de modelo de base de datos en MySQL Workbench con notación Crow's Foot.
   - **Objetivo:** Visualizar y diseñar la estructura de la base de datos utilizando MySQL Workbench.

6. **Diagrama Lógico Físico (Notación Crow Foot).png**
   - **Descripción:** Imagen PNG del diagrama lógico y físico de la base de datos en notación Crow's Foot.
   - **Objetivo:** Proporcionar una representación visual de la estructura de la base de datos.

7. **DiagramaEntidadRelación Notación Chen..png**
   - **Descripción:** Imagen PNG del diagrama de entidad-relación de la base de datos en notación Chen.
   - **Objetivo:** Proporcionar una representación visual alternativa de la estructura de la base de datos.

8. **Insertar DatosSQL.sql**
   - **Descripción:** Archivo SQL con consultas para insertar datos en la base de datos.
   - **Objetivo:** Proporcionar consultas predefinidas para insertar datos en las tablas de la base de datos.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Carpeta Programación
## Análisis EPS

- **Descripción:** Este archivo contiene el análisis del proceso EPS (Entrada, Procesamiento, Salida) para un sistema o programa específico.
- **Objetivo:** Proporcionar una descripción detallada de cómo el sistema o programa interactúa con el usuario y procesa la información.

## Menu_PseudoCódigo

- **Descripción:** Este archivo contiene el pseudocódigo en PSeInt para un menú de opciones en un programa o sistema.
- **Objetivo:** Definir las opciones disponibles para el usuario y la lógica de navegación del menú dentro del programa o sistema.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Requisitos para su funciónamiento.
Antes de iniciar el programa es necesario tener instalado python, la libreria de python mysql.connector; y mysql. Esta aplicación no cuenta con una interfaz gráfica por lo que debe ser ejecutada desde consola.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Paso a paso
1.Instale las dependencias requeridas.
  
2.Clone el repositorio en un repositorio local.
  
3.Haciendo uso de los archivos .sql importer la base de datos en mysql workbench.
  
4.Desde mySQL Workbench genere una nueva conexión.
  
5.Edite el codigo fuente con sus credenciales de conexión con la base de datos.
  
6.Inicialice el archivo index.py.
