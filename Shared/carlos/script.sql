
CREATE TABLE IF NOT EXISTS  water_measures(
    id SERIAL PRIMARY KEY,
    sample_score NUMERIC,
    sulfates NUMERIC,
    sample_qty NUMERIC,
    chloramines NUMERIC,
    analysis_date TIMESTAMP DEFAULT NOW()
);