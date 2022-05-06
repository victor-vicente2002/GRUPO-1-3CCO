DROP DATABASE IF EXISTS project_db;

CREATE DATABASE project_db;

USE project_db;

CREATE TABLE insert_values (
    id int PRIMARY KEY auto_increment,
    nome varchar(100),
    sistema_abastecimento int,
    turbidez decimal(10,5),
    ph decimal(10,5),
    temperatura decimal(10,5),
    coliformes int,
    exec_date datetime default CURRENT_TIMESTAMP()
);