import pytest


def test_return_array_recursion_error(return_types):
    with pytest.raises(RecursionError):
        return_types.return_uint256_array()


def test_return_tuples_uint256_array(return_types):
    with pytest.raises(RecursionError):
        assert return_types.return_tuples_uint256_array() == ([0] * 20, [0] * 20)


def test_return_tuples_uint256(return_types):
    assert return_types.return_tuples_uint256() == (0, 0)
