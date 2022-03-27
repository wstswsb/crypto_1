from typing import NamedTuple


class TableGenerationScripts(NamedTuple):
    a_inputs_outputs_c: str
    probability_a_c: str


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

table_generation_scripts = TableGenerationScripts(
    a_inputs_outputs_c=__a_inputs_outputs_c,
    probability_a_c=__probability_a_c,
)
