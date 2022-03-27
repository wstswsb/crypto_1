CREATE TABLE IF NOT EXISTS a_inputs_outputs_c (
    a INTEGER  NOT NULL,
    input_1 INTEGER NOT NULL,
    input_2 INTEGER NOT NULL,
    output_1 INTEGER NOT NULL,
    output_2 INTEGER NOT NULL,
    c INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS probability_a_c (
    a INTEGER NOT NULL,
    c INTEGER NOT NULL,
    probability REAL NOT NULL
);

SELECT a, input_1, input_2, output_1, output_2, c FROM a_inputs_outputs_c
WHERE a=5;
