#! "C:\Python33\python.exe"
# -*- coding: utf-8 -*-

import iofiles
import analysis

iodata = iofiles.IOData()
words = iodata.read_sequence("a.txt", duplicates="n")

wordanalysis = analysis.WordAnalysis(words)
wordanalysis.check_special_characters()

wordanalysis.length()
wordInfo = wordanalysis.get_word_info()

print("\n"*10)

wordanalysis.check_silent_letters()
muteInfo = wordanalysis.get_silent_letter_info()

with open("testMuteLetters.txt") as file:
    file.write('kj')
    
#    iodata.write_sequence((k, v), "testMuteLetters.txt")

end = input("press enter")

