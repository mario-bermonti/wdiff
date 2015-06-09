#! "C:\Python33\python.exe"
# -*- coding: utf-8 -*-

import iofiles
import analysis


def main():
    iodata = iofiles.IOData()
    words = iodata.read_sequence("words.txt", duplicates="y")

    wordanalysis = analysis.WordAnalysis(words)
    # wordanalysis.check_special_characters()

    # wordanalysis.length()
    # wordInfo = wordanalysis.get_word_info()

    wordanalysis.check_silent_letters()
    silentInfo = wordanalysis.get_silent_letter_info()
    print(silentInfo)

    with open("testSilentLetters.txt", "wt") as file:
        file.write(str(silentInfo))

        #iodata.write_sequence(silentInfo, "testSilentLetters.txt")

        end = input("press enter")

main()
