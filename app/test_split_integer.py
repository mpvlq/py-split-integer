from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parts = split_integer(32, 6)
    assert (
        sum(parts) == 32
    ), "Sum of parts should be equal to 32"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parts = split_integer(6, 2)
    for part in parts:
        assert (
            part == parts[0]
        ), ("Every part should be equal if "
            "value is divisible by number of parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert (
        split_integer(31, 1) == [31]
    ), "Part should be equal if value if number of parts is 1"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert (
        split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    ), "Parts should be sorted if they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert (
        split_integer(3, 6)[: -3] == [0, 0, 0]
    ), "Function should add zeros if value is less than number of parts"
