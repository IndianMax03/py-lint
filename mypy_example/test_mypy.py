def add(a: int, b: int) -> int:
    return a + b

def test_type() -> None:
    total = add("15", 3)
    assert total > 0
    result = add_num(16, 16)
    assert result == 32
