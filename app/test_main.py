import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("NIOcean", True),
    ("I Love Mate academy", False),
    ("wrong", True),
    ("brother", False),
    ("Ukraine", True),
    ("", True)
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
