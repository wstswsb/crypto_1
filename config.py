import json
from typing import NamedTuple
import os
from dotenv import dotenv_values

env = dotenv_values()

__base_dir = os.path.dirname(os.path.realpath(__file__))


class Config(NamedTuple):
    BASE_DIRECTORY: str
    BLOCK_BIT_SIZE: int
    EXPANDED_BLOCK_BIT_SIZE: int
    PERMUTATION_WITH_EXPANSION: list[int]
    PERMUTATION: list[int]
    FIRST_S_BLOCK_ANALYTICS_DB_PATH: str
    SECOND_S_BLOCK_ANALYTICS_DB_PATH: str
    THIRD_S_BLOCK_ANALYTICS_DB_PATH: str


config = Config(
    BASE_DIRECTORY=__base_dir,
    BLOCK_BIT_SIZE=int(env["BLOCK_BIT_SIZE"]),
    EXPANDED_BLOCK_BIT_SIZE=int(env["EXPANDED_BLOCK_BIT_SIZE"]),
    PERMUTATION_WITH_EXPANSION=json.loads(env["PERMUTATION_WITH_EXPANSION"]),
    PERMUTATION=json.loads(env["PERMUTATION"]),
    FIRST_S_BLOCK_ANALYTICS_DB_PATH=f"{__base_dir}/{env['FIRST_S_BLOCK_ANALYTICS_DB_PATH']}",
    SECOND_S_BLOCK_ANALYTICS_DB_PATH=f"{__base_dir}/{env['SECOND_S_BLOCK_ANALYTICS_DB_PATH']}",
    THIRD_S_BLOCK_ANALYTICS_DB_PATH=f"{__base_dir}/{env['THIRD_S_BLOCK_ANALYTICS_DB_PATH']}"
)
