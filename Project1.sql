DROP TABLE IF EXISTS Salesman;

CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    Comission REAL
);

INSERT INTO Salesman (Salesman_id, name, city, Comission) VALUES
    ('5001', 'James Hoog', 'New York', 0.15),
    ('5002', 'Nail Knite', 'Paris', 0.13),
    ('5005', 'Pit Alex', 'London', 0.11),
    ('5006', 'Mc Lyon', 'Paris', 0.14),
    ('5007', 'Paul Adam', 'Rome', 0.13),
    ('5003', 'Lauson Hen', 'San Jose', 0.12);

SELECT * FROM Salesman;
SELECT * FROM Salesman WHERE city = 'Paris';
SELECT * FROM Salesman WHERE Comission > 0.13;
SELECT name FROM Salesman WHERE Comission < 0.13;
SELECT * FROM Salesman WHERE city != 'London';
