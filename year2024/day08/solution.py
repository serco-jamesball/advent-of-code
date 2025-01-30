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
    antennas: defaultdict[Frequency, set[Position]],
    bounds: tuple[int, int],
    is_resonant_harmonics_effect_applied: bool,
) -> defaultdict[Frequency, set[Position]]:
    antinodes: defaultdict[Frequency, set[Position]] = defaultdict(set[Position])

    row_count, col_count = bounds

    for frequency, positions in antennas.items():
        for row, col in positions:
            for target_row, target_col in positions:
                if target_row == row or target_col == col:
                    continue

                row_offset: int = row - target_row
                col_offset: int = col - target_col

                if is_resonant_harmonics_effect_applied:
                    for direction in (1, -1):
                        antinode_row: int = row + direction * row_offset
                        antinode_col: int = col + direction * col_offset

                        while (
                            -1 < antinode_row < row_count
                            and -1 < antinode_col < col_count
                        ):
                            antinodes[frequency].add((antinode_row, antinode_col))

                            antinode_row += direction * row_offset
                            antinode_col += direction * col_offset
                else:
                    antinode_row: int = row + row_offset
                    antinode_col: int = col + col_offset

                    if -1 < antinode_row < row_count and -1 < antinode_col < col_count:
                        antinodes[frequency].add((antinode_row, antinode_col))

    return antinodes


def get_answer(antinodes: defaultdict[Frequency, set[Position]]) -> int:
    return len({position for antinodes in antinodes.values() for position in antinodes})


def main() -> None:
    map: Map = get_map(MAP_FILE_PATH)

    bounds: tuple[int, int] = get_bounds(map)

    antennas: defaultdict[Frequency, set[Position]] = get_antennas(map)

    part_1_antinodes: defaultdict[Frequency, set[Position]] = get_antinodes(
        antennas, bounds, False
    )
    part_1_answer: int = get_answer(part_1_antinodes)

    part_2_antinodes: defaultdict[Frequency, set[Position]] = get_antinodes(
        antennas, bounds, True
    )
    part_2_answer: int = get_answer(part_2_antinodes)

    print(utility.get_answer_message(DAY, part_1=part_1_answer, part_2=part_2_answer))


if __name__ == "__main__":
    main()
