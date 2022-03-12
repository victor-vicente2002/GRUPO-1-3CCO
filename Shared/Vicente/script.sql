CREATE DATABASE measures;

\c measures;

CREATE TABLE measures(
id serial PRIMARY KEY,
transactions numeric,
accumulate double precision,
memory numeric,
time_elapsed numeric(12,10),
exec_date timestamp default now());