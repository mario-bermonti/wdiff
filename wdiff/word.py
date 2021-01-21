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
        self._total_difficulty = None

    def check_silent_letters(self):
        """Count how many silent letters there are in the word.

        Returns
        -------
        None
        """

        silent_u_count = self._check_silent_u()
        silent_h_count = self._check_silent_h()

        self._silent_letters = silent_u_count + silent_h_count

    def _check_silent_u(self):
        """Count how many silent letters *u* there are in the word.

        Returns
        -------
        silent_u_count: int
            Number of silent letters u in the word
        """

        silent_u_count = (
            self._text.count("que")
            + self._text.count("qui")
            + self._text.count("gue")
            + self._text.count("gui")
        )

        return silent_u_count

    def _check_silent_h(self):
        """Count how many silent letters *h* there are in the word.

        Returns
        -------
        silent_h_count: int
            Number of silent letters h in the word
        """

        h_count = self._text.count("h")
        h_noncomplian_count = self._text.count("ch")

        silent_h_count = h_count - h_noncomplian_count

        return silent_h_count

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
