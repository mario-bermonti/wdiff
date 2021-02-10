import pytest

from wdiff.analyzer import Analyzer
from wdiff.word import Word


@pytest.mark.parametrize("text", ["perro", "gato", "pájaro"])
def test_create_word_objects(text):
    """Test the _create_word_objects with different cases."""

    word = Word(text)

    assert isinstance(word, Word)
    assert word.text == text


@pytest.mark.parametrize(
    ("word_property", "word_properties_exp"), 
    [
        ("text", ["huevo", "guitarra", "calabaza", "gigante"]),
        ("length", [5, 8, 8, 7]),
        ("silent_letters", [1, 1, 0, 0]),
        ("shared_phonemes", [1, 0, 3, 1]),
    ]
)
def test_get_property_from_words(word_property, word_properties_exp):
    """Test the _get_property_from_words for each property."""

    text_list = ["huevo", "guitarra", "calabaza", "gigante"]
    # create analyzer
    analyzer = Analyzer(text_list)

    # get prop
    word_properties_obs = analyzer._get_property_from_words(word_property)

    # verify
    assert word_properties_obs.to_list() == word_properties_exp

@pytest.mark.parametrize(
    ("difficulty_length", "difficulty_silent", "difficulty_shared_phonemes", "total_difficulty_exp"),
    [
        # all ints
        (1, 2, 3, 6),
        # mixed
        (1, None, 3, 4),
    ]
)
def test_calculate_total_difficulty(
        difficulty_length,
        difficulty_silent,
        difficulty_shared_phonemes,
        total_difficulty_exp
):
    """Test the _get_property_from_words with the total_difficulty property.

    .. note::
       This test is done in a separate from the test for getting other
       properties because it depends on other properties of the word
       that have to be set manually.
    """

    analyzer = Analyzer(["ejemplo"])
    word_obj = analyzer._results.word_objs[0]
    word_obj._length = difficulty_length
    word_obj._silent_letters = difficulty_silent
    word_obj._shared_phonemes = difficulty_shared_phonemes
    total_difficulty_obs = analyzer._get_property_from_words("total_difficulty")

    assert total_difficulty_obs.to_list()[0] == total_difficulty_exp
