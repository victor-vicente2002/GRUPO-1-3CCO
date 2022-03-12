create database ALGASCATARINA;
use ALGASCATARINA;

create table insert_values(
id int PRIMARY KEY auto_increment,
bank_transaciton int,
accumulate long,
memory decimal(18,2),
time_elapsed numeric(18,2),
exec_date datetime default CURRENT_TIMESTAMP()
);