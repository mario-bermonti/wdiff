class Word(object):
    """Base class for all analyses. It conceptualizes words as objects with
    features, where each feature corresponds to a characteristic of the word.

    The Word class is aware of its characteristics and knows how to determine
    them.

    The word's features supported are:
    - word length
    - silent letters
    - graphemes that share phonemes with other graphemes (grapheme-to-phoneme correspondence)
    - total difficulty
    """

    def __init__(self, text):
        text = self._normalize_text(text)
        self._validate_word(text)
        self._text = text
        self._length = None
        self._silent_letters = None
        self._shared_phonemes = None
        self._total_difficulty = None

    def _normalize_text(self, text):
        """Normalize text so it is properly formatted.

        Parameters
        ----------
        text : str
            word's text

        Returns
        -------
        word_normalized : str
            word's text
        """

        word_normalized = text.strip().lower()

        return word_normalized


    def _validate_word(self, text):
        """Validate that the word's text meets minimal requirements.

        Parameters
        ----------
        text: str
            Spanish word to build for analysis

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If _word_length_is_invalid or if _word_contains_invalid_character
            return True
        """

        if (
            self._word_length_is_invalid(text)
            or self._word_contains_invalid_character(text)
        ):
            raise ValueError(f"\'{text}\' is invalid for creating word")


    def _word_length_is_invalid(self, text):
        """Checks whether the word's text length is invalid.

        Parameters
        ----------
        text : str
            Spanish word to build for analysis

        Returns
        -------
        Bool 
            True if the length is 0 False; False if it is different than 0
        """

        return len(text) == 0

    def _word_contains_invalid_character(self, text):
        """Checks whether the text provided for the word contains invalid characters.

        Parameters
        ----------
        text : str
            Spanish word to build for analysis

        Returns
        -------
        Bool
            True if the text is contains invalid characters; False otherwise
        """

        valid_characters = "aábcdeéfghiíjklmnñoópqrstuúüvwxyz "
        for char in text:
            if char not in valid_characters:
                return True
        return False


    def _check_silent_letters(self):
        """Count the number of silent letters in the word.

        Silent letters are graphemes that do not have a phonemic representation.
        In Spanish, silent letters are *h*s and *u*s that meet certain criteria. 

        Rules
        -----
        TODO Add reference to rules

        Returns
        -------
        silent_letter_count : int
            Number of silent letters.
        """

        silent_u_count = self._check_silent_u()
        silent_h_count = self._check_silent_h()

        silent_letter_count = silent_u_count + silent_h_count

        return silent_letter_count

    def _check_silent_u(self):
        """Count how many silent letters *u* there are in the word.

        Rules
        -----
        - Silent letter *u*: letter *u* that is preceded by an *g* or *q* and
        followed by a *i* or *e*. These follow the pattern *gui*, *gue*,
        *que*, *qui*. 

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

        Rules
        -----
        - Silent letter *h*: letter *h* that is not preceded by a letter *c*.

        Returns
        -------
        silent_h_count: int
            Number of silent letters h in the word
        """

        h_count = self._text.count("h")
        h_noncomplian_count = self._text.count("ch")

        silent_h_count = h_count - h_noncomplian_count

        return silent_h_count

    def _check_shared_phonemes(self):
        """Count how many graphemes that share phonemes with other graphemes
        are in the word.

        Graphemes that share phonemes with other graphemes are 
        letters or combination of letters that represent the same sound
        as other letters or combination of letters.

        Rules
        -----
        TODO Add reference to rules

        Returns
        -------
        shared_phoneme_count : int
            Number of shared phonemes.
        """

        shared_phoneme_s_count = self._check_shared_phoneme_s()
        shared_phoneme_j_count = self._check_shared_phoneme_j()
        shared_phoneme_k_count = self._check_shared_phoneme_k()
        shared_phoneme_y_count = self._check_shared_phoneme_y()
        shared_phoneme_b_count = self._check_shared_phoneme_b()

        shared_phoneme_count = (
            shared_phoneme_s_count
            + shared_phoneme_j_count
            + shared_phoneme_k_count
            + shared_phoneme_y_count
            + shared_phoneme_b_count
        )

        return shared_phoneme_count

    def _check_shared_phoneme_s(self):
        """Count how many graphemes that share the /s/ phoneme are in the word.

        Rules
        -----
        - Any letter *z*
        - Any letter *s*
        - Letter *c* that is followed by an *i* or *e*

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

        Rules
        -----
        - Any letter *b*
        - Any letter *v*

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

        Rules
        -----
        - Letter *l*: If it is next to another letter *l* (i.e., *ll*)
        - Letter *y*: Any letter *y* that is not at the end of the word

        Returns
        -------
        shared_phoneme_y_count: int
            Number of graphemes that share the /y/ phoneme in the word
        """

        ll_count = self._text.count("ll")

        y_count = self._text.count("y")  # TODO improve algorithm
        if self._text[-1] == "y":
            y_count -= 1

        shared_phoneme_y_count = ll_count + y_count

        return shared_phoneme_y_count

    def _check_shared_phoneme_j(self):
        """Count how many graphemes that share the /j/ phoneme are in the word.

        Rules
        -----
        - Any letter *j*
        - Letter *g*: when followed by an *e* or *i*

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

        Rules
        -----
        - Any letter *k*
        - Any letter *q*
        - Letter *c*: when followed by an *a*, *o* or *u*

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

    def _calculate_total_difficulty(self):
        """Calculate the total difficulty for the word.

        This is the sum of all other characteristics. It is taken to indicate
        how difficult is to spell a word. This information can be particularly
        useful if this *difficulty index* is compared to the index of
        other words.

        Only the characteristics that have a value valid int value are used.

        Returns
        -------
        int
            Total difficulty for the word

        Raises
        ------
        ValueError
            If none of the analyses has been run (are None).
        """

        characteristics = [self._length, self._silent_letters, self._shared_phonemes]

        if characteristics.count(None) == len(characteristics):
            print("ValueError: total_dificulty cannot be calculated because no analysis has been conducted")
            raise ValueError

        characteristic_valid = [characteristic
                                for characteristic in characteristics
                                if characteristic is not None
                                ]
        total_difficulty = sum(characteristic_valid)

        return total_difficulty

    @property
    def text(self):
        return self._text

    @property
    def length(self):
        if self._length is None:
            self._length = len(self._text)

        return self._length

    @property
    def silent_letters(self):
        if self._silent_letters is None:
            self._silent_letters = self._check_silent_letters()

        return self._silent_letters

    @property
    def shared_phonemes(self):
        if self._shared_phonemes is None:
            self._shared_phonemes = self._check_shared_phonemes()

        return self._shared_phonemes

    @property
    def total_difficulty(self):
        if self._total_difficulty is None:
            self._total_difficulty = self._calculate_total_difficulty()

        return self._total_difficulty

