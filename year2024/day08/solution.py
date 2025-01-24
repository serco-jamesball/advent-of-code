import year2024.utility as utility
from collections import defaultdict


Map = tuple[str]
Position = tuple[int, int]
Frequency = str


DAY: str = "8"

MAP_FILE_PATH: str = r"year2024\day08\resource\map.txt"

POINT: str = "."


def get_map(map_file_path: str) -> Map:
    with open(map_file_path) as map_file:
        return tuple(line for line in map_file.read().split())


def get_bounds(map: Map) -> tuple[int, int]:
    return len(map), len(map[0])


def get_antennas(map: Map) -> defaultdict[Frequency, set[Position]]:
    antennas: defaultdict[Frequency, set[Position]] = defaultdict(set[Position])

    for row, line in enumerate(map):
        for col, character in enumerate(line):
            if character != POINT:
                antennas[character].add((row, col))

    return antennas


def get_antinodes(
    antennas: defaultdict[Frequency, set[Position]], bounds: tuple[int, int]
) -> defaultdict[Frequency, set[Position]]:
    antinodes: defaultdict[Frequency, set[Position]] = defaultdict(set[Position])

    row_count, col_count = bounds

    for frequency, positions in antennas.items():
        for row, col in positions:
            for target_row, target_col in positions:
                if target_row == row or target_col == col:
                    # if (target_row, target_col) == (row, col):
                    continue

                antinode_row: int = row + row - target_row
                antinode_col: int = col + col - target_col

                if -1 < antinode_row < row_count and -1 < antinode_col < col_count:
                    antinodes[frequency].add((antinode_row, antinode_col))

    return antinodes


def get_part_1_answer(antinodes: defaultdict[Frequency, set[Position]]) -> int:
    return len({position for antinodes in antinodes.values() for position in antinodes})


def main() -> None:
    map: Map = get_map(MAP_FILE_PATH)

    bounds: tuple[int, int] = get_bounds(map)

    antennas: defaultdict[Frequency, set[Position]] = get_antennas(map)

    antinodes: defaultdict[Frequency, set[Position]] = get_antinodes(antennas, bounds)

    part_1_answer: int = get_part_1_answer(antinodes)

    print(utility.get_answer_message(DAY, part_1=part_1_answer))


if __name__ == "__main__":
    main()
