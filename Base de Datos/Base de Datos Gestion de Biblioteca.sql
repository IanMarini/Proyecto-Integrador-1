-- MySQL Workbench

-- CREAR SCHEMA SI NO EXISTE CON NOMBRE DEL PROYECTO 'Gestion de Biblioteca'.
CREATE SCHEMA IF NOT EXISTS `Gestion_Biblioteca` DEFAULT CHARACTER SET utf8mb3 ;
USE `Gestion_Biblioteca` ;

-- -----------------------------------------------------------------------------

-- Tabla de libros
CREATE TABLE Libros (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Titulo VARCHAR(255) NOT NULL,
    Autor VARCHAR(255) NOT NULL,
    ISBN VARCHAR(20) NOT NULL,
    Editorial VARCHAR(255) NOT NULL,
    Anio_Publicacion INT NOT NULL,
    Disponibilidad BOOLEAN NOT NULL
);

-- -----------------------------------------------------------------------------

-- Tabla de usuarios
CREATE TABLE Usuarios (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255) NOT NULL,
    Direccion VARCHAR(255) NOT NULL,
    Telefono VARCHAR(15) NOT NULL,
    Email VARCHAR(255) NOT NULL
);

-- -----------------------------------------------------------------------------

-- Tabla de préstamos
CREATE TABLE Prestamos (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ID_Libro INT,
    ID_Usuario INT,
    Fecha_Prestamo DATE NOT NULL,
    Fecha_Devolucion DATE,
    FOREIGN KEY (ID_Libro) REFERENCES Libros(ID),
    FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID)
);

-- -----------------------------------------------------------------------------

-- Tabla de categorías
CREATE TABLE Categorias (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(255) NOT NULL
);

-- -----------------------------------------------------------------------------

-- Tabla de relación
CREATE TABLE Libros_Categorias (
    ID_Libro INT,
    ID_Categoria INT,
    FOREIGN KEY (ID_Libro) REFERENCES Libros(ID),
    FOREIGN KEY (ID_Categoria) REFERENCES Categorias(ID),
    PRIMARY KEY (ID_Libro, ID_Categoria)
);

-- -----------------------------------------------------------------------------
-- AGREGAR DATOS A TABLAS
-- AGREGAR DATOS A LA TABLA LIBROS: A LAS COLUMNAS QUE SON TITULO,AUTOR,ISBN,EDITORIAL,ANIOPUBLICACION,DISPONIBILIDAD.
INSERT INTO Libros (Titulo, Autor, ISBN, Editorial, Anio_Publicacion, Disponibilidad) VALUES
('El Misterio de la Biblioteca', 'Carlos Ruiz', '978-3-16-148410-0', 'Editorial Planeta', 2015, TRUE),
('La Sombra del Viento', 'Laura Gallego', '978-1-4028-9462-6', 'Editorial Anagrama', 2008, TRUE),
('Cien Años de Soledad', 'Gabriel García Márquez', '978-0-7432-7356-5', 'Editorial Sudamericana', 1967, FALSE),
('El Código Da Vinci', 'Dan Brown', '978-0-385-50420-1', 'Doubleday', 2003, TRUE),
('Los Pilares de la Tierra', 'Ken Follett', '978-0-451-21418-4', 'Penguin Books', 1989, TRUE),
('El Nombre del Viento', 'Patrick Rothfuss', '978-0-7564-0476-2', 'DAW Books', 2007, TRUE),
('Juego de Tronos', 'George R. R. Martin', '978-0-553-10354-0', 'Bantam Books', 1996, FALSE),
('1984', 'George Orwell', '978-0-452-28423-4', 'Signet Classics', 1949, TRUE),
('Orgullo y Prejuicio', 'Jane Austen', '978-0-14-143951-8', 'Penguin Classics', 1813, TRUE),
('El Hobbit', 'J.R.R. Tolkien', '978-0-618-00221-3', 'Houghton Mifflin Harcourt', 1937, FALSE);

INSERT INTO Usuarios (Nombre, Direccion, Telefono, Email) VALUES
('Juan Pérez', 'Calle Falsa 123, Ciudad', '123-4567', 'juan.perez@example.com'),
('María García', 'Avenida Siempreviva 742, Ciudad', '987-6543', 'maria.garcia@example.com'),
('Luis Martínez', 'Calle Luna 456, Ciudad', '456-7890', 'luis.martinez@example.com'),
('Ana López', 'Calle Sol 789, Ciudad', '321-6549', 'ana.lopez@example.com'),
('Pedro Sánchez', 'Calle Estrella 101, Ciudad', '654-3210', 'pedro.sanchez@example.com'),
('Laura Fernández', 'Calle Nube 202, Ciudad', '789-0123', 'laura.fernandez@example.com'),
('Jorge Rodríguez', 'Calle Mar 303, Ciudad', '012-3456', 'jorge.rodriguez@example.com'),
('Marta Gómez', 'Calle Río 404, Ciudad', '234-5678', 'marta.gomez@example.com'),
('Carlos Torres', 'Calle Bosque 505, Ciudad', '876-5432', 'carlos.torres@example.com'),
('Lucía Díaz', 'Calle Montaña 606, Ciudad', '567-8901', 'lucia.diaz@example.com');

INSERT INTO Prestamos (ID_Libro, ID_Usuario, Fecha_Prestamo, Fecha_Devolucion) VALUES
(1, 1, '2024-01-10', '2024-01-20'),
(2, 2, '2024-02-15', '2024-02-28'),
(3, 3, '2024-03-05', '2024-03-15'),
(4, 4, '2024-04-12', NULL),
(5, 5, '2024-05-08', '2024-05-18'),
(6, 6, '2024-06-14', NULL),
(7, 7, '2024-07-21', '2024-07-31'),
(8, 8, '2024-08-16', NULL),
(9, 9, '2024-09-23', '2024-10-03'),
(10, 10, '2024-10-29', '2024-11-12');

INSERT INTO Categorias (Nombre) VALUES
('Drama'),
('Historia'),
('Ciencia Ficción'),
('Politica'),
('Novelas');

INSERT INTO Libros_Categorias (ID_Libro, ID_Categoria) VALUES
(1, 1),
(2, 4),
(3, 5),
(4, 1),
(5, 4),
(6, 4),
(7, 4),
(8, 5),
(9, 5),
(10, 4);

-- -----------------------------------------------------------------------------

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

