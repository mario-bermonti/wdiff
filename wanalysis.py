#! "C:\Python33\python.exe"
# -*- coding: utf-8 -*-


class WordAnalyzer(object):
    """Analyzes words on the dimensions of: number of letters, if letters have
    special characters, silent letters, different letters with the same sound,
    and letters visually similar. It will assign different difficulty points
    to the letters depending on the dimension. The total difficulty level will
    help organize words in ascending (or descending) ordering of difficulty.
    """

    def __init__(self, words):
        self.words = words
        self.analysisDimensions = (
            "length",
            "silent letters",
            "same sound letters",
            "anagrams"
            "difficulty index"
        )

    def check_length(self):
        """Calculates the length of each word in words and includes in the
        dictionary wordInfo.
        """

        self.lengthInfo = dict()
        difficultyweight = 3
        for word in self.words:
            self.lengthInfo[word] = len(word) * difficultyweight

    def check_silent_letters(self):
        """Uses has_silent_letters to determine if the words in self.words
        have silent letters. Assigns a difficulty index to each word based
        on the presence of silent letters.
        """

        difficultyweight = 2
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
            start = 0

            while hCount > 0:
                hPosition = word.find("h", start)
                if not word[hPosition-1] == "c":
                    silenthCount += 1
                hCount -= 1
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

        return(
            self.check_b_sound(word) + self.check_j_sound(word) +
            self.check_s_sound(word) + self.check_k_sound(word) +
            self.check_y_sound(word)
        )

    def check_b_sound(self, word):
        """Determines the number of occurrences in the word word of different
        letters with the sound /b/ that can be swapped by mistake.
        """

        bSwappableCount = 0
        if "b" in word and "v" in word:
            bSwappableCount = word.count("b") * word.count("v")

        return bSwappableCount

    def check_j_sound(self, word):
        """Determines the number of occurrences in the word word of different
        letters with the sound /j/ that can be swapped by mistake. Uses
        the gswappable_check method to determine if there are any g's that
        sound like j's.
        """

        jSwappableCount = 0
        if "j" in word and "g" in word:
            ruleCompliantGs = self.swap_g_for_j_check(word)
            jSwappableCount = word.count("j") * ruleCompliantGs

        return jSwappableCount

    def swap_g_for_j_check(self, word):
        """Checks how many g's in the word word sound like j's so they can be
        swapped with j's by mistake.
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
                ruleCompliantCs = self.swap_c_for_s_check(word)
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

    def swap_c_for_s_check(self, word):
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
            if position == (len(word) - 1):
                continue
            if word[position+1] == 'i' or word[position+1] == "e":
                cCompliantCount += 1

        return cCompliantCount

    def check_k_sound(self, word):
        """Determines the number of occurrences in the word word of different
        letters with the sound /k/ that can be swapped by mistake. Uses
        the cSwappable_check qSwappable_check methods to determine if there are
        any c's or q's that sound like k's.
        """

        kSwappableCount = 0
        if (("k" in word and "q" in word) or ("k" in word and "c" in word) or
                ("q" in word and "c" in word)):
            if "q" in word:
                ruleCompliantQs = self.swap_q_for_k_check(word)
            if "c" in word:
                ruleCompliantCs = self.swap_c_for_k_check(word)
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

    def swap_q_for_k_check(self, word):
        """Checks how many q's in the word word sound like k's so they can be
        swapped with k's by mistake.
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

    def swap_c_for_k_check(self, word):
        """Checks how many c's in the word word sound like k's so they can be
        swapped with k's by mistake.
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

    def check_y_sound(self, word):
        """Determines the number of occurrences in the word word of different
        letters with the sound /y/ that can be swapped by mistake. Uses
        the swap_y_for_y_check and swap_l_for_y_check methods to determine
        if there are any y's or ll's that sound like y's.
        """

        ySwappableCount = 0
        if "y" in word and "l" in word:
            ruleCompliantYs = self.swap_y_for_y_check(word)
            ruleCompliantLs = self.swap_l_for_y_check(word)
            ySwappableCount = ruleCompliantYs * ruleCompliantLs

        return ySwappableCount

    def swap_y_for_y_check(self, word):
        """Checks how many c's in the word word sound like k's so they can be
        swapped with k's by mistake.
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

        for position in yPositions:
            if position != (len(word) - 1):
                yCompliantCount += 1

        return yCompliantCount

    def swap_l_for_y_check(self, word):
        """Checks how many c's in the word word sound like k's so they can be
        swapped with k's by mistake.
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

    def check_anagrams(self):
        """It uses in_anagrams_list to determine if any of the words is an
        anagram and determines a difficulty index for each word for the anagram
        dimension. Stores the word info in the dict anagramsInfo.

        Checks to see if an instance of IOData already exists and if it doesn't
        it creates one in order to read the anagram database.
        """

        difficultyweight = 1
        self.anagramsInfo = dict()
        for word in self.words:
            anagramCount = self.in_anagrams_list(word, anagramList)
            difficultyIndex = anagramCount * difficultyweight
            self.anagramsInfo[word] = difficultyIndex

    def in_anagrams_list(self, word, anagramList):
        """Checks if the word word is in any of the lines in anagramList.
        If it is in any line, it counts the number of words on that line
        to determine how many words can the letters of the word be scrambled
        to make.
        """

        anagramCount = 0
        for line in anagramList:
            if word in line:
                anagramCount = len(line)
        return anagramCount

    def determine_total_difficulty_index(self):
        """Determines the total difficulty index for each word and appends it
        to the properties of each word.
        """

        for k, v in self.wordInfo.items():
            total = sum(v)
            self.wordInfo[k] = v + (total, )

    def integrate_word_information(self):
        """Integrates information  the work information for each dictionary
        into a single dictionary.
        """

        self.wordInfo = dict()
        for word in self.words:
            self.wordInfo[word] = (
                self.lengthInfo[word],
                self.silentLetterInfo[word],
                self.sameSoundLetterInfo[word],
                self.anagramsInfo[word]
            )

        self.determine_total_difficulty_index()

    def get_length_info(self):
        """Returns a dict with the info of the length of every word."""

        return self.lengthInfo

    def get_silent_letter_info(self):
        """Returns a dict with the silent letter info for every word."""

        return self.silentLetterInfo

    def get_same_sound_letter_info(self):
        """Returns a dict with the same sound letters info for
        every word.
        """

        return self.sameSoundLetterInfo

    def get_anagrams_info(self):
        """Returns a dict with the anagrams info for every word."""

        return self.anagramsInfo

    def get_word_info(self):
        """Returns a dictionary with the info for every word."""

        return self.wordInfo

    def get_analysis_dimensions(self):
        """Returns a tuple with the dimensions analyzed for informative
        purposes or for database construction.
        """

        return self.analysisDimensions


if __name__ == "__main__":
    wordanalyzer = WordAnalyzer()
