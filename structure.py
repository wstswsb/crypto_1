from services import (
    BitComputingService,
    BitPermutationService,
    SBlockAnalyticsService,
)

from repositories import (
    AInputsOutputsCRepository,
    ProbabilityACRepository,
)
from s_block import SBlock2Rows8Columns, SBlock4Rows4Columns
from s_block_reader import SBlockReader
from config import config
from sqlite_table_generation_scripts import table_generation_scripts
from translators import AInputsOutputsCTranslator, ProbabilityACTranslator
from presenters import ProbabilityACPresenter

s_block_reader = SBlockReader(path_resources=f"{config.BASE_DIRECTORY}/resources")

first_s_block: SBlock2Rows8Columns = s_block_reader.read("s_1_block.json")
second_s_block: SBlock2Rows8Columns = s_block_reader.read("s_2_block.json")
third_s_block: SBlock4Rows4Columns = s_block_reader.read("s_3_block.json")

a_inputs_outputs_c_translator = AInputsOutputsCTranslator()
probability_a_c_translator = ProbabilityACTranslator()

s_block_1_a_inputs_outputs_c_repository = AInputsOutputsCRepository(
    translator=a_inputs_outputs_c_translator,
    db_path=config.FIRST_S_BLOCK_ANALYTICS_DB_PATH,
    table_name="a_inputs_outputs_c",
    table_generation_script=table_generation_scripts.a_inputs_outputs_c,
)
s_block_2_a_inputs_outputs_c_repository = AInputsOutputsCRepository(
    translator=a_inputs_outputs_c_translator,
    db_path=config.SECOND_S_BLOCK_ANALYTICS_DB_PATH,
    table_name="a_inputs_outputs_c",
    table_generation_script=table_generation_scripts.a_inputs_outputs_c,
)
s_block_3_a_inputs_outputs_c_repository = AInputsOutputsCRepository(
    translator=a_inputs_outputs_c_translator,
    db_path=config.THIRD_S_BLOCK_ANALYTICS_DB_PATH,
    table_name="a_inputs_outputs_c",
    table_generation_script=table_generation_scripts.a_inputs_outputs_c,
)

s_block_1_probability_a_c_repository = ProbabilityACRepository(
    translator=probability_a_c_translator,
    db_path=config.FIRST_S_BLOCK_ANALYTICS_DB_PATH,
    table_name="probability_a_c",
    table_generation_script=table_generation_scripts.probability_a_c,
)
s_block_2_probability_a_c_repository = ProbabilityACRepository(
    translator=probability_a_c_translator,
    db_path=config.SECOND_S_BLOCK_ANALYTICS_DB_PATH,
    table_name="probability_a_c",
    table_generation_script=table_generation_scripts.probability_a_c,
)
s_block_3_probability_a_c_repository = ProbabilityACRepository(
    translator=probability_a_c_translator,
    db_path=config.THIRD_S_BLOCK_ANALYTICS_DB_PATH,
    table_name="probability_a_c",
    table_generation_script=table_generation_scripts.probability_a_c,
)

bit_computing_service = BitComputingService()
bit_permutation_service = BitPermutationService(
    permutation=config.PERMUTATION,
    bit_computing_service=bit_computing_service,
    input_bit_size=config.BLOCK_BIT_SIZE,
    output_bit_size=config.BLOCK_BIT_SIZE,
)
bit_permutation_service_expand = BitPermutationService(
    permutation=config.PERMUTATION_WITH_EXPANSION,
    bit_computing_service=bit_computing_service,
    input_bit_size=config.BLOCK_BIT_SIZE,
    output_bit_size=config.EXPANDED_BLOCK_BIT_SIZE,
)

first_s_block_analytics_service = SBlockAnalyticsService(
    s_block=first_s_block,
    bit_computing_service=bit_computing_service,
    a_inputs_outputs_c_repository=s_block_1_a_inputs_outputs_c_repository,
    probability_a_c_repository=s_block_1_probability_a_c_repository,
)
second_s_block_analytics_service = SBlockAnalyticsService(
    s_block=second_s_block,
    bit_computing_service=bit_computing_service,
    a_inputs_outputs_c_repository=s_block_2_a_inputs_outputs_c_repository,
    probability_a_c_repository=s_block_2_probability_a_c_repository,
)
third_s_block_analytics_service = SBlockAnalyticsService(
    s_block=third_s_block,
    bit_computing_service=bit_computing_service,
    a_inputs_outputs_c_repository=s_block_3_a_inputs_outputs_c_repository,
    probability_a_c_repository=s_block_3_probability_a_c_repository,
)

probability_a_c_presenter = ProbabilityACPresenter()
