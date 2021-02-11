"""Module that defines the api."""

import pandas as pd

from .word import Word


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
            List of word objects
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
            Series containing the property of each words.
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
        """Determine the difficulty associated with the length of the words.

        # TODO add the docstring of word's analog attribute.

        Returns
        -------
        None
        """

        word_lengths = self._get_property_from_words(word_property="length")
        self._results["length"] = word_lengths

    def check_silent_letter_difficulty(self):
        """Determine each word's difficulty associated with silent letters.

        # TODO add the docstring of word's analog attribute.

        Returns
        -------
        None
        """

        word_silent_letters = self._get_property_from_words(word_property="silent_letters")
        self._results["silent_letters"] = word_silent_letters

    def check_shared_phonemes_difficulty(self):
        """Determine each word's difficulty associated with shared phonemes.

        # TODO add the docstring of word's analog attribute.

        Returns
        -------
        None
        """

        word_shared_phonemes = self._get_property_from_words(word_property="shared_phonemes")
        self._results["shared_phonemes"] = word_shared_phonemes

    def determine_total_difficulty(self):
        """Determine each word's total difficulty.

        # TODO add the docstring of word's analog attribute.

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

    @property
    def results(self):
        """Return the results

        Returns
        -------
        results : pandas.DataFrame
        """

        return self._format_results()

    def save_results(self, filename="results"):
        """Save the results to a CSV file.

        Parameters
        ----------
        filename : str
            Filename. If a complete path is provided, it will be saved
            in the specific path. It must not include the file's extension.

        Returns
        -------
        None
        """

        results_formatted = self._format_results()
        filename = f"{filename}.csv"
        results_formatted.to_csv(filename, index=False)


