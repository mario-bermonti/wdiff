#! "C:\Python33\python.exe"
# -*- coding: utf-8 -*-

import iofiles


class WordAnalysis(object):
    """Analyzes words on the dimensions of: number of letters, if letters have
    special characters, silent letters, different letters with the same sound,
    and letters visually similar. It will assign different difficulty points
    to the letters depending on the dimension. The total difficulty level will
    help organize words in ascending (or descending) ordering of difficulty.
    """

    def __init__(self, words):
        self.words = words
        self.wordInfo = dict()
        self.dimensions = ("length", "accents", "silent letters",
                           "same sound letters")

    def check_special_characters(self):
        """Uses has_special_characters to determine if any word has special
        characters. If the word has any of the special characters they are
        included in the  wordsWithSpecialCharacters list, which will be
        written to the file file, so the user can check them.
        """

        self.wordsWithSpecialCharacters = list()
        for word in self.words:
            if self.has_special_characters(word):
                self.wordsWithSpecialCharacters.append(word)
        print(self.wordsWithSpecialCharacters)

        if self.wordsWithSpecialCharacters:
            self.iodata = iofiles.IOData()
            writeWord = self.iodata.write_sequence(
                self.wordsWithSpecialCharacters,
                "invalid words.txt"
            )

            self.eliminate_invalid_words(self.wordsWithSpecialCharacters)

    def has_special_characters(self, word):
        """Returns True if any of the letters of the word is not a valid
        character.
        """

        self.acceptedSymbols = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
        for letter in word:
            upperCaseLetter = letter.upper()
            if upperCaseLetter not in self.acceptedSymbols:
                return True

    def eliminate_invalid_words(self, words):
        """Eliminates invalid words from self.words."""

        for word in words:
            self.words.remove(word)

    def length(self):
        """Calculates the length of each word in words and includes in the
        dictionary wordInfo.
        """

        self.lengthInfo = dict()
        difficultyweight = 1
        for word in self.words:
            # the difficultyLevel is the same as the length of the word,
            # so no additional calculation is needed.
            self.lengthInfo[word] = len(word)

        # just fo debugging purposes
        print("""length info:
        {}""".format(self.lengthInfo))

    def check_silent_letters(self):
        """Uses has_silent_letters to determine if the words has silent letters
        that. If it does, it assigns a point of difficulty to the word.
        """

        difficultyweight = 1
        self.silentLetterInfo = dict()

        for word in self.words:
            silentLetterOcurrences = self.has_silent_letters(word)
            difficultyLevel = difficultyweight * silentLetterOcurrences
            self.silentLetterInfo[word] = difficultyLevel

        # just fo debugging purposes
        print("""mute info:
        {}""".format(self.silentLetterInfo))

    def has_silent_letters(self, word):
        """Adds difficulty points to the word passed in if it contains mute
        letters. It supports spanish mute letters ("h" and "u".

        Returns the total difficulty points for the word.
        """

        silentLetterCount = 0

        if "h" in word:
            hCount = word.count("h")
            start = 0
            while hCount > 0:
                hPosition = word.find("h", start)
                if not word[hPosition-1] == "c":
                    silentLetterCount += 1
                hCount -= 1
                start = hPosition

        if "u" in word:
            uCount = word.count("u")
            start = 0
            while uCount > 0:
                uPosition = word.find("u", start)
                if ((word[uPosition-1] == "q" or word[uPosition-1] == 'g') and
                        (word[uPosition+1] == "e" or word[uPosition+1] == "i")):
                    silentLetterCount += 1
            hCount -= 1
            start = hPosition

        print(silentLetterCount)

        return silentLetterCount

    def get_silent_letter_info(self):
        """Returns a dict with the mute letter info for every word."""

        return self.silentLetterInfo

    def get_word_info(self):
        """Returns a dict with the info of the dimensions analyzed for
        every word.
        """

        return self.wordInfo
