CREATE TABLE IF NOT EXISTS test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Вставим данные только если таблица пустая
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM test_table) THEN
        INSERT INTO test_table (name) VALUES ('Initial data 1');
        INSERT INTO test_table (name) VALUES ('Initial data 2');
    END IF;
END
$$;
