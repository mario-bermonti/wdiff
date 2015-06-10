#! "C:\Python33\python.exe"
# -*- coding: utf-8 -*-

import iofiles
import analysis


def get_file_name():
    """Aks the user for the name of the file with the words to be analyzed."""

    fileName = input("Escribe el nombre del documento con las palabras: ")

    return fileName


def main():
    iodata = iofiles.IOData()
    fileName = get_file_name()
    fileName = "{}.txt".format(fileName)
    words = iodata.read_sequence(fileName, duplicates="y")

    wordanalysis = analysis.WordAnalysis(words)
    # wordanalysis.check_special_characters()

    # wordanalysis.length()
    # wordInfo = wordanalysis.get_word_info()

    wordanalysis.check_silent_letters()
    silentInfo = wordanalysis.get_silent_letter_info()
    print(silentInfo)

#    with open("testSilentLetters.txt", "wt") as file:
#        file.write(str(silentInfo))

    end = input("press enter")

main()
