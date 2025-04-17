import pytest
from flat_iterator import FlatIterator


@pytest.mark.parametrize("input_data, expected_output", [
    (
        [['a', 'b', 'c'], ['d', 'e'], ['f']],
        ['a', 'b', 'c', 'd', 'e', 'f']
    ),
    (
        [[], [1, 2], [], [3]],
        [1, 2, 3]
    ),
    (
        [[None], [False, True]],
        [None, False, True]
    ),
    (
        [[1], [], [], [2, 3]],
        [1, 2, 3]
    ),
    (
        [],
        []
    )
])
def test_flat_iterator_output(input_data, expected_output):
    assert list(FlatIterator(input_data)) == expected_output


def test_flat_iterator_is_iterable():
    data = [[10], [20, 30]]
    flat_iter = FlatIterator(data)
    assert iter(flat_iter) is flat_iter