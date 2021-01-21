class Word(object):
    """Base class for all analyses. It conceptualizes words as objects with
    features, where each feature corresponds to a characteristic of the word.

    The Word class is aware of its characteristics and knows how to determine
    them.

    The word features are:
    - word length
    - silent letters: u, h
    - graphemes that share phonemes with other graphemes (grapheme-to-phoneme correspondence)
    - total difficulty: the sum of all other characteristics
    """

    def __init__(self, text):
        self._text = text
        self._length = len(text)
        self._silent_letters = None
        self._shared_phonemes = None
        self._shared_phonemes = None
        self._total_difficulty = None

    @property
    def text(self):
        return self._text

    @property
    def length(self):
        return self._length

    @property
    def silent_letters(self):
        return self._silent_letters

    @property
    def shared_phonemes(self):
        return self._shared_phonemes

    @property
    def total_difficulty(self):
        return self._total_difficulty
