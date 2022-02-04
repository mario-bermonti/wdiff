"""Module that defines the Word class."""

from .docsprocessor import docstrings, _COMMON_SECTIONS

###########################################################################
# Note                                                                    #
###########################################################################
# The order of the methods is important for the docstrings to be build    #
# correctly. This is because docrep reads and builds docstrings as they   #
# are evaluated by python and the docstrings from which the text is       #
# taken have to be evaluated before they can be used in other strings.    #
#                                                                         #
# There is an alternative, but it is too messy.                           #
#                                                                         #
# The same applies to methods that are properties. The docstrings have to #
# build before the method can be converted into properties.               #
###########################################################################

class Word(object):
    """Base class for all analyses. It conceptualizes words as objects with
    features, where each feature corresponds to a characteristic of the word.

    The Word class is aware of its characteristics and knows how to determine
    them.

    The following word features are supported:
    - word length
    - silent letters
    - shared phonemes: graphemes that share phonemes with other graphemes
      This is related to the grapheme-to-phoneme correspondence.
    - total difficulty
    """

    def __init__(self, text):
        """
        Parameters
        ----------
        text: str
            Text to use for creating the Word object.
        """

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
            True if the length is 0 False; False if it is not 0
        """

        return len(text) == 0

    def _word_contains_invalid_character(self, text):
        """Checks whether the word's text contains invalid characters.

        Parameters
        ----------
        text : str
            Spanish word to build for analysis

        Returns
        -------
        Bool
            True if the text contains invalid characters; False otherwise
        """

        valid_characters = "aábcdeéfghiíjklmnñoópqrstuúüvwxyz "
        for char in text:
            if char not in valid_characters:
                return True
        return False

    @docstrings.get_sections(base="silent_u", sections=_COMMON_SECTIONS)
    def _check_silent_u(self):
        """Count the number of silent letters *u*.

        Rules
        -----
        *u*: when preceded by an *g* or *q* and followed by a *i* or *e*.
             These follow the pattern *gui*, *gue*, *que*, *qui*. 

        Returns
        -------
        silent_u_count: int
            Number of silent letters *u* in the word
        """

        silent_u_count = (
            self._text.count("que")
            + self._text.count("qui")
            + self._text.count("gue")
            + self._text.count("gui")
        )

        return silent_u_count

    @docstrings.get_sections(base="silent_h", sections=_COMMON_SECTIONS)
    def _check_silent_h(self):
        """Count the number of silent letters *h*.

        Rules
        -----
        *h*: when is not preceded by a letter *c*.

        Returns
        -------
        silent_h_count: int
            Number of silent letters *h* in the word
        """

        h_count = self._text.count("h")
        h_noncomplian_count = self._text.count("ch")

        silent_h_count = h_count - h_noncomplian_count

        return silent_h_count

    @docstrings.get_sections(
        base="silent_letters",
        sections=["Rules", "Returns"]
    )
    @docstrings.get_extended_summary(base="silent_letters")
    @docstrings.with_indent(8)
    def _check_silent_letters(self):
        """Count the number of silent letters.

        Silent letters are graphemes that do not have a phonemic representation.
        In Spanish, silent letters are *h*s and *u*s that meet certain criteria. 

        Rules
        -----
        %(silent_u.rules)s
        %(silent_h.rules)s

        Returns
        -------
        silent_letter_count : int
            Number of silent letters.
        """

        silent_u_count = self._check_silent_u()
        silent_h_count = self._check_silent_h()

        silent_letter_count = silent_u_count + silent_h_count

        return silent_letter_count

    @docstrings.get_sections(base="shared_s", sections=_COMMON_SECTIONS)
    def _check_shared_phoneme_s(self):
        """Count the number of graphemes that represent the /s/ phoneme.

        Rules
        -----
        *z*: Any letter *z*
        *s*: Any letter *s*
        *c*: when followed by an *i* or *e*

        Returns
        -------
        shared_phoneme_s_count: int
            Number of graphemes that represent the /s/ phoneme
        """

        z_count = self._text.count("z")
        s_count = self._text.count("s")
        c_with_s_sound_count = self._text.count("ci") + self._text.count("ce")
        shared_phoneme_s_count = z_count + s_count + c_with_s_sound_count

        return shared_phoneme_s_count

    @docstrings.get_sections(base="shared_b", sections=_COMMON_SECTIONS)
    def _check_shared_phoneme_b(self):
        """Count the number of graphemes that represent the /b/ phoneme.

        Rules
        -----
        *b*: Any letter *b*
        *v*: Any letter *v*

        Returns
        -------
        shared_phoneme_b_count: int
            Number of graphemes that represent the /b/ phoneme.
        """

        b_count = self._text.count("b")
        v_count = self._text.count("v")
        shared_phoneme_b_count = b_count + v_count

        return shared_phoneme_b_count

    @docstrings.get_sections(base="shared_y", sections=_COMMON_SECTIONS)
    def _check_shared_phoneme_y(self):
        """Count the number of graphemes that represent the /y/ phoneme.

        Rules
        -----
        *l*: If it is next to another letter *l* (i.e., *ll*)
        *y*: Any letter *y* that is not at the end of the word

        Returns
        -------
        shared_phoneme_y_count: int
            Number of graphemes that represent the /y/ phoneme.
        """

        ll_count = self._text.count("ll")

        y_count = self._text.count("y")  # TODO improve algorithm
        if self._text[-1] == "y":
            y_count -= 1

        shared_phoneme_y_count = ll_count + y_count

        return shared_phoneme_y_count

    @docstrings.get_sections(base="shared_j", sections=_COMMON_SECTIONS)
    def _check_shared_phoneme_j(self):
        """Count the number of graphemes that represent the /j/ phoneme.

        Rules
        -----
        *j*: Any letter *j*
        *g*: when followed by an *e* or *i*

        Returns
        -------
        shared_phoneme_j_count: int
            Number of graphemes that represent the /j/ phoneme.
        """

        j_count = self._text.count("j")
        g_compliant_count = self._text.count("ge") + self._text.count("gi")
        shared_phoneme_j_count = j_count + g_compliant_count

        return shared_phoneme_j_count

    @docstrings.get_sections(base="shared_k", sections=_COMMON_SECTIONS)
    def _check_shared_phoneme_k(self):
        """Count the number of graphemes that represent the /k/ phoneme.

        Rules
        -----
        *k*: Any letter *k*
        *q*: Any letter *q*
        *c*: when followed by an *a*, *o* or *u*

        Returns
        -------
        shared_phoneme_k_count: int
            Number of graphemes that represent the /k/ phoneme.
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

    @docstrings.get_sections(
        base="shared_phonemes",
        sections=["Rules", "Returns"]
    )
    @docstrings.get_extended_summary(base="shared_phonemes")
    @docstrings.with_indent(8)
    def _check_shared_phonemes(self):
        """Count the number of graphemes that share phonemes with other graphemes.

        Graphemes that share phonemes with other graphemes are 
        letters or combination of letters that represent the same sound
        as other letters or combination of letters.

        Rules
        -----
        %(shared_s.rules)s
        %(shared_b.rules)s
        %(shared_y.rules)s
        %(shared_j.rules)s
        %(shared_k.rules)s

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

    @docstrings.get_sections(
        base="total_difficulty",
        sections=["Returns", "Raises"]
    )
    @docstrings.get_extended_summary(base="total_difficulty")
    def _calculate_total_difficulty(self):
        """Calculate the total difficulty for the word.

        This is the sum of all other characteristics. It is interpreted as
        how difficult is to spell the word. This information can be particularly
        useful if this *difficulty index* is compared to the index of
        other words.

        Only the characteristics that have a valid value (int) are used.

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
        """Word's text."""

        return self._text

    @property
    def length(self):
        """Number of letters in the word."""

        if self._length is None:
            self._length = len(self._text)

        return self._length

    @property
    @docstrings.with_indent(8)
    def silent_letters(self):
        """Returns the number of silent letters in the word.

        %(silent_letters.summary_ext)s

        Rules
        -----
        %(silent_letters.rules)s

        Returns
        -----
        %(silent_letters.returns)s
        """

        if self._silent_letters is None:
            self._silent_letters = self._check_silent_letters()

        return self._silent_letters

    @property
    @docstrings.with_indent(8)
    def shared_phonemes(self):
        """Returns the number of shared phonemes in the word.

        %(shared_phonemes.summary_ext)s

        Rules
        -----
        %(shared_phonemes.rules)s

        Returns
        -------
        %(shared_phonemes.returns)s
        """

        if self._shared_phonemes is None:
            self._shared_phonemes = self._check_shared_phonemes()

        return self._shared_phonemes

    @property
    @docstrings.with_indent(8)
    def total_difficulty(self):
        """Returns the word's total difficulty.

        %(total_difficulty.summary_ext)s

        Returns
        -------
        %(total_difficulty.returns)s
        
        Raises
        ------
        %(total_difficulty.raises)s
        """

        if self._total_difficulty is None:
            self._total_difficulty = self._calculate_total_difficulty()

        return self._total_difficulty

