#! "C:\Python33\python.exe"
# -*- coding: utf-8 -*-

import iofiles
import analysis


def get_file_name():
    """Aks the user for the name of the file with the words to be analyzed."""

    fileName = input("Escribe el nombre del documento con las palabras: ")

    return fileName


def get_words(fileName):
    iodata = iofiles.IOData()
    words = iodata.read_sequence(fileName, duplicates="y")

    return words


def main():
    fileName = get_file_name()
    fileName = "{}.txt".format(fileName)
    words = get_words(fileName)

    wordanalysis = analysis.WordAnalysis(words)

#    wordanalysis.check_special_characters()

#    wordanalysis.length()
#    wordLengthInfo = wordanalysis.get_length_info()
#    print(wordLengthInfo)
##    wordanalysis.check_silent_letters()
#    silentInfo = wordanalysis.get_silent_letter_info()
#    print("\n")
#    print(silentInfo)

#    wordanalysis.check_same_sound_letter()
#    sameSoundInfo = wordanalysis.get_same_sound_letter_info()
#    print(sameSoundInfo)
    wordanalysis.check_anagrams()

    end = input("press enter")


main()
