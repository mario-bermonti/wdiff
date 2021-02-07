import pytest

from wdiff.word import Word


@pytest.mark.parametrize("text", ["perro", "gato", "pájaro"])
def test_create_word_objects(text):
    """Test the _create_word_objects with different cases."""

    word = Word(text)

    assert isinstance(word, Word)
    assert word.text == text
