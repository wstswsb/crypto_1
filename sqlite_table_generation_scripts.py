from typing import NamedTuple


class TableGenerationScripts(NamedTuple):
    a_inputs_outputs_c: str
    probability_a_c: str
    key_1_1: str
    key_1_2: str
    key_1_3: str

    key_3_1: str
    key_3_2: str
    key_3_3: str


__a_inputs_outputs_c = """
CREATE TABLE IF NOT EXISTS a_inputs_outputs_c (
    a INTEGER,
    input_1 INTEGER,
    input_2 INTEGER,
    output_1 INTEGER,
    output_2 INTEGER,
    c INTEGER
);
"""

__probability_a_c = """
CREATE TABLE IF NOT EXISTS probability_a_c (
    a INTEGER NOT NULL,
    c INTEGER NOT NULL,
    probability REAL NOT NULL
);
"""

__key_tables = [
    f"CREATE TABLE IF NOT EXISTS key_{i}_{j}"
    f"(key INTEGER NOT NULL);"
    for i in (1, 3)
    for j in (1, 2, 3)
]

table_generation_scripts = TableGenerationScripts(
    a_inputs_outputs_c=__a_inputs_outputs_c,
    probability_a_c=__probability_a_c,
    key_1_1=__key_tables[0],
    key_1_2=__key_tables[1],
    key_1_3=__key_tables[2],
    key_3_1=__key_tables[3],
    key_3_2=__key_tables[4],
    key_3_3=__key_tables[5],
)
