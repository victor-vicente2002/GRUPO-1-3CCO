CREATE TABLE measures(
    id SERIAL PRIMARY KEY,
    value NUMERIC,
    acc NUMERIC,
    used_memory NUMERIC,
    time_elapsed NUMERIC,
    exec_date TIMESTAMP DEFAULT NOW()
);