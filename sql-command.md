# Solución Ejercicio 1
    CREATE DATABASE Escuela;

# Solución Ejercicio 2
    USE Escuela;
    CREATE TABLE Estudiantes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        edad INT
    );

# Solución Ejercicio 3
    INSERT INTO Estudiantes (nombre, edad) VALUES ('Ana', 20);
    INSERT INTO Estudiantes (nombre, edad) VALUES ('Luis', 22);
    INSERT INTO Estudiantes (nombre, edad) VALUES ('Marta', 19);

# Solución Ejercicio 4
    SELECT * FROM Estudiantes;
    SELECT * FROM Estudiantes WHERE edad > 20;

# Solución Ejercicio 5
    UPDATE Estudiantes SET edad = 21 WHERE nombre = 'Ana';
# Solución Ejercicio 6
    DELETE FROM Estudiantes WHERE nombre = 'Marta';

# Solución Ejercicio 7
    SELECT COUNT(*) FROM Estudiantes;
    SELECT MAX(edad), MIN(edad), AVG(edad) FROM Estudiantes;

# Solución Ejercicio 8
    SELECT curso, COUNT(*) FROM Estudiantes GROUP BY curso;
    SELECT curso, COUNT(*) FROM Estudiantes GROUP BY curso HAVING COUNT(*) > 5;

# Solución Ejercicio 9
    SELECT nombre FROM Estudiantes WHERE edad > (SELECT AVG(edad) FROM Estudiantes);

# Solución Ejercicio 10
    SELECT Estudiantes.nombre, Cursos.nombre_curso
    FROM Estudiantes
    JOIN Cursos ON Estudiantes.curso = Cursos.id_curso;