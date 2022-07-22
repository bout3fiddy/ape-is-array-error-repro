import pytest

def test_return_array_recursion_error(return_types):
    with pytest.raises(RecursionError):
        return_types.return_uint256_array()
        