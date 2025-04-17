import pytest
import types
from flat_generator import flat_generator

@pytest.mark.parametrize("input_data, expected_output", [
    (
        [['a', 'b'], ['c', 'd']],
        ['a', 'b', 'c', 'd']
    ),
    (
        [[1, 2, 3], [4], [5, 6]],
        [1, 2, 3, 4, 5, 6]
    ),
    (
        [[], ['x'], []],
        ['x']
    ),
    (
        [[], []],
        []
    ),
    (
        [[None], [False, True]],
        [None, False, True]
    )
])
def test_flat_generator_output(input_data, expected_output):
    assert list(flat_generator(input_data)) == expected_output

def test_flat_generator_returns_generator():
    input_data = [[1, 2], [3]]
    gen = flat_generator(input_data)
    assert isinstance(gen, types.GeneratorType)
