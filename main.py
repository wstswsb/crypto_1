import click

from structure import (
    first_s_block_analytics_service,
    second_s_block_analytics_service,
    third_s_block_analytics_service,
    probability_a_c_presenter
)

most_probabilistic_values = [
    first_s_block_analytics_service.analyze_s_block(),
    second_s_block_analytics_service.analyze_s_block(),
    third_s_block_analytics_service.analyze_s_block(),
]

for index, most_probabilistic in enumerate(most_probabilistic_values):
    click.echo(click.style(f"S_{index+1}_BLOCK most probabilistic:", fg="green"))
    click.echo(probability_a_c_presenter.present(most_probabilistic))
