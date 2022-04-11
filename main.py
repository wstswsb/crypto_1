from click import echo, style
from models import XlXrYlYr

from structure import (
    inputs,
    s_block_1_analytics_service,
    s_block_2_analytics_service,
    s_block_3_analytics_service,
    bit_permutation_service,
    bit_permutation_service_expand,
    bit_computing_service,
    key_1_1_search_service,
    key_1_2_search_service,
    key_1_3_search_service,
    key_3_1_search_service,
    key_3_2_search_service,
    key_3_3_search_service,
    k_1_1_repository,
    k_1_2_repository,
    k_1_3_repository,
    k_3_1_repository,
    k_3_2_repository,
    k_3_3_repository,
    probability_a_c_presenter,
    key_and_count_presenter
)

s1_probabilistic = s_block_1_analytics_service.compute_most_probabilistic()
s2_probabilistic = s_block_2_analytics_service.compute_most_probabilistic()
s3_probabilistic = s_block_3_analytics_service.compute_most_probabilistic()

echo(style("S1 most probabilistic:", "green"))
echo(probability_a_c_presenter.present(s1_probabilistic))

echo(style("S2 most probabilistic:", "green"))
echo(probability_a_c_presenter.present(s2_probabilistic))

echo(style("S3 most probabilistic:", "green"))
echo(probability_a_c_presenter.present(s3_probabilistic) + "\n")

permuted_delta_a = bit_computing_service.merge_nums(
    num_bit_length=4,
    nums=[s1_probabilistic.a, s2_probabilistic.a, s3_probabilistic.a]
)
echo(style("Permuted delta_A: ", "yellow") + f"{permuted_delta_a:>014_b}")

delta_a = bit_permutation_service_expand.reverse_permutation(permuted_delta_a)
echo(style("delta_A: ", "green") + f"{delta_a:>09_b}")

delta_c = bit_computing_service.merge_c(
    s1_probabilistic.c,
    s2_probabilistic.c,
    s3_probabilistic.c,
)
echo(style("delta_С: ", "green") + f"{delta_c:>09_b}")

delta_d = bit_permutation_service.permute(delta_c)
echo(style("delta_D: ", "green") + f"{delta_d:>09_b}")

#  data from lab_program
echo()
echo(style("Analyze inputs by lab_program:", "blue"))
xy_1 = XlXrYlYr(
    xl=0b0001_0111,
    xr=0b0101_1010,
    yl=0b1000_0000,
    yr=0b1001_1100,
)
xy_2 = XlXrYlYr(

    xl=0b0100_0000,
    xr=0b0011_0101,
    yl=0b1101_0111,
    yr=0b1111_0011,
)
print(len(inputs))
for triad in inputs:
    xy_1 = triad.xl_xr_yr_yl_1
    xy_2 = triad.xl_xr_yr_yl_2
    key_1_1_search_service.find_keys(xy_1.xr, xy_2.xr, s1_probabilistic.c)
    key_1_2_search_service.find_keys(xy_1.xr, xy_2.xr, s2_probabilistic.c)
    key_1_3_search_service.find_keys(xy_1.xr, xy_2.xr, s3_probabilistic.c)

    key_3_1_search_service.find_last_keys(
        xy_1, xy_2,
        c_start_position=1, c_end_position=4
    )
    key_3_2_search_service.find_last_keys(
        xy_1, xy_2,
        c_start_position=4, c_end_position=7
    )
    key_3_3_search_service.find_last_keys(
        xy_1, xy_2,
        c_start_position=7, c_end_position=9
    )

echo(style("\nK_1_1 statistics: ", "green"))
for key in k_1_1_repository.count_keys():
    echo(key_and_count_presenter.present(key))

echo(style("\nK_1_2 statistics: ", "green"))
for key in k_1_2_repository.count_keys():
    echo(key_and_count_presenter.present(key))

echo(style("\nK_1_3 statistics: ", "green"))
for key in k_1_3_repository.count_keys():
    echo(key_and_count_presenter.present(key))

echo(style("\nK_3_1 statistics: ", "green"))
for key in k_3_1_repository.count_keys():
    echo(key_and_count_presenter.present(key))

echo(style("\nK_3_2 statistics: ", "green"))
for key in k_3_2_repository.count_keys():
    echo(key_and_count_presenter.present(key))

echo(style("\nK_3_3 statistics: ", "green"))
for key in k_3_3_repository.count_keys():
    echo(key_and_count_presenter.present(key))

