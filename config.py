import json
from typing import NamedTuple
import os
from dotenv import dotenv_values

env = dotenv_values()

__base_dir = os.path.dirname(os.path.realpath(__file__))


class Config(NamedTuple):
    BASE_DIR: str
    BLOCK_BIT_SIZE: int
    EXPANDED_BLOCK_BIT_SIZE: int
    PERMUTATION_WITH_EXPANSION: list[int]
    PERMUTATION: list[int]
    S_BLOCK_INPUT_BIT_SIZE: int
    S_BLOCK_1_ANALYTICS_DB_PATH: str
    S_BLOCK_2_ANALYTICS_DB_PATH: str
    S_BLOCK_3_ANALYTICS_DB_PATH: str
    KEY_1_1_DB_PATH: str
    KEY_1_2_DB_PATH: str
    KEY_1_3_DB_PATH: str
    KEY_3_1_DB_PATH: str
    KEY_3_2_DB_PATH: str
    KEY_3_3_DB_PATH: str


config = Config(
    __base_dir,
    int(env["BLOCK_BIT_SIZE"]),
    int(env["EXPANDED_BLOCK_BIT_SIZE"]),
    json.loads(env["PERMUTATION_WITH_EXPANSION"]),
    json.loads(env["PERMUTATION"]),
    int(env["S_BLOCK_INPUT_BIT_SIZE"]),
    f"{__base_dir}/{env['S_BLOCK_1_ANALYTICS_DB_PATH']}",
    f"{__base_dir}/{env['S_BLOCK_2_ANALYTICS_DB_PATH']}",
    f"{__base_dir}/{env['S_BLOCK_3_ANALYTICS_DB_PATH']}",
    f"{__base_dir}/{env['KEY_1_1_DB_PATH']}",
    f"{__base_dir}/{env['KEY_1_2_DB_PATH']}",
    f"{__base_dir}/{env['KEY_1_3_DB_PATH']}",
    f"{__base_dir}/{env['KEY_3_1_DB_PATH']}",
    f"{__base_dir}/{env['KEY_3_2_DB_PATH']}",
    f"{__base_dir}/{env['KEY_3_3_DB_PATH']}",

)
