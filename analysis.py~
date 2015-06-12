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
        self.dimensions = ("length", "accents", "silent letters",
                           "same sound letters")

    def check_special_characters(self):
        """Uses has_special_characters to determine if any word has special
        characters. If the word has any of the special characters they are
        included in the wordsWithSpecialCharacters list, which will be
        written to the file file, so the user can check them.
        """

        self.wordsWithSpecialCharacters = list()
        for word in self.words:
            if self.has_special_characters(word):
                self.wordsWithSpecialCharacters.append(word)

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
        """Uses has_silent_letters to determine if the words in self.words
        have silent letters. Assigns a difficulty index to each word based
        on the presence of silent letters.
        """

        difficultyweight = 1
        self.silentLetterInfo = dict()

        for word in self.words:
            silentLetterOcurrences = self.has_silent_letters(word)
            difficultyIndex = difficultyweight * silentLetterOcurrences
            self.silentLetterInfo[word] = difficultyIndex

    def has_silent_letters(self, word):
        """Returns the total difficulty points for the word passed in."""

        return self.has_silent_h(word) + self.has_silent_u(word)

    def has_silent_h(self, word):
        """Determines the occurences of silent h's in the word based on the
        spanish language rules.

        returns: the number of silent h's in the word.
        """

        silenthCount = 0

        if "h" in word:
            hCount = word.count("h")
            print('count', hCount)
            start = 0
            while hCount > 0:
                print('start', start)
                hPosition = word.find("h", start)
                print('hpos', hPosition)
                if not word[hPosition-1] == "c":
                    silenthCount += 1
                print('silent count', silenthCount)
                print('before h', word[hPosition-1])
                hCount -= 1
                print('count', hCount)
                start = hPosition + 1

        return silenthCount

    def has_silent_u(self, word):
        """Determines the occurences of silent u's in the word based on the
        spanish language rules.

        returns: the number of silent u's in the word.
        """

        silentuCount = 0

        if "u" in word:
            uCount = word.count("u")
            start = 0
            while uCount > 0:
                uPosition = word.find("u", start)
                if ((word[uPosition-1] == "q" or word[uPosition-1] == 'g') and
                        (word[uPosition+1] == "e" or word[uPosition+1] == "i")):
                    silentuCount += 1
                uCount -= 1
                start = uPosition + 1

        return silentuCount

    def check_same_sound_letter(self):
        """Uses has_same_sound_letters to determine if the words in self.words
        have different letters that can be swapped by mistake, because they
        have the same sound. Assigns a difficulty index to each word based
        on the occurrences of "same sound letters".
        """

        difficultyweight = 2
        self.sameSoundLetterInfo = dict()

        for word in self.words:
            sameSoundLetterOcurrences = self.has_same_sound_letters(word)
            difficultyIndex = difficultyweight * sameSoundLetterOcurrences
            self.sameSoundLetterInfo[word] = difficultyIndex

    def has_same_sound_letters(self, word):
        """Returns the total difficulty points for the word passed in
        based on "same sound letter" occurrences.
        """

        return (self.check_b_sound(word) + self.check_j_sound(word) +
                self.check_s_sound(word) + self.check_k_sound(word) +
                self.check_l_sound(word)
                )

    def check_b_sound(self, word):
        """Determines the number of occurrences in the word word of different
        letters with the sound /b/ that can be swapped by mistake.
        """

        if "b" in word and "v" in word:
            bSwappableCount = word.count("b") * word.count("v")

        return bSwappableCount

    def check_j_sound(self, word):
        """Determines the number of occurrences in the word word of different
        letters with the sound /j/ that can be swapped by mistake. Uses
        the gswappable_check method to determine if there are any g's that
        sound like j's.
        """

        if "j" in word and "g" in word:
            ruleCompliantGs = self.gSwappable_check(word)
            jSwappableCount = word.count("j") * ruleCompliantGs

        return jSwappableCount

    def gSwappable_check(self, word):

        gCompliantCount = 0
        gCount = word.count("g")
        gPositions = list()
        start = 0

        while gCount > 0:
            gPosition = word.find("g", start)
            gPositions.append(gPosition)
            start = gPosition + 1
            gCount -= 1

        for position in gPositions:
            if word[position+1] == 'i' or word[position+1] == "e":
                gCompliantCount += 1

        return gCompliantCount

    def check_s_sound(self, word):
        """Determines the number of occurrences in the word word of different
        letters with the sound /s/ that can be swapped by mistake. Uses
        the cSwappable_check method to determine if there are any c's
        that sound like s's.
        """

        sSwappableCount = 0

        if (("s" in word and "c" in word) or ("s" in word and "z" in word) or
                ("c" in word and "z" in word)):
            if "c" in word:
                ruleCompliantCs = self.cSwappable_check(word)
            if "s" in word and "c" in word and "z" in word:
                sSwappableCount = (
                    (word.count("s") * ruleCompliantCs) +
                    (word.count("s") * word.count("z")) +
                    (ruleCompliantCs * word.count("z"))
                )
            elif "s" in word and "c" in word:
                sSwappableCount = word.count("s") * ruleCompliantCs
            elif "s" in word and "z" in word:
                sSwappableCount = word.count("s") * word.count("z")
            elif "c" in word and "z" in word:
                sSwappableCount = ruleCompliantCs * word.count("z")

        return sSwappableCount

    def cSwappable_check(self, word):
        """Checks how many c's in the word word sound like s's so they can be
        swapped with s's by mistake.
        """

        cCompliantCount = 0
        cCount = word.count("c")
        cPositions = list()
        start = 0

        while cCount > 0:
            cPosition = word.find("c", start)
            cPositions.append(cPosition)
            start = cPosition + 1
            cCount -= 1

        for position in cPositions:
            if word[position+1] == 'i' or word[position+1] == "e":
                cCompliantCount += 1

        return cCompliantCount

    def check_k_sound(self, word):
        """Determines the number of occurrences in the word word of different
        letters with the sound /k/ that can be swapped by mistake.
        """

        kSoundCount = 0

        return kSoundCount

    def check_l_sound(self, word):
        """Determines the number of occurrences in the word word of different
        letters with the sound /b/ that can be swapped by mistake.
        """

        lSoundCount = 0

        return lSoundCount

    def get_silent_letter_info(self):
        """Returns a dict with the silent letter info for every word."""

        return self.silentLetterInfo

    def get_length_info(self):
        """Returns a dict with the info of the length of every word."""

        return self.lengthInfo

    def get_same_sound_letter_info(self):
        """"Returns a dict with the same sound letters info for
        every word.
        """

        return self.sameSoundLetterInfo

if __name__ == "__main__":
    analysis = WordAnalysis()
