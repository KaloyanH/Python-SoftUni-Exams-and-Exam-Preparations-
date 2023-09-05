CREATE SCHEMA stc;
USE stc;


CREATE TABLE addresses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE categories (
	 id INT PRIMARY KEY AUTO_INCREMENT,
     name VARCHAR(10) NOT NULL
);

CREATE TABLE clients (
	id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE drivers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    rating FLOAT
);

CREATE TABLE cars (
    id INT PRIMARY KEY AUTO_INCREMENT,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20),
    `year` INT NOT NULL,
    mileage INT,
    `condition` CHAR(1) NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (category_id)
        REFERENCES categories (id)
);


CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    from_address_id INT NOT NULL,
    start DATETIME NOT NULL,
    bill DECIMAL(10 , 2 ),
    car_id INT NOT NULL,
    client_id INT NOT NULL,
    FOREIGN KEY (from_address_id)
        REFERENCES addresses (id),
    FOREIGN KEY (car_id)
        REFERENCES cars (id),
    FOREIGN KEY (client_id)
        REFERENCES clients (id)
);

CREATE TABLE cars_drivers (
    car_id INT NOT NULL,
    driver_id INT NOT NULL,
    PRIMARY KEY (car_id , driver_id),
    FOREIGN KEY (car_id)
        REFERENCES cars (id),
    FOREIGN KEY (driver_id)
        REFERENCES drivers (id)
);


INSERT INTO clients (full_name, phone_number)
SELECT CONCAT_WS(' ', d.first_name, d.last_name), CONCAT('(088) 9999', d.id * 2)
FROM drivers AS d
WHERE d.id BETWEEN 10 AND 20;

UPDATE cars AS c
SET c.condition = 'C'
WHERE (c.mileage >= 800000 OR c.mileage IS NULL) AND make != 'Mercedes-Benz'
AND c.year <= 2010;


DELETE FROM clients
WHERE LENGTH(full_name) > 3 
AND id NOT IN (SELECT DISTINCT client_id FROM courses);


SELECT make, model, `condition` 
FROM cars;

SELECT d.first_name, d.last_name, c.make, c.model, c.mileage 
FROM drivers AS d
JOIN cars_drivers AS cd ON cd.driver_id = d.id
JOIN cars AS c ON c.id = cd.car_id
WHERE c.mileage IS NOT NULL
ORDER BY c.mileage DESC, d.first_name;


SELECT c.id AS car_id, 
		c.make, 
        c.mileage, 
        COUNT(cs.id) AS count_of_courses ,
        ROUND(AVG(cs.bill),2) AS avg_bill
FROM cars AS c
LEFT JOIN courses AS cs ON cs.car_id = c.id
GROUP BY c.id
HAVING count_of_courses != 2
ORDER BY count_of_courses DESC, c.id;


SELECT c.full_name, COUNT(cr.id) AS count_of_cars, SUM(cs.bill) AS total_sum
FROM clients AS c
JOIN courses AS cs ON cs.client_id = c.id
JOIN cars AS cr ON cr.id = cs.car_id
GROUP BY c.full_name
HAVING SUBSTRING(full_name, 2, 1) = 'a'
ORDER BY c.full_name;

SELECT c.full_name, COUNT(DISTINCT cr.id) AS count_of_cars, SUM(cs.bill) AS total_sum
FROM clients AS c
JOIN courses AS cs ON cs.client_id = c.id
JOIN cars AS cr ON cr.id = cs.car_id
GROUP BY c.full_name
HAVING count_of_cars > 1 AND SUBSTRING(c.full_name, 2, 1) = 'a'
ORDER BY c.full_name;



SELECT a.name,
	CASE 
    WHEN HOUR(cs.start) BETWEEN 6 AND 20 THEN 'Day'
	WHEN HOUR(cs.start) BETWEEN 21 AND 23 THEN 'Night'
    WHEN HOUR (cs.start) BETWEEN 0 AND 5 THEN 'Night'
    END AS day_time, 
	cs.bill AS bill,
	cl.full_name AS full_name,
	car.make AS make , 
	car.model AS model , 
	cg.name AS category_name 
FROM addresses AS a
JOIN courses AS cs ON cs.from_address_id = a.id
JOIN clients AS cl ON cl.id = cs.client_id 
JOIN cars AS car ON car.id = cs.car_id
JOIN categories AS cg ON cg.id = car.category_id
ORDER BY cs.id;



DELIMITER $$
CREATE FUNCTION udf_courses_by_client(phone_num VARCHAR(20))
	RETURNS INT
    DETERMINISTIC
    
BEGIN 
	DECLARE counter INT;
    SELECT COUNT(*) INTO counter
    FROM courses AS c
    JOIN clients AS cl ON cl.id = c.client_id
    WHERE cl.phone_number = phone_num;
    RETURN counter;
END$$

DELIMITER ;

DELIMITER $$
CREATE PROCEDURE udp_courses_by_address(address_name VARCHAR(100))
DELIMITER ;


SELECT 	addr.name AS name, 
	cli.full_name AS full_name, 
    CASE
    WHEN cou.bill <= 20 THEN 'LOW'
    WHEN cou.bill <= 30 THEN 'Medium'
    WHEN cou.bill > 30 THEN 'High'
    END AS level_of_bill,
    car.make AS make, 
    car.condition AS `condition`, 
    cat.name AS cat_name
FROM addresses AS addr
JOIN courses AS cou ON cou.from_address_id = addr.id
JOIN clients AS cli ON cli.id = cou.client_id
JOIN cars AS car ON car.id = cou.car_id
JOIN categories AS cat ON cat.id = car.category_id
ORDER BY car.make, cli.full_name;

DELIMITER $$

CREATE PROCEDURE udp_courses_by_address(address_name VARCHAR(100))
BEGIN
    SELECT 	addr.name AS name, 
			cli.full_name AS full_name, 
			CASE
				WHEN cou.bill <= 20 THEN 'Low'
				WHEN cou.bill <= 30 THEN 'Medium'
				WHEN cou.bill > 30 THEN 'High'
			END AS level_of_bill,
			car.make AS make, 
			car.condition AS `condition`, 
			cat.name AS cat_name
    FROM addresses AS addr
    JOIN courses AS cou ON cou.from_address_id = addr.id
    JOIN clients AS cli ON cli.id = cou.client_id
    JOIN cars AS car ON car.id = cou.car_id
    JOIN categories AS cat ON cat.id = car.category_id
    WHERE addr.name = address_name
    ORDER BY car.make, cli.full_name;
END$$

DELIMITER ;

CALL udp_courses_by_address('700 Monterey Avenue');
