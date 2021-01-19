# -*- coding: utf-8 -*-

"""
Provides a class to analyze a list of words on specific criteria in order
to determine their difficulty and provides a class to save the data to an
Excel file.
"""

import collections
import pandas as pd


class WordAnalyzer(object):
    """Interface to analyze words on the following dimensions:
    1) length: number of letters,
    2) silent letters: letters that have no sound (e.g. /h/),
    3) same sound letters: different letters with the same sound (e.g. s and
       z),
    4) anagrams: words that may form other words if its letters are reorganized
    """

    def __init__(self):
        self.completedAnalysis = []

    def set_words(self, words):
        """Sets up the words that are going to be analyzed, passing a
        list-like object of words.


        Notes
        _____
        1) This methods was added so the WordAnalyzer doesn't have to be
        instantiated for running every test.
        """

        self.words = words

    def determine_length_difficulty(self, difficultyWeight=3):
        """Determines the difficulty in each word associated with its length
        and stores the results.

        Parameter
        _________
        difficultyWeight: int
            Indicates the relative contribution of this variable to
            the total word difficulty
        """

        self.completedAnalysis.append('length_difficulty')
        self.lengthInfo = dict()
        for word in self.words:
            self.lengthInfo[word] = len(word) * difficultyWeight

    def determine_silent_letter_difficulty(self, difficultyWeight=2):
        """Determines the difficulty in each word associated with the presence
        of silent letters and stores the results.

        Parameter
        _________
        difficultyWeight: int
            Indicates the relative contribution of this variable to
            the total word difficulty
        """

        self.completedAnalysis.append('silent_letter_difficulty')
        self.silentLetterInfo = dict()
        for word in self.words:
            silentLetterOcurrences = self.determine_total_silent_letters(word)
            difficultyIndex = difficultyWeight * silentLetterOcurrences
            self.silentLetterInfo[word] = difficultyIndex

    def determine_total_silent_letters(self, word):
        """Determines the total number of silent letters in the word and
        returns it as an int.
        """

        return self.count_silent_h(word) + self.count_silent_u(word)

    def count_silent_h(self, word):
        """Determines the occurences of silent h's in the word based on the
        Spanish language rules and returns it as an int.
        """

        silentHCount = 0

        if "h" in word:
            hCount = word.count("h")
            start = 0

            while hCount > 0:
                hPosition = word.find("h", start)
                if not word[hPosition-1] == "c":
                    silentHCount += 1
                hCount -= 1
                start = hPosition + 1

        return silentHCount

    def count_silent_u(self, word):
        """Determines the occurences of silent u's in the word based on the
        Spanish language rules and returns it as an int.
        """

        silentUCount = 0

        if "u" in word:
            uCount = word.count("u")
            start = 0

            while uCount > 0:
                uPosition = word.find("u", start)
                if ((word[uPosition-1] == "q" or word[uPosition-1] == 'g') and
                        (word[uPosition+1] == "e" or word[uPosition+1] == "i")):
                    silentUCount += 1
                uCount -= 1
                start = uPosition + 1

        return silentUCount

    def determine_same_sound_letter_difficulty(self, difficultyWeight=2):
        """Determines the difficulty in each word associated with the presence
        of same sound letters and stores the results.

        Parameter
        _________
        difficultyWeight: int
            Indicates the relative contribution of this variable to
            the total word difficulty
        """


        self.completedAnalysis.append('same_sound_difficulty')
        self.sameSoundLetterInfo = dict()
        for word in self.words:
            sameSoundLetterOcurrences = self.determine_total_same_sound_letters(word)
            difficultyIndex = difficultyWeight * sameSoundLetterOcurrences
            self.sameSoundLetterInfo[word] = difficultyIndex

    def determine_total_same_sound_letters(self, word):
        """Determines the total number of same sound letters in the word and
        returns it as an int.
        """

        return(
            self.count_swappable_b_sounds(word) + self.count_swappable_j_sounds(word) +
            self.count_swappable_s_sounds(word) + self.count_swappable_k_sounds(word) +
            self.count_swappable_ll_sounds(word)
        )

    def count_swappable_b_sounds(self, word):
        """Determines the number of letters that could be swapped because
        they represent they same /b/ phoneme and returns it as an int.
        """

        bSwappableCount = 0
        if "b" in word and "v" in word:
            bSwappableCount = word.count("b") * word.count("v")

        return bSwappableCount

    def count_swappable_j_sounds(self, word):
        """Determines the number of letters that could be swapped because
        they represent they same /j/ phoneme and returns it as an int.
        """

        jSwappableCount = 0
        if "j" in word and "g" in word:
            ruleCompliantGs = self.count_g_with_j_sound(word)
            jSwappableCount = word.count("j") * ruleCompliantGs

        return jSwappableCount

    def count_g_with_j_sound(self, word):
        """Determines the number of letter g's that have a /j/ sound and returns
        it as an int.
        """

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
            if position == (len(word) - 1):
                continue
            if word[position+1] == 'i' or word[position+1] == "e":
                gCompliantCount += 1

        return gCompliantCount

    def count_swappable_s_sounds(self, word):
        """Determines the number of letters that could be swapped because
        they represent they same /s/ phoneme and returns it as an int.
        """

        sSwappableCount = 0
        if (("s" in word and "c" in word) or ("s" in word and "z" in word) or
                ("c" in word and "z" in word)):
            if "c" in word:
                ruleCompliantCs = self.count_c_with_s_sound(word)
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

    def count_c_with_s_sound(self, word):
        """Determines the number of c's that have an /s/ sound and returns
        it as an int.
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
            if position == (len(word) - 1):
                continue
            if word[position+1] == 'i' or word[position+1] == "e":
                cCompliantCount += 1

        return cCompliantCount

    def count_swappable_k_sounds(self, word):
        """Determines the number of letters that could be swapped because
        they represent they same /k/ phoneme and returns it as an int.
        """

        kSwappableCount = 0
        if (("k" in word and "q" in word) or ("k" in word and "c" in word) or
                ("q" in word and "c" in word)):
            if "q" in word:
                ruleCompliantQs = self.count_q_with_k_sound(word)
            if "c" in word:
                ruleCompliantCs = self.count_c_with_k_sound(word)
            if "k" in word and "q" in word and "c" in word:
                kSwappableCount = (
                    (word.count("k") * ruleCompliantQs) +
                    (word.count("k") * ruleCompliantCs) +
                    (ruleCompliantQs * ruleCompliantCs)
                )
            elif "k" in word and "q" in word:
                kSwappableCount = word.count("k") * ruleCompliantQs
            elif "k" in word and "c" in word:
                kSwappableCount = word.count("k") * ruleCompliantCs
            elif "q" in word and "c" in word:
                kSwappableCount = ruleCompliantQs * ruleCompliantCs

        return kSwappableCount

    def count_q_with_k_sound(self, word):
        """Determines the number of q's that have an /k/ sound and returns
        it as an int.
        """

        qCompliantCount = 0
        qCount = word.count("q")
        qPositions = list()
        start = 0

        while qCount > 0:
            qPosition = word.find("q", start)
            qPositions.append(qPosition)
            start = qPosition + 1
            qCount -= 1

        for position in qPositions:
            if position == (len(word) - 1):
                continue
            if (word[position+1] == "u" and
                    (word[position+2] == "e" or word[position+2] == "i")):
                qCompliantCount += 1

        return qCompliantCount

    def count_c_with_k_sound(self, word):
        """Determines the number of c's that have an /k/ sound and returns
        it as an int.
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
            if position == (len(word) - 1):
                continue
            if (word[position+1] == "a" or word[position+1] == "o" or
                    word[position+1] == "u"):
                cCompliantCount += 1

        return cCompliantCount

    def count_swappable_ll_sounds(self, word):
        """Determines the number of letters that could be swapped because
        they represent they same /ll/ phoneme and returns it as an int.
        """

        llSwappableCount = 0
        if "y" in word and "l" in word:
            ruleCompliantYs = self.count_y_with_ll_sound(word)
            ruleCompliantLs = self.count_l_with_ll_sound(word)
            llSwappableCount = ruleCompliantYs * ruleCompliantLs

        return llSwappableCount

    def count_y_with_ll_sound(self, word):
        """Determines the number of y's that have an /ll/ sound and returns
        it as an int.
        """

        yCompliantCount = 0
        yCount = word.count("y")
        yPositions = list()
        start = 0

        while yCount > 0:
            yPosition = word.find("y", start)
            yPositions.append(yPosition)
            start = yPosition + 1
            yCount -= 1

        # Improve
        # Could be improve if 1 was taken from the
        # count if length - 1 is in the list of
        # position
        for position in yPositions:
            if position != (len(word) - 1):
                yCompliantCount += 1

        return yCompliantCount

    def count_l_with_ll_sound(self, word):
        """Determines the number of l's that have an /ll/ sound and returns
        it as an int.
        """

        lCompliantCount = 0
        lCount = word.count("l")
        lPositions = list()
        start = 0

        while lCount > 0:
            lPosition = word.find("l", start)
            lPositions.append(lPosition)
            start = lPosition + 1
            lCount -= 1

        for position in lPositions:
            if position == (len(word) - 1):
                continue
            if word[position+1] == "l":
                lCompliantCount += 1

        return lCompliantCount

    def determine_anagrams_difficulty(self, difficultyWeight=1):
        """Determines the difficulty in each word associated with the word
        being and anagram of another word.

        Parameter
        _________
        difficultyWeight: int
            Indicates the relative contribution of this variable to
            the total word difficulty
        """

        self.completedAnalysis.append('anagrams_difficulty')
        self.anagramsInfo = dict()
        for word in self.words:
            anagramCount = self.count_anagrams(word)
            # if the letters of the word can only form 1 word (itself) then its
            # difficulty should be 0.
            if anagramCount == 1:
                difficultyIndex = 0
            else:
                difficultyIndex = anagramCount * difficultyWeight
            self.anagramsInfo[word] = difficultyIndex

    def count_anagrams(self, word):
        """Determines the number of words that are anagrams of this word and
        returns it as an int.

        Parameter
        _________
        word: str
            word to analyze

        Returns
        _______
        anagramCount: int
            Indicates the number of anagrams that can be
            created (including the word itself)

        Notes
        _____
        1) This method assumes the word passed in and self.words contain valid
        words. It will consider nonvalid words as anagrams of each other if
        they contain the same letter count, regardless of the validity.
        2) Because this algorithm only considers each word in the list against
        other words in the list the accuracy of the estimation improves as the
        number of words in the list is larger.
        """

        anagramCount = 0
        for w in list(self.words):
            if collections.Counter(word) == collections.Counter(w):
                anagramCount += 1

        return anagramCount

    def determine_total_difficulty_index(self):
        """Determines the total difficulty index for each word."""

        self.completedAnalysis.append('total difficulty')
        self.wordInfo = self.integrate_word_information()
        for word, difficultyIndexes in self.wordInfo.items():
            self.wordInfo[word].append(
                sum(difficultyIndexes)
            )

    def integrate_word_information(self):
        """Integrates the difficulty index from each analysis into
        a single dictionary and returns it.
        """

        wordInfo = dict()
        for word in self.words:
            wordInfo[word] = []
            if 'length_difficulty' in self.completedAnalysis:
                wordInfo[word].append(self.lengthInfo[word])
            if 'silent_letter_difficulty' in self.completedAnalysis:
                wordInfo[word].append(self.silentLetterInfo[word])
            if 'same_sound_difficulty' in self.completedAnalysis:
                wordInfo[word].append(self.sameSoundLetterInfo[word])
            if 'anagrams_difficulty' in self.completedAnalysis:
                wordInfo[word].append(self.anagramsInfo[word])

        return wordInfo

    def get_length_info(self):
        """Returns a dict object where the keys are the words and the values
        are the difficulty associated with its length.
        """

        return self.lengthInfo

    def get_silent_letter_info(self):
        """Returns a dict object where the keys are the words and the values
        are the difficulty associated with the presence of silent letters.
        """

        return self.silentLetterInfo

    def get_same_sound_letter_info(self):
        """Returns a dict object where the keys are the words and the values
        are the difficulty associated with the presence of same sound letters.
        """

        return self.sameSoundLetterInfo

    def get_anagrams_info(self):
        """Returns a dict object where the keys are the words and the values
        are the difficulty associated with the number of anagrams that can be
        made from this word's letters.
        """

        return self.anagramsInfo

    def get_word_difficulty(self):
        """Returns a dict object where the keys are the words and the values
        are the total difficulty indexes.
        """

        return self.wordInfo

    def save_results(self, filename='results.csv'):
        """Save the results for each dimension analyzed and the total word
        difficulty to a file.

        Parameter:
        _________
        filename: str; name of the file to save the results to
        """

        results = self.format_data()
        results.to_csv(filename)

    def format_data(self):
        """Integrates all data into a pd dataframe to facilitate saving
        it to disk. It uses the data stored in self.wordInfo.

        Returns
        _______
        formatted_data: pandas dataframe
             Pandas dataframe that has the analyzed dimensions as
        columns and the words as the index.
        """

        formattedData = pd.DataFrame.from_dict(self.wordInfo, orient='index')
        formattedData.columns = self.completedAnalysis

        return formattedData
