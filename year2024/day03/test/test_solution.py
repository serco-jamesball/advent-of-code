import pytest
import year2024.day03.solution as solution
from year2024.day03.solution import DoInstruction, MulInstruction


PART_1_CORRUPTED_MEMORY_FILE_PATH: str = (
    r"year2024\day03\test\resource\part_1_input.txt"
)
PART_2_CORRUPTED_MEMORY_FILE_PATH: str = (
    r"year2024\day03\test\resource\part_2_input.txt"
)
TEST_FIND_DO_INSTRUCTIONS_FILE_PATH: str = (
    r"year2024\day03\test\resource\test_find_do_instructions.txt"
)

PART_1_CORRUPTED_MEMORY_FRAGMENT_1: str = (
    r"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
)
PART_2_CORRUPTED_MEMORY_FRAGMENT_1: str = r"xmul(2,4)&mul[3,7]!^"
PART_2_CORRUPTED_MEMORY_FRAGMENT_2: str = r"?mul(8,5))"

PART_1_MUL_INSTRUCTIONS: list[MulInstruction] = [(2, 4), (5, 5), (11, 8), (8, 5)]
PART_2_MUL_INSTRUCTIONS: list[MulInstruction] = [(2, 4), (8, 5)]

PART_1_ANSWER: int = 161
PART_2_ANSWER: int = 48


def test_find_do_instructions() -> None:
    expected: list[DoInstruction] = [
        r"from()$&mul(602,165)why()mul(305,64)?(where()-:mul(80,703);)why()*from()%select()mul(290,957)}/?%'from()]mul(851,335)mul(844,49)what()]![from(667,522)]}how()how()mul(938,695)#/)*?@~?@select()mul(706,392)^mul(242,513)who()@]mul(871,132)( ] from()$mul(41,656)^{(&how()from()[when()-when()mul(628,478)mul(287,621)why():'mul(127,825)# ]mul(360,578)select()?^^select() @:why()mul(136,849);{how()%*@%+how()[mul(544,891)mul(436,21)from()}mul(184,294)+/from(81,871) how()&?]mul(297,492)select()/}%;$$~{*mul(161,703)when():+(,mul(335,695) ()&where()?who();'mul(689,420)^how()from()how()what()>]where()",
        r"''>~'$mul(109,905)}how(){!@where()%/mul(380,929)*){~:where()mul(547,552)$:*mul(58,881)where(145,89)[why(634,213)mul(699,443)mul(826,660)what()from()-how()}'from()what()<;mul(700,665)] #(*?how()<+mul(507,719))~*/-^(%mul(941,551)$;",
        r"@when()why()from()mul(975,883);select()who()mul(165,847)why();^/{^mul(31,153)?;'",
        r"*#mul(543,422)^*from()/^#~do()mul(832,873)]#when(455,108)^}who()/]mul(448,716)why()#/&mul(319,598)when()]{/ /'why()mul(865,894): +what()>from()+})what()mul(262,509)!*where()}/-#~/mul(308,953);*!]mul(741,76)[mul(256,536)[)>%-who()<^[$mul(382,338)where()[ when():select()<>mul(993,630)@$mul(411,640)/+where(623,926)/~mul(807,676)+*],mul(579,979who()what()from()when()how()what(),mul(882,434)&who()'mul(154,824)from()#<<,,{where()$mul(259,438)from()}?:;mul(641,967?from())<,>~mul(325,912)%select()mul where()do()where()where();(!,[$why()mul(131,307)mul(323,794)mul(570,548+!$from()!}what(588,195)<select()select()mul(622,782)why()mul(304,116)${(mul(942,260why()[?<$mul(420,225);~,>-from()mul(319,524)!/why()mul(737,137)+^&]/mul(228,919)@mul(672,604)+when(773,127)select()+why(941,245)mul(121!<[?$?;from(987,370):mul(904,487)#^what()from()({?mul(791,791)!,::)@^(mul(517,686)what()*how(),why()&mul(218,978)#,who()&$who()how(205,211)where()[mul(70,357)^$[?^$^what()mul(245,237)where()why()?{/mul$when()+},why()mul(264,30)@*:when(628,215):+&why()[mul(346,794){:}~-,select(),mul(115,926)~mul(140,56)[/:#~",
    ]

    with open(TEST_FIND_DO_INSTRUCTIONS_FILE_PATH) as corrupted_memory_file:
        corrupted_memory: str = corrupted_memory_file.read()

    foo = solution.find_do_instructions(corrupted_memory)

    assert solution.find_do_instructions(corrupted_memory) == expected


@pytest.mark.parametrize(
    "corrupted_memory, expected",
    [
        (PART_1_CORRUPTED_MEMORY_FRAGMENT_1, PART_1_MUL_INSTRUCTIONS),
        (PART_2_CORRUPTED_MEMORY_FRAGMENT_1, [PART_2_MUL_INSTRUCTIONS[0]]),
        (PART_2_CORRUPTED_MEMORY_FRAGMENT_2, [PART_2_MUL_INSTRUCTIONS[1]]),
    ],
)
def test_find_mul_instructions(
    corrupted_memory: str, expected: list[MulInstruction]
) -> None:
    assert solution.find_mul_instructions(corrupted_memory) == expected


@pytest.mark.parametrize(
    "corrupted_memory_file_path, is_processing_of_do_instructions_enabled, expected",
    [
        (PART_1_CORRUPTED_MEMORY_FILE_PATH, False, PART_1_MUL_INSTRUCTIONS),
        (PART_2_CORRUPTED_MEMORY_FILE_PATH, True, PART_2_MUL_INSTRUCTIONS),
    ],
)
def test_scan_corrupted_memory(
    corrupted_memory_file_path: str,
    is_processing_of_do_instructions_enabled: bool,
    expected: list[MulInstruction],
) -> None:
    with open(corrupted_memory_file_path) as corrupted_memory_file:
        corrupted_memory: str = corrupted_memory_file.read().strip()

        assert (
            solution.scan_corrupted_memory(
                corrupted_memory, is_processing_of_do_instructions_enabled
            )
            == expected
        )


@pytest.mark.parametrize(
    "mul_intructions, expected",
    [
        (PART_1_MUL_INSTRUCTIONS, PART_1_ANSWER),
        (PART_2_MUL_INSTRUCTIONS, PART_2_ANSWER),
    ],
)
def test_sum_mul_instructions(
    mul_intructions: list[MulInstruction], expected: int
) -> None:
    assert solution.sum_mul_instructions(mul_intructions) == expected


@pytest.mark.parametrize(
    "corrupted_memory_file_path, is_processing_of_do_instructions_enabled, expected",
    [
        (PART_1_CORRUPTED_MEMORY_FILE_PATH, False, PART_1_ANSWER),
        (PART_2_CORRUPTED_MEMORY_FILE_PATH, True, PART_2_ANSWER),
    ],
)
def test_run_program(
    corrupted_memory_file_path: str,
    is_processing_of_do_instructions_enabled: bool,
    expected: int,
) -> None:
    assert (
        solution.run_program(
            corrupted_memory_file_path, is_processing_of_do_instructions_enabled
        )
        == expected
    )
