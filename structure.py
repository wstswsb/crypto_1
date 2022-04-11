from s_block_reader import SBlockReader
from config import config
from sqlite_table_generation_scripts import table_generation_scripts
from xl_xr_yl_yr_reader import XlXrYlYrReader
from services import (
    BitComputingService,
    BitPermutationService,
    SBlockAnalyticsService,
    FAnalyticsService,
    KeySearchService,
)

from repositories import (
    AInputsOutputsCRepository,
    ProbabilityACRepository,
    K_1_X_Repository,
)
from s_block import (
    SBlock2Rows8Columns,
    SBlock4Rows4Columns,
)
from translators import (
    AInputsOutputsCTranslator,
    ProbabilityACTranslator,
)
from presenters import (
    ProbabilityACPresenter,
    ListPresenter,
    XlXrYlYrPresenter,
    KeyAndCountPresenter,
)

s_block_reader = SBlockReader(f"{config.BASE_DIR}/resources")
xl_xr_yl_yr_reader = XlXrYlYrReader(f"{config.BASE_DIR}/resources")

s_block_1: SBlock2Rows8Columns = s_block_reader.read("s_1_block.json")
s_block_2: SBlock2Rows8Columns = s_block_reader.read("s_2_block.json")
s_block_3: SBlock4Rows4Columns = s_block_reader.read("s_3_block.json")

inputs = xl_xr_yl_yr_reader.read("save.txt")
a_in_out_c_translator = AInputsOutputsCTranslator()
probability_a_c_translator = ProbabilityACTranslator()

s_block_1_a_in_out_c_repository = AInputsOutputsCRepository(
    translator=a_in_out_c_translator,
    db_path=config.S_BLOCK_1_ANALYTICS_DB_PATH,
    table_name="a_inputs_outputs_c",
    table_generation_script=table_generation_scripts.a_inputs_outputs_c,
)
s_block_2_a_in_out_c_repository = AInputsOutputsCRepository(
    translator=a_in_out_c_translator,
    db_path=config.S_BLOCK_2_ANALYTICS_DB_PATH,
    table_name="a_inputs_outputs_c",
    table_generation_script=table_generation_scripts.a_inputs_outputs_c,
)
s_block_3_a_in_out_c_repository = AInputsOutputsCRepository(
    translator=a_in_out_c_translator,
    db_path=config.S_BLOCK_3_ANALYTICS_DB_PATH,
    table_name="a_inputs_outputs_c",
    table_generation_script=table_generation_scripts.a_inputs_outputs_c,
)

s_block_1_probability_a_c_repository = ProbabilityACRepository(
    translator=probability_a_c_translator,
    db_path=config.S_BLOCK_1_ANALYTICS_DB_PATH,
    table_name="probability_a_c",
    table_generation_script=table_generation_scripts.probability_a_c,
)
s_block_2_probability_a_c_repository = ProbabilityACRepository(
    translator=probability_a_c_translator,
    db_path=config.S_BLOCK_2_ANALYTICS_DB_PATH,
    table_name="probability_a_c",
    table_generation_script=table_generation_scripts.probability_a_c,
)
s_block_3_probability_a_c_repository = ProbabilityACRepository(
    translator=probability_a_c_translator,
    db_path=config.S_BLOCK_3_ANALYTICS_DB_PATH,
    table_name="probability_a_c",
    table_generation_script=table_generation_scripts.probability_a_c,
)
k_1_1_repository = K_1_X_Repository(
    db_path=config.KEY_1_1_DB_PATH,
    table_name="key_1_1",
    table_generation_script=table_generation_scripts.key_1_1,
)
k_1_2_repository = K_1_X_Repository(
    db_path=config.KEY_1_2_DB_PATH,
    table_name="key_1_2",
    table_generation_script=table_generation_scripts.key_1_2,
)
k_1_3_repository = K_1_X_Repository(
    db_path=config.KEY_1_3_DB_PATH,
    table_name="key_1_3",
    table_generation_script=table_generation_scripts.key_1_3,
)

