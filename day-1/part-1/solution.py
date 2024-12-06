from pandas import (
    DataFrame,
    Series,
)
from pathlib import Path

import pandas

input_file_path: Path = Path.cwd().joinpath('day-1', 'part-1', 'input.csv')

unsorted: DataFrame = pandas.read_csv(input_file_path)

x: Series = Series(unsorted['x'])
y: Series = Series(unsorted['y'])

sorted_x: Series = x.sort_values(ignore_index=True)
sorted_y: Series = y.sort_values(ignore_index=True)

sorted: DataFrame = pandas.concat([sorted_x, sorted_y], axis=1)

sorted['distance'] = sorted.apply(lambda x: abs(x.loc['x'] - x.loc['y']), axis=1)

total_distance: int = sorted['distance'].sum()

print(f'answer: {total_distance}')
