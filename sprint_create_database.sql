DROP DATABASE IF EXISTS bd_memory_time;
CREATE DATABASE bd_memory_time;
USE bd_memory_time;
CREATE TABLE tbl_memory_time(
	id INT PRIMARY KEY auto_increment,
    byte_memory INT,
    runtime DECIMAL(18,2),
    acumulator LONG,
    iterator_number INT,
    block_number INT,
    number_of_transactions INT
)auto_increment = 1;

# TRUNCATE tbl_memory_time;
# SELECT * FROM tbl_memory_time WHERE block_number = 2;