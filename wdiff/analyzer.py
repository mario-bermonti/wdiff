"""Module that defines the api."""

import pandas as pd

from .word import Word
from .docsprocessor import docstrings, _COMMON_SECTIONS


class Analyzer(object):
    """This class exposes wdiff's API.
    
    It provides methods for creating word objects, running analyses, storing
    results, and saving results to a file.
    """

    def __init__(self, words):
        """
        Parameters
        ----------
        words : iterable, list-like object
            Contains the words to be analyzed.
        """

        self._results = pd.DataFrame()
        word_objs = self._create_word_objs(words)
        self._results["word_objs"] = word_objs
        self._add_words_text_to_results()

    def _create_word_objs(self, text_for_words):
        """Create a word object for each text.

        Parameters
        ----------
        text_for_words : iterable, list-like object
            Text to be used to create word objects.

        Returns
        -------
        word_objs : List of Words
            Word objects
        """

        word_objs = [Word(text) for text in text_for_words]

        return word_objs

    def _get_property_from_words(self, word_property):
        """Get property of all words.

        Parameters
        ----------
        word_property : str
            Property to be extracted from word.

        Returns
        -------
        word_properties : pandas.Series
            The property of all words.
        """

        word_objs = self._results["word_objs"]
        function_for_extracting_property = lambda w: getattr(w, word_property)
        word_properties = word_objs.apply(function_for_extracting_property)

        return word_properties

    def _add_words_text_to_results(self):
        """Add the word's text to the results object.

        Returns
        -------
        None
        """

        word_text = self._get_property_from_words(word_property="text")
        self._results["text"] = word_text

    def check_length_difficulty(self):
        """Determine the difficulty of each word associated with its length.

        The length is determined based on the number of letters in the words.

        Returns
        -------
        None
        """

        word_lengths = self._get_property_from_words(word_property="length")
        self._results["length"] = word_lengths

    @docstrings.with_indent(8)
    def check_silent_letter_difficulty(self):
        """Determine the difficulty of each word associated with silent letters.

        %(silent_letters.summary_ext)s

        Rules
        -----
        %(silent_letters.rules)s

        Returns
        -------
        None
        """

        word_silent_letters = self._get_property_from_words(word_property="silent_letters")
        self._results["silent_letters"] = word_silent_letters

    @docstrings.with_indent(8)
    def check_shared_phonemes_difficulty(self):
        """Determine the difficulty of each word associated with shared phonemes.

        %(shared_phonemes.summary_ext)s

        Rules
        -----
        %(shared_phonemes.rules)s

        Returns
        -------
        None
        """

        word_shared_phonemes = self._get_property_from_words(word_property="shared_phonemes")
        self._results["shared_phonemes"] = word_shared_phonemes

    @docstrings.with_indent(8)
    def determine_total_difficulty(self):
        """Determine each word's total difficulty.

        %(total_difficulty.summary_ext)s

        Raises
        ------
        %(total_difficulty.raises)s

        Returns
        -------
        None
        """

        word_total_difficulty = self._get_property_from_words(
            word_property="total_difficulty"
        )
        self._results["total_difficulty"] = word_total_difficulty
        # valid_cols = self._results.iloc[:, 2:]
        # print(valid_cols)
        # # total_difficulty = valid_cols.sum()
        # self._results["total_difficulty"] = valid_cols.sum()

    def _format_results(self):
        """Format the results before making them public.

        Returns
        -------
        results_formatted : pandas.DataFrame
            Formatted results
        """

        results = self._results.copy()
        results_formatted = results.drop(columns="word_objs")

        return results_formatted

    def save_results(self, filename="results"):
        """Save the results to a CSV file.

        Parameters
        ----------
        filename : str, default="results"
            Filename. If a complete path is provided, it will be saved
            in the specific path. It must not include the file's extension.

        Returns
        -------
        None
        """

        results_formatted = self._format_results()
        filename = f"{filename}.csv"
        results_formatted.to_csv(filename, index=False)

    def run_all_analyses(self):
        """Run all analyses.

        This is a convenient function to run all analyses and simplify
        the process for the user.

        Returns
        -------
        None
        """

        self.check_length_difficulty()
        self.check_silent_letter_difficulty()
        self.check_shared_phonemes_difficulty()
        self.determine_total_difficulty()

    @property
    def results(self):
        """Return the results.

        Returns
        -------
        results : pandas.DataFrame
            Formatted results
        """

        return self._format_results()
