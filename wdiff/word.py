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

    def check_shared_phonemes(self):
        """Count how many graphemes that share phonemes with other graphemes
        are in the word.

        Returns
        -------
        None
        """

        shared_phoneme_s_count = self._check_shared_phoneme_s()
        shared_phoneme_j_count = self._check_shared_phoneme_j()
        shared_phoneme_k_count = self._check_shared_phoneme_k()
        shared_phoneme_y_count = self._check_shared_phoneme_y()
        shared_phoneme_b_count = self._check_shared_phoneme_b()

        self._shared_phonemes = (
            shared_phoneme_s_count
            + shared_phoneme_j_count
            + shared_phoneme_k_count
            + shared_phoneme_y_count
            + shared_phoneme_b_count
        )

    def _check_shared_phoneme_s(self):
        """Count how many graphemes that share the /s/ phoneme are in the word.

        Returns
        -------
        shared_phoneme_s_count: int
            Number of graphemes that share the /s/ phoneme in the word
        """

        z_count = self._text.count("z")
        s_count = self._text.count("s")
        c_with_s_sound_count = self._text.count("ci") + self._text.count("ce")
        shared_phoneme_s_count = z_count + s_count + c_with_s_sound_count

        return shared_phoneme_s_count

    def _check_shared_phoneme_b(self):
        """Count how many graphemes that share the /b/ phoneme are in the word.

        Returns
        -------
        shared_phoneme_b_count: int
            Number of graphemes that share the /b/ phoneme in the word
        """

        b_count = self._text.count("b")
        v_count = self._text.count("v")
        shared_phoneme_b_count = b_count + v_count

        return shared_phoneme_b_count

    def _check_shared_phoneme_y(self):
        """Count how many graphemes that share the /y/ phoneme are in the word.

        Returns
        -------
        shared_phoneme_y_count: int
            Number of graphemes that share the /y/ phoneme in the word
        """

        ll_count = self._text.count("ll")

        y_count = self._text.count("y")
        if self._text[-1] == "y":
            y_count -= 1

        shared_phoneme_y_count = ll_count + y_count

        return shared_phoneme_y_count

    def _check_shared_phoneme_j(self):
        """Count how many graphemes that share the /j/ phoneme are in the word.

        Returns
        -------
        shared_phoneme_j_count: int
            Number of graphemes that share the /j/ phoneme in the word
        """

        j_count = self._text.count("j")
        g_compliant_count = self._text.count("ge") + self._text.count("gi")
        shared_phoneme_j_count = j_count + g_compliant_count

        return shared_phoneme_j_count

    def _check_shared_phoneme_k(self):
        """Count how many graphemes that share the /k/ phoneme are in the word.

        Returns
        -------
        shared_phoneme_k_count: int
            Number of graphemes that share the /k/ phoneme in the word
        """

        k_count = self._text.count("k")
        q_count = self._text.count("q") 
        c_compliant_count = (
            self._text.count("ca")
            + self._text.count("co")
            + self._text.count("cu")
        )
        shared_phoneme_k_count = k_count + q_count + c_compliant_count

        return shared_phoneme_k_count

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
