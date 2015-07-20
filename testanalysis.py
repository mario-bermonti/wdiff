#! "C:\Python33\Python.exe"
# -*- coding: utf-8 -*-

import iofiles
import analysis


class WordAnalysis():
    def __init__(self):
        self.fileName = self.get_file_name()
        self.fileName = "{}.txt".format(self.fileName)
        self.words = self.get_words(self.fileName)
        self.wordanalysis = analysis.WordAnalysis(self.words)

        self.interface()

    def interface(self):
        while True:
            self.print_menu()
            desiredAnalysis = self.get_desired_analysis()
            if desiredAnalysis == "6":
                break
            elif desiredAnalysis in ("1", "2", "3", "4", "5"):
                self.run_analysis(desiredAnalysis)
            else:
                print("Opción inválida. Intente nuevamente")

    def print_menu(self):
        """Print the anaylsis options to the user."""

        print("Bienvenido Análisis de Palabras\n")
        print("Presione el número que identifica el análisis deseado")
        print("Las opciones de análisis son las siguientes:")
        print("1. Identificar palabras inválidas")
        print("2. Analizar la longitud de la palabra")
        print("3. Analizar letras silenciosas")
        # Find a better description
        print("4. Analizar letras con sonidos iguales")
        print("5. Analizar anagramas")
        print("6. Fin")

    def get_desired_analysis(self):
        """Gets the desired analysis from the user."""

        desiredAnalysis = input("Escriba la opción que desee: ")

        return desiredAnalysis

    def run_analysis(self, desiredAnalysis):
        """Runs the analysis desired by the user."""

        if desiredAnalysis == "1":
            self.wordanalysis.check_special_characters()
        elif desiredAnalysis == "2":
            self.wordanalysis.length()
            self.wordLengthInfo = self.wordanalysis.get_length_info()
        elif desiredAnalysis == "3":
            self.wordanalysis.check_silent_letters()
            self.silentInfo = self.wordanalysis.get_silent_letter_info()
        elif desiredAnalysis == "4":
            self.wordanalysis.check_same_sound_letter()
            self.sameSoundInfo = self.wordanalysis.get_same_sound_letter_info()
        elif desiredAnalysis == "5":
            self.wordanalysis.check_anagrams()
            self.anagramInfo = self.wordanalysis.get_anagrams_info()

    def get_file_name(self):
        """Aks the user for the name of the file with the words to be
        analyzed.
        """

        fileName = input("Escribe el nombre del documento con las palabras: ")

        return fileName

    def get_words(self, fileName):
        """ Get the words from the file specified by get_file_name."""

        iodata = iofiles.IOData()
        words = iodata.read_sequence(fileName)
        words = iodata.get_data()
        words = self.clean_words(words)

        return words

    def clean_words(self, words):
        """Eliminates empty strings from the word list (sometimes happens)."""

        words = [word.upper() for word in words]
        for word in words[:]:
            if word == "":
                words.remove(word)

        return words

    def export_to_csv(self):
        """Exports the information of the analyzed words into a csv file."""

        pass

wordanalysis = WordAnalysis()
end = input("press enter")
