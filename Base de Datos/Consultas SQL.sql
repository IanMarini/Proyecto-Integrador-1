-- MySQL Workbench

-- CONSULTAS

-- Insertar datos: Esta consulta inserta un nuevo libro en la tabla de libros y un usuario en la tabla usuarios.
-- Insertar un nuevo libro.
-- Insertar un nuevo usuario.
-- Sintaxis SQL:
INSERT INTO Libros (Titulo, Autor, ISBN, Editorial, Anio_Publicacion, Disponibilidad)
VALUES ('El Señor de los Anillos', 'J.R.R. Tolkien', '978-0-395-08254-4', 'Houghton Mifflin Harcourt', 1954, TRUE);
INSERT INTO Usuarios (Nombre, Direccion, Telefono, Email)
VALUES ('Marcela Pérez', 'Calle Falsa 456, Ciudad', '234-5678', 'marcela.perez@example.com');

-- Actualizar datos: Esta consulta actualiza la disponibilidad de un libro en la tabla de libros y actualiza el teléfono de un usuario en la tabla de usuarios.
-- Actualizar la disponibilidad de un libro.
-- Actualizar el teléfono de un usuario.
-- Sintaxis SQL:
UPDATE Libros SET Disponibilidad = FALSE WHERE ID = 1;
UPDATE Usuarios SET Telefono = '351-6623039' WHERE ID = 6;

-- Eliminar datos: Esta consulta elimina un libro de la tabla de libros y elimina un usuario de la tabla de usuarios.
-- La consulta Drop elimina una tabla incluyendo los datos en ella.
-- Eliminar un libro.
-- Eliminar un usuario.

-- Sintaxis SQL:
DELETE FROM prestamos WHERE Fecha_Devolucion IS NULL LIMIT 100;
DELETE FROM usuarios WHERE Email = 'ana.lopez@example.com' LIMIT 1;

-- -----------------------------------------------------------------------------

-- Mostrar todos los datos de una sola tabla:
SELECT * FROM Libros;

-- Mostrar algunas columnas de una tabla:

SELECT Titulo, Autor FROM Libros;

-- Consulta con WHERE:
SELECT * FROM Libros WHERE Anio_Publicacion = 2008;

-- Consulta con WHERE utilizando BETWEEN:

SELECT * FROM Libros WHERE Anio_Publicacion BETWEEN 2000 AND 2010;

-- Consulta con WHERE utilizando LIMIT:
SELECT * FROM Libros LIMIT 5;

-- Consulta con INNER JOIN:
SELECT Libros.Titulo, Categorias.Nombre
FROM Libros
INNER JOIN Libros_Categorias ON Libros.ID = Libros_Categorias.ID_Libro
INNER JOIN Categorias ON Libros_Categorias.ID_Categoria = Categorias.ID;

-- WHERE con operador lógico:
SELECT * FROM Libros WHERE Editorial = 'Editorial Anagrama' AND Anio_Publicacion > 2000;

-- WHERE con operador de comparación:
SELECT * FROM Libros WHERE Anio_Publicacion >= 2000;

-- Tabla con GROUP BY:
SELECT Editorial, COUNT(*) as Total FROM Libros GROUP BY Editorial;

-- Tabla con GROUP BY usando función agregada:
SELECT Editorial, AVG(Anio_Publicacion) as Anio_Promedio FROM Libros GROUP BY Editorial;

-- Esta consulta selecciona todas las columnas de la tabla Libros para aquellos libros cuya columna Disponibilidad es TRUE. 
-- Esto significa que solo se obtendrán los libros que actualmente están disponibles para préstamo.
SELECT * FROM Libros WHERE Disponibilidad = TRUE;
SELECT * FROM Libros WHERE Disponibilidad = FALSE;

-- Consultar todos los préstamos no devueltos:
-- Esta consulta une las tablas Prestamos, Libros y Usuarios para mostrar los préstamos que aún no han sido devueltos (Fecha_Devolucion IS NULL). 
-- Se listan el ID del préstamo, el título del libro, el nombre del usuario y la fecha del préstamo.
-- ( En caso de que no hubiese eliminado los valores NULL )
SELECT Prestamos.ID, Libros.Titulo, Usuarios.Nombre, Prestamos.Fecha_Prestamo 
FROM Prestamos
JOIN Libros ON Prestamos.ID_Libro = Libros.ID
JOIN Usuarios ON Prestamos.ID_Usuario = Usuarios.ID
WHERE Prestamos.Fecha_Devolucion IS NULL;

-- Consultar libros por categoría:
-- Esta consulta selecciona los libros que pertenecen a la categoría 'Novelas'. 
-- Se unen las tablas Libros, Libros_Categorias y Categorias para obtener los títulos de los libros y sus categorías correspondientes.
SELECT Libros.Titulo, Categorias.Nombre 
FROM Libros
JOIN Libros_Categorias ON Libros.ID = Libros_Categorias.ID_Libro
JOIN Categorias ON Libros_Categorias.ID_Categoria = Categorias.ID
WHERE Categorias.Nombre = 'Novelas';

-- Consultar los libros prestados en los últimos 30 días:
-- Esta consulta selecciona los libros que han sido prestados en los últimos 30 días. 
-- Se unen las tablas Prestamos, Libros y Usuarios y se filtran los préstamos cuya fecha de préstamo es dentro de los últimos 30 días (Fecha_Prestamo >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)).
SELECT Libros.Titulo, Usuarios.Nombre, Prestamos.Fecha_Prestamo 
FROM Prestamos
JOIN Libros ON Prestamos.ID_Libro = Libros.ID
JOIN Usuarios ON Prestamos.ID_Usuario = Usuarios.ID
WHERE Prestamos.Fecha_Prestamo >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);