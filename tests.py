#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import wdiff
import pandas as pd


class TestWordAnalyzerUnit():
    def test_determine_length_difficulty(self):
        """Tests the determine_length_difficulty method of the WordAnalyzer class. Values
        are 3 times the actual length because they are multipled by the
        difficulty index (in this case the default = 3).
        """

        words = {
            'gato': 12,
            'oso': 9,
            '': 0,
            'electroencefalografista': 69
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        analyzer.determine_length_difficulty()
        assert analyzer.get_length_info() == words

    def test_count_silent_h(self):
        """Tests the count_silent_h method."""

        words = {
            'hambre': 1,
            'oso': 0,
            'habichuela': 1  # Has 2 h but the second one changes the sound
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words:
            assert analyzer.count_silent_h(word) == words[word]

    def test_count_silent_u(self):
        """Tests the count_silent_u method."""

        words = {
            'guineo': 1,
            'guerra': 1,
            'ques': 1,
            'quine': 1,
            'gato': 0,
            'güiro': 0,
            'ungüento': 0,
        }
        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)

        for word in words:
            assert analyzer.count_silent_u(word) == words[word]

    def test_count_swappable_b_sounds(self):
        """Tests the count_swappable_b_sounds method."""

        words = {
            'absolver': 1,
            'observatorio': 1,
            # the following aren't words but serve as an example
            'vavebi': 2,
            'babevi': 2,
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_swappable_b_sounds(word)

    def test_count_g_with_j_sound(self):
        """Tests count_g_with_j_sound."""

        words = {
            'gentil': 1,
            'girar': 1,
            'gato': 0,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_g_with_j_sound(word)

    def test_count_swappable_j_sounds(self):
        """Tests count_swappable_j_sounds method."""

        # Uses nonwords that meet the specifications
        words = {
            'geje': 1,
            'jengibre': 1,
            'gegijije': 4,
            '': 0,
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_swappable_j_sounds(word)

    def test_count_c_with_s_sound(self):
        """Tests count_c_with_s_sound method."""

        words = {
            'ceda': 1,
            'citronela': 1,
            'casa': 0,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_c_with_s_sound(word)


    def test_count_q_with_k_sound(self):
        """Tests count_q_with_k_sound method."""

        # Uses nonwords that meet the specifications
        words = {
            'queso': 1,
            'quiero': 1,
            'queque': 2,
            'qi': 0,
            'casa': 0,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_q_with_k_sound(word)

    def test_count_c_with_k_sound(self):
        """Tests count_c_with_k_sound method."""

        words = {
            'casa': 1,
            'cosa': 1,
            'coco': 2,
            'cocina': 1,
            'jaula': 0,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_c_with_k_sound(word)

    def test_count_swappable_k_sounds(self):
        """Tests count_swappable_k_sounds method."""

        # Uses nonwords that meet the specifications
        words = {
            'queso': 0,
            'quiero': 0,
            'cosa': 0,
            'coco': 0,
            'cocina': 0,
            'quicoka': 3,
            'quecaki': 3,
            'cacique': 1,
            'kacuci': 1,
            'jaula': 0,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_swappable_k_sounds(word)

    def test_count_y_with_ll_sound(self):
        """Tests count_y_with_ll_sound method."""

        words = {
            'carey': 0,
            'yeso': 1,
            'yautia': 1,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_y_with_ll_sound(word)

    def test_count_l_with_ll_sound(self):
        """Tests count_l_with_ll_sound method."""

        words = {
            'llanto': 1,
            'llollan': 2,
            'lamento': 0,
            'gato': 0,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_l_with_ll_sound(word)

    def test_count_swappable_ll_sounds(self):
        """Tests count_swappable_ll_sounds method."""

        # Uses nonwords that meet the specifications
        words = {
            'llanto': 0,
            'llollan': 0,
            'lamento': 0,
            'carey': 0,
            'carelley': 0,
            'galleyo': 1,
            'belloyo': 1,
            'galloyollo': 2,
            'gato': 0,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.count_swappable_ll_sounds(word)


    def test_count_anagrams(self):
        """Tests the count_anagram method."""

        words = {
            '': 1,
            'tu': 1,
            'fresa': 2,
            'frase': 2,
            'arma': 3,
            'rama': 3,
            'amar': 3,
            'acre': 4,
            'caer': 4,
            'cera': 4,
            'crea': 4
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(list(words.keys()))
        for word in words:
            assert analyzer.count_anagrams(word) == words[word]

    def test_determine_anagrams_difficulty(self):
        """Tests the check_anagram method."""

        words = {
            '': 0,
            'tu': 0,
            'fresa': 2,
            'frase': 2,
            'arma': 3,
            'rama': 3,
            'amar': 3,
            'acre': 4,
            'caer': 4,
            'cera': 4,
            'crea': 4
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(list(words.keys()))
        analyzer.determine_anagrams_difficulty()
        assert words == analyzer.get_anagrams_info()


class TestWordAnalyzerIntegration:
    def test_determine_total_silent_letters(self):
        """Tests the determine_total_silent_letters method."""

        words = {
            'guineo': 1,
            'guerra': 1,
            'ques': 1,
            'quine': 1,
            'gato': 0,
            'güiro': 0,
            'ungüento': 0,
            'hambre': 1,
            'oso': 0,
            'habichuela': 1,  # Has 2 h but the second one changes the sound
            'hoguera': 2,
            'riachuelo': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)

        for word in words:
            assert analyzer.determine_total_silent_letters(word) == words[word]

    def test_determine_silent_letter_difficulty(self):
        """Tests the determine_total_silent_letters method."""

        words = {
            'guineo': 1,
            'guerra': 1,
            'queso': 1,
            'quine': 1,
            'gato': 0,
            'güiro': 0,
            'ungüento': 0,
            'hambre': 1,
            'oso': 0,
            'habichuela': 1,  # Has 2 h but the second one changes the sound
            'hoguera': 2,
            'riachuelo': 0
        }
        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)

        for word in words:
            assert analyzer.determine_total_silent_letters(word) == words[word]

    def test_determine_total_same_sound_letters(self):
        """Tests the determine_total_same_sound_letters method."""

        # Uses nonwords that meet the specifications
        words = {
            'bota': 0,
            'bovasazeyollo': 3,
            'bovajigisazekocoyollo': 5,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        for word in words.keys():
            assert words[word] == analyzer.determine_total_same_sound_letters(word)

    def test_determine_same_sound_letter_difficulty(self):
        """Tests determine_same_sound_letter_difficulty method."""

        # Uses nonwords that meet the specifications
        words = {
            'bota': 0,
            'bovasazeyollo': 6,
            'bovajigisazekocoyollo': 10,
            '': 0
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(words)
        analyzer.determine_same_sound_letter_difficulty()
        assert analyzer.get_same_sound_letter_info() == words

    def test_integrate_word_information_all_analysis(self):
        """Tests integrate_word_information method when all analysis
        conducted.
        """

        words = {
            '': [0, 0, 0, 0],
            'hguicokocese': [36, 4, 4, 0],
            'hgui': [12, 4, 0, 0]
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(list(words.keys()))
        analyzer.determine_length_difficulty()
        analyzer.determine_silent_letter_difficulty()
        analyzer.determine_same_sound_letter_difficulty()
        analyzer.determine_anagrams_difficulty()
        word_info = analyzer.integrate_word_information()

        assert words == word_info

    def test_integrate_word_information_some_analysis(self):
        """Tests integrate_word_information method when some analysis
        conducted.
        """

        words = {
            '': [0, 0, 0],
            'hguicokocese': [36, 4, 0],
            'hgui': [12, 0, 0]
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(list(words.keys()))
        analyzer.determine_length_difficulty()
        analyzer.determine_same_sound_letter_difficulty()
        analyzer.determine_anagrams_difficulty()
        word_info = analyzer.integrate_word_information()

        assert words == word_info

    def test_determine_total_difficulty_index(self):
        """Tests determine_total_difficulty_index method."""

        words = {
            '': [0, 0, 0, 0, 0],
            'hguicokocese': [36, 4, 4, 0, 44],
            'hgui': [12, 4, 0, 0, 16]
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(list(words.keys()))
        analyzer.determine_length_difficulty()
        analyzer.determine_silent_letter_difficulty()
        analyzer.determine_same_sound_letter_difficulty()
        analyzer.determine_anagrams_difficulty()
        analyzer.determine_total_difficulty_index()

        assert words == analyzer.get_word_difficulty()


class TestSaveResults():
    def test_save_results(self):
        """Tests the save_results method."""

        data = {
            '': [0, 0, 0, 0, 0],
            'hguicokocese': [36, 4, 4, 0, 44],
            'hgui': [12, 4, 0, 0, 16]
        }

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(list(data.keys()))
        analyzer.determine_length_difficulty()
        analyzer.determine_silent_letter_difficulty()
        analyzer.determine_same_sound_letter_difficulty()
        analyzer.determine_anagrams_difficulty()
        analyzer.determine_total_difficulty_index()
        analyzer.save_results('results_test.csv')
        results_saved = pd.read_csv('results_test.csv', index_col=0, keep_default_na=False)
        import os
        os.remove('results_test.csv')

        results_expected = pd.DataFrame(
            list(data.values()),
            index=list(data.keys()),
            columns=[
                'length_difficulty', 'silent_letter_difficulty', 'same_sound_difficulty', 'anagrams_difficulty', 'total difficulty']
        )

        assert results_expected.equals(results_saved)

    def test_format_all_analysis(self):
        """Tests the format_data method with all analysis conducted."""

        data = {
            '': [0, 0, 0, 0, 0],
            'hguicokocese': [36, 4, 4, 0, 44],
            'hgui': [12, 4, 0, 0, 16]
        }

        formattedDataExpected = pd.DataFrame(
            list(data.values()),
            index=list(data.keys()),
            columns=[
                'length_difficulty', 'silent_letter_difficulty', 'same_sound_difficulty', 'anagrams_difficulty', 'total difficulty']
        )

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(list(data.keys()))
        analyzer.determine_length_difficulty()
        analyzer.determine_silent_letter_difficulty()
        analyzer.determine_same_sound_letter_difficulty()
        analyzer.determine_anagrams_difficulty()
        analyzer.determine_total_difficulty_index()
        formattedData = analyzer.format_data()

        assert formattedData.equals(formattedDataExpected)

    def test_format_some_analysis(self):
        """Tests the format_data method with just some analysis conducted ."""

        data = {
            '': [0, 0, 0, 0],
            'hguicokocese': [36, 4, 0, 40],
            'hgui': [12, 0, 0, 12]
        }

        formattedDataExpected = pd.DataFrame(
            list(data.values()),
            index=list(data.keys()),
            columns=[
                'length_difficulty', 'same_sound_difficulty', 'anagrams_difficulty', 'total difficulty']
        )

        analyzer = wdiff.WordAnalyzer()
        analyzer.set_words(list(data.keys()))
        analyzer.determine_length_difficulty()
        analyzer.determine_same_sound_letter_difficulty()
        analyzer.determine_anagrams_difficulty()
        analyzer.determine_total_difficulty_index()
        formattedData = analyzer.format_data()

        assert formattedDataExpected.equals(formattedData)
