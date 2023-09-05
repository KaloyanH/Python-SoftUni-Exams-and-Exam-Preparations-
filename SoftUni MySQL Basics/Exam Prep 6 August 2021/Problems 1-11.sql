CREATE SCHEMA sgd;
USE sgd;

CREATE TABLE addresses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL
);

CREATE TABLE offices (
    id INT PRIMARY KEY AUTO_INCREMENT,
    workspace_capacity INT NOT NULL,
    website VARCHAR(50),
    address_id INT NOT NULL,
    FOREIGN KEY (address_id)
        REFERENCES addresses (id)
);

CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    age INT NOT NULL,
    salary DECIMAL(10 , 2 ) NOT NULL,
    job_title VARCHAR(20) NOT NULL,
    happiness_level CHAR(1) NOT NULL
);

CREATE TABLE teams (
    id INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(40) NOT NULL,
    office_id INT NOT NULL,
    leader_id INT UNIQUE NOT NULL,
    FOREIGN KEY (office_id)
        REFERENCES offices (id),
    FOREIGN KEY (leader_id)
        REFERENCES employees (id)
);

CREATE TABLE games (
    id INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    rating FLOAT NOT NULL,
    budget DECIMAL(10 , 2 ) NOT NULL,
    release_date DATE,
    team_id INT NOT NULL,
    FOREIGN KEY (team_id)
        REFERENCES teams (id)
);

CREATE TABLE games_categories (
    game_id INT NOT NULL,
    category_id INT NOT NULL,
    PRIMARY KEY (game_id , category_id),
    FOREIGN KEY (game_id)
        REFERENCES games (id),
    FOREIGN KEY (category_id)
        REFERENCES categories (id)
);

INSERT INTO games (`name`, rating, budget, team_id)
SELECT REVERSE(SUBSTRING(LOWER((`name`)), 2)) , t.id , t.leader_id * 1000, t.id
FROM teams AS t
WHERE t.id BETWEEN 1 AND 9;

UPDATE employees AS e
JOIN teams AS t ON e.id = t.leader_id
SET e.salary = e.salary + 1000
WHERE age < 40 AND salary <= 5000;

DELETE FROM games
WHERE release_date IS NULL AND
id NOT IN (SELECT DISTINCT game_id FROM games_categories);

SELECT first_name, last_name, age, salary, happiness_level
FROM employees
ORDER BY salary, id;	

SELECT t.name AS team_name, a.name AS address_name, LENGTH(a.name) AS count_of_characters
FROM teams AS t
JOIN offices AS o ON t.office_id =  o.id
JOIN addresses AS a ON a.id = o.address_id
WHERE o.website IS NOT NULL
ORDER BY team_name, address_name;


SELECT 
    c.name,
    COUNT(g.id) AS games_count,
    ROUND(AVG(g.budget), 2) AS avg_budget,
    MAX(g.rating) AS max_rating
FROM
    games AS g
        JOIN
    games_categories AS gc ON g.id = gc.game_id
        JOIN
    categories AS c ON c.id = gc.category_id
GROUP BY c.name
HAVING max_rating >= 9.5
ORDER BY games_count DESC , c.name ASC;


SELECT g.name AS name,
g.release_date, 
CONCAT(SUBSTRING(g.description, 1, 10) , '...') AS summary,
	CASE
        WHEN MONTH(g.release_date) IN (1, 2, 3) THEN 'Q1'
        WHEN MONTH(g.release_date) IN (4, 5, 6) THEN 'Q2'
        WHEN MONTH(g.release_date) IN (7, 8, 9) THEN 'Q3'
        WHEN MONTH(g.release_date) IN (10, 11, 12) THEN 'Q4'
    END AS quarter,
    t.name AS team_name
FROM games AS g
JOIN teams AS t ON g.team_id = t.id
WHERE
    YEAR(g.release_date) = 2022
    AND MONTH(g.release_date) % 2 = 0
    AND g.name LIKE '%2'
ORDER BY
    quarter ASC;



SELECT g.name AS name, 
	CASE
    WHEN g.budget <= 50000 THEN 'Normal budget'
    WHEN g.budget > 50000 THEN 'Insufficient budget'
    END AS budget_level,
    t.name AS team_name,
    a.name AS address_name 
FROM games AS g
JOIN teams AS t ON t.id = g.team_id
JOIN offices AS o ON o.id = t.office_id
JOIN addresses AS a ON a.id = o.address_id
WHERE g.id NOT IN (SELECT DISTINCT game_id FROM games_categories) AND g.release_date IS NULL
ORDER BY name; 


SELECT g.name AS game_name, t.name AS team_name, a.name AS address_text
FROM games AS g
JOIN teams AS t ON t.id = g.team_id
JOIN offices AS o ON o.id = t.office_id
JOIN addresses AS a ON a.id = o.address_id;

DELIMITER $$

	CREATE FUNCTION udf_game_info_by_name(game_name VARCHAR(20))
	RETURNS TEXT
	DETERMINISTIC
	BEGIN
		DECLARE game_info TEXT;
		SELECT CONCAT("The ", g.name, " is developed by a ", t.name, " in an office with an address ", a.name)
		INTO game_info
		FROM games AS g
		JOIN teams AS t ON t.id = g.team_id
		JOIN offices AS o ON o.id = t.office_id
		JOIN addresses AS a ON a.id = o.address_id
		WHERE g.name = game_name;
		
		RETURN game_info;
	END$$

DELIMITER ;

DROP FUNCTION IF EXISTS udf_game_info_by_name;

SELECT udf_game_info_by_name('Bitwolf') AS info;

DELIMITER //
CREATE PROCEDURE udp_update_budget(IN min_game_rating FLOAT)
BEGIN
    UPDATE games AS g
    LEFT JOIN games_categories AS gc ON gc.game_id = g.id
    SET g.budget = g.budget + 100000, g.release_date = DATE_ADD(g.release_date, INTERVAL 1 YEAR)
    WHERE gc.game_id IS NULL
    AND g.rating > min_game_rating
    AND g.release_date IS NOT NULL;
END //
DELIMITER ;

