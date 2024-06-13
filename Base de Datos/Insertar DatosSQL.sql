-- MySQL Workbench

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