from wdiff.word import Word

import pytest

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # none
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
        # none
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
        # none
        ("perro", 0),
        # s
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
        # none
        ("perro", 0),
        # b
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

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # none
        ("perro", 0),
        # j
        ("jaula", 1),
        # g
        ("girar", 1),
        ("gato", 0),
        # mixed
        ("jengibre", 2),
        ("jaguar", 1),
        ("juguete", 1),
    ]
)
def test_check_shared_phoneme_j(text, expected):
    """Test the _check_shared_phoneme_j function with different types of cases."""

    word = Word(text)
    observed = word._check_shared_phoneme_j()

    assert observed == expected

@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # none
        ("perro", 0),
        # k
        ("koala", 1),
        ("karaoke", 2),
        # c
        ("calabaza", 1),
        ("concordar", 2),
        ("circo", 1),
        # q
        ("queso", 1),
        ("quisquilloso", 2),
        # mixed
        ("kiosco", 2),
        ("quince", 1),
        ("cosquillas", 2),
    ]
)
def test_check_shared_phoneme_k(text, expected):
    """Test the _check_shared_phoneme_k function with different types of cases."""

    word = Word(text)
    observed = word._check_shared_phoneme_k()

    assert observed == expected

@pytest.mark.parametrize(
    ("difficulty_length", "difficulty_silent", "difficulty_shared_phonemes", "total_difficulty_expected"),
    [
        # all ints
        (1, 2, 3, 6),
        # mixed
        (1, None, 3, 4),
    ]
)
def test_calculate_overall_difficulty(
        difficulty_length,
        difficulty_silent,
        difficulty_shared_phonemes,
        total_difficulty_expected
):
    """Test the _calculate_overall_difficulty."""

    word = Word("ejemplo")
    word._length = difficulty_length
    word._silent_letters = difficulty_silent
    word._shared_phonemes = difficulty_shared_phonemes
    total_difficulty_observed = word._calculate_total_difficulty()

    assert total_difficulty_observed == total_difficulty_expected


def test_calculate_overall_difficulty_none_valid():
    """Test the _calculate_overall_difficulty when none of the
    characteristics are valid.
    """

    word = Word("ejemplo")
    word._length = None
    word._silent_letters = None
    word._shared_phonemes = None

    with pytest.raises(ValueError):
        total_difficulty_observed = word._calculate_total_difficulty()

