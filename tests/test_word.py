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

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # s
        ("perro", 0),
        ("sopa", 1),
        ("salsa", 2),
        # z
        ("zanahoria", 1),
        ("zarpazo", 2),
        # c compliant
        ("citronela", 1),
        ("celda", 1),
        ("decencia", 2),
        # c non compliant
        ("carro", 0),
        ("educador", 0),
        # c compliant and non compliant
        ("concurrencia", 1),
        ("convivencia", 1),
        # combined 
        ("adolescencia", 3),
        ("adolescencia", 3),
        ("acidez", 2),
        ("castizo", 2),
    ]
)
def test_check_shared_phoneme_s(text, expected):
    """Test the _check_shared_phoneme_s function with different types of cases."""

    word = Word(text)
    observed = word._check_shared_phoneme_s()

    assert observed == expected

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # b
        ("perro", 0),
        ("bola", 1),
        ("burbuja", 2),
        # v
        ("advierte", 1),
        ("invasivo", 2),
        # mixed
        ("absolver", 2),
        ("observatorio", 2),
    ]
)
def test_check_shared_phoneme_b(text, expected):
    """Test the _check_shared_phoneme_b function with different types of cases."""

    word = Word(text)
    observed = word._check_shared_phoneme_b()

    assert observed == expected

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # none
        ("perro", 0),
        # ll
        ("lluvia", 1),
        # y
        ("yate", 1),
        ("yoyo", 2),
        ("hoy", 0),
        ("rey", 0),
    ]
)
def test_check_shared_phoneme_y(text, expected):
    """Test the _check_shared_phoneme_y function with different types of cases."""

    word = Word(text)
    observed = word._check_shared_phoneme_y()

    assert observed == expected
