CREATE DATABASE api_project;

USE api_project

CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    username VARCHAR(50),
    valid BOOLEAN
);

USE api_project;

SELECT * FROM users;

SELECT * FROM users WHERE valid = true;

SELECT * FROM users WHERE valid = false;

SELECT COUNT(*) FROM users;

CREATE TABLE test_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    test_name VARCHAR(100),
    result VARCHAR(10),
    message VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SELECT * FROM test_results;
SELECT COUNT(*) FROM test_results;
SELECT result, COUNT(*)
FROM test_results
GROUP BY result;

ALTER TABLE users MODIFY id INT AUTO_INCREMENT;

