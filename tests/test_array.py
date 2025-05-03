from typing import Any

import pytest

from essential_building_blocks.data_structures.lists import Array

def test_init():
    array = Array(3)
    assert array.size == 3
    assert array.dtype is None

    array = Array(3, int)
    assert array.size == 3
    assert array.dtype == int

    array = Array(3, Any)
    assert array.size == 3
    assert array.dtype == Any

    with pytest.raises(TypeError):
        Array("3")

    with pytest.raises(ValueError):
        Array(-1)

    with pytest.raises(TypeError):
        Array(3.0)

    with pytest.raises(TypeError):
        Array(3, "int")

    with pytest.raises(TypeError):
        Array(3, 3)

def test_size():
    array = Array(3)
    assert array.size == 3

    with pytest.raises(AttributeError):
        array.size = "3"

    with pytest.raises(AttributeError):
        array.size = 3.0

    with pytest.raises(AttributeError):
        array.size = 3

def test_dtype():
    array = Array(3)
    assert array.dtype is None

    array = Array(3, int)
    assert array.dtype == int

    with pytest.raises(AttributeError):
        array.dtype = int

    with pytest.raises(AttributeError):
        array.dtype = "int"

def test_length():
    array = Array(3)
    assert len(array) == 3

    array = Array(3, int)
    assert len(array) == 3

    array = Array(100, int)
    assert len(array) == 100

def test_set_get_item():
    array = Array(3, int)
    array[0] = 1
    array[1] = 2
    array[2] = 3

    assert array[0] == 1
    assert array[1] == 2
    assert array[2] == 3
    assert array[-1] == 3
    assert array[1:3] == [2, 3]

    with pytest.raises(IndexError):
        array[3] = 4

    with pytest.raises(IndexError):
        temp = array[3]

    with pytest.raises(TypeError):
        array[0] = "1"

    with pytest.raises(TypeError):
        array[0] = 1.0

def test_iter():
    array = Array(3, int)
    array[0] = 1
    array[1] = 2
    array[2] = 3
    assert list(array) == [1, 2, 3]

    for element in array:
        assert element in [1, 2, 3]

def test_str():
    array = Array(3, int)
    array[0] = 1
    array[1] = 2
    array[2] = 3
    assert str(array) == str(list(array))

def test_repr():
    array = Array(3, int)
    array[0] = 1
    array[1] = 2
    array[2] = 3
    assert repr(array) == f"Array(size={array.size}, dtype={array.dtype})"

def test_from_sequence():
    sequence1: list[int] = [1, 2, 3]
    sequence2: tuple[int, int, int] = (1, 2, 3)
    sequence3: str = "123"

    array1 = Array.from_sequence(sequence1)
    assert array1.size == 3
    assert array1.dtype == int
    assert array1[0] == 1
    assert array1[1] == 2
    assert array1[2] == 3

    array2 = Array.from_sequence(sequence2)
    assert array2.size == 3
    assert array2.dtype == int
    assert array2[0] == 1
    assert array2[1] == 2
    assert array2[2] == 3

    array3 = Array.from_sequence(sequence3)
    assert array3.size == 3
    assert array3.dtype == str
    assert array3[0] == '1'
    assert array3[1] == '2'
    assert array3[2] == '3'

    with pytest.raises(TypeError):
        Array.from_sequence(bool)

    with pytest.raises(TypeError):
        Array.from_sequence(1)

    with pytest.raises(TypeError):
        seq = [1, "2"]
        Array.from_sequence(seq)

def test_operations():
    array = Array(3, int)
    array[0] = 1
    array[1] = 2
    array[2] = 3

    assert 1 in array
    assert not(4 in array)

    assert min(array) == 1
    assert max(array) == 3
    assert sum(array) == 6
    assert array.count(1) == 1

    with pytest.raises(AttributeError):
        array + array

    with pytest.raises(AttributeError):
        array + [1, 2, 3]

    with pytest.raises(AttributeError):
        [1, 2, 3] + array

    with pytest.raises(AttributeError):
        array += [1, 2, 3]

    with pytest.raises(AttributeError):
        array * array

    with pytest.raises(AttributeError):
        array * [1, 2, 3]

    with pytest.raises(AttributeError):
        [1, 2, 3] * array

    with pytest.raises(AttributeError):
        array *= [1, 2, 3]