k_3_1_repository = K_1_X_Repository(
    db_path=config.KEY_3_1_DB_PATH,
    table_name="key_3_1",
    table_generation_script=table_generation_scripts.key_3_1
)
k_3_2_repository = K_1_X_Repository(
    db_path=config.KEY_3_2_DB_PATH,
    table_name="key_3_2",
    table_generation_script=table_generation_scripts.key_3_2
)

k_3_3_repository = K_1_X_Repository(
    db_path=config.KEY_3_3_DB_PATH,
    table_name="key_3_3",
    table_generation_script=table_generation_scripts.key_3_3
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

s_block_1_analytics_service = SBlockAnalyticsService(
    s_block=s_block_1,
    bit_computing_service=bit_computing_service,
    a_in_out_c_repository=s_block_1_a_in_out_c_repository,
    probability_a_c_repository=s_block_1_probability_a_c_repository,
)
s_block_2_analytics_service = SBlockAnalyticsService(
    s_block=s_block_2,
    bit_computing_service=bit_computing_service,
    a_in_out_c_repository=s_block_2_a_in_out_c_repository,
    probability_a_c_repository=s_block_2_probability_a_c_repository,
)
s_block_3_analytics_service = SBlockAnalyticsService(
    s_block=s_block_3,
    bit_computing_service=bit_computing_service,
    a_in_out_c_repository=s_block_3_a_in_out_c_repository,
    probability_a_c_repository=s_block_3_probability_a_c_repository,
)

f_analytics_service = FAnalyticsService(
    s_input_bit_length=config.S_BLOCK_INPUT_BIT_SIZE,
    s_1_analytics_service=s_block_1_analytics_service,
    s_2_analytics_service=s_block_2_analytics_service,
    s_3_analytics_service=s_block_3_analytics_service,
    permutation_service=bit_permutation_service_expand,
    computing_service=bit_computing_service,
)
key_1_1_search_service = KeySearchService(
    a_start_position=1,
    a_end_position=5,
    permutation_service=bit_permutation_service,
    permutation_with_expand_service=bit_permutation_service_expand,
    bit_computing_service=bit_computing_service,
    a_in_out_repository=s_block_1_a_in_out_c_repository,
    key_repository=k_1_1_repository,
)
key_1_2_search_service = KeySearchService(
    a_start_position=5,
    a_end_position=9,
    permutation_service=bit_permutation_service,
    permutation_with_expand_service=bit_permutation_service_expand,
    bit_computing_service=bit_computing_service,
    a_in_out_repository=s_block_2_a_in_out_c_repository,
    key_repository=k_1_2_repository,
)
key_1_3_search_service = KeySearchService(
    a_start_position=9,
    a_end_position=13,
    permutation_service=bit_permutation_service,
    permutation_with_expand_service=bit_permutation_service_expand,
    bit_computing_service=bit_computing_service,
    a_in_out_repository=s_block_3_a_in_out_c_repository,
    key_repository=k_1_3_repository,
)

key_3_1_search_service = KeySearchService(
    a_start_position=1,
    a_end_position=5,
    permutation_service=bit_permutation_service,
    permutation_with_expand_service=bit_permutation_service_expand,
    bit_computing_service=bit_computing_service,
    a_in_out_repository=s_block_1_a_in_out_c_repository,
    key_repository=k_3_1_repository,
)
key_3_2_search_service = KeySearchService(
    a_start_position=5,
    a_end_position=9,
    permutation_service=bit_permutation_service,
    permutation_with_expand_service=bit_permutation_service_expand,
    bit_computing_service=bit_computing_service,
    a_in_out_repository=s_block_1_a_in_out_c_repository,
    key_repository=k_3_2_repository,
)
key_3_3_search_service = KeySearchService(
    a_start_position=9,
    a_end_position=13,
    permutation_service=bit_permutation_service,
    permutation_with_expand_service=bit_permutation_service_expand,
    bit_computing_service=bit_computing_service,
    a_in_out_repository=s_block_1_a_in_out_c_repository,
    key_repository=k_3_3_repository,
)

probability_a_c_presenter = ProbabilityACPresenter()
probabilities_a_c_list_presenter = ListPresenter(probability_a_c_presenter)
xl_xr_yl_yr_presenter = XlXrYlYrPresenter()
key_and_count_presenter = KeyAndCountPresenter()
