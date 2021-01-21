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
def test_check_silent_h(text, expected):
    """Test the check_silent_h function with different types of cases."""

    word = Word(text)
    observed = word._check_silent_h()

    assert observed == expected

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # no us
        ("oso", 0),
        ("perro", 0),
        # non silent us
        ("urbano", 0),
        ("contigua", 0),
        ("uruguayo", 0),
        # silent us
        ("guiso", 1),
        ("dengue", 1),
        ("quieto", 1),
        ("quebrar", 1),
        ("panqueque", 2),
        ("quisquilloso", 2),
        # silent and non silent us
        ("huelguista", 1),
        ("conjugues", 1),
        ("quietud", 1),
        ("aunque", 1),
    ]
)
def test_check_silent_u(text, expected):
    """Test the check_silent_u function with different types of cases."""

    word = Word(text)
    observed = word._check_silent_u()

    assert observed == expected
