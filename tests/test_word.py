from wdiff.word import Word

import pytest

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # no hs
        ("oso", 0),
        ("perro", 0),
        # non silent hs
        ("cacharro", 0),
        ("muchacho", 0),
        # silent hs
        ("habitual", 1),
        ("huevo", 1),
        ("hispanohablante", 2),
        # silent and non silent hs
        ("habichuela", 1),
        ("hecho", 1),
        ("chihuahua", 2),
    ]
)
def test_check_silent_h_(text, expected):
    """Test the check_silent_h function with different types of cases."""

    word = Word(text)
    observed = word._check_silent_h()

    assert observed == expected
