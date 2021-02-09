import pandas as pd

from word import Word


class Analyzer(object):
    """This class provides the API.
    It provides methods for creating word objects, running analyses, storing
    results, and saving them to disk.
    """

    def __init__(self, words):
        """It requires an iterable of words to be analyzed.

        Parameters
        ----------
        words : iterable, list-like object
            Contains the words to be analyzed.
        """

        self._results = pd.DataFrame()
        word_objs = self._create_word_objs(words)
        self._results["word_objs"] = word_objs


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

