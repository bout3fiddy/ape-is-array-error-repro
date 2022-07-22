# @version 0.3.3

@external
@view
def return_uint256_array() -> uint256[20]:
    return empty(uint256[20])


@external
@view
def return_tuples_uint256_array() -> (uint256[20], uint256[20]):
    return (empty(uint256[20]), empty(uint256[20]))


@external
@view
def return_tuples_uint256() -> (uint256, uint256):
    return (0, 0)
