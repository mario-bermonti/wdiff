#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import wanalysis


class TestWordAnalyzer():
    def test_check_length(self):
        """Tests the check_length method of the WordAnalyzer class. Values
        are 3 times the actual length because they are multipled by the
        difficulty index (in this case the default = 3).
        """
        words = {
            'gato': 12,
            'oso': 9,
            '': 0,
            'electroencefalografista': 69
        }
        analyzer = wanalysis.WordAnalyzer(words)

        analyzer.check_length()
        assert analyzer.get_length_info() == words

    def test_has_silent_h(self):
        """Tests the has_silent_h method."""

        words = {
            'hambre': 1,
            'oso': 0,
            'habichuela': 1  # Has 2 h but the second one changes the sound
        }
        analyzer = wanalysis.WordAnalyzer(words)

        for word in words:
            assert analyzer.has_silent_h(word) == words[word]

    def test_has_silent_u(self):
        """Tests the has_silent_u method."""

        words = {
            'guineo': 1,
            'guerra': 1,
            'ques': 1,
            'quine': 1,
            'gato': 0,
            'güiro': 0,
            'ungüento': 0,
        }
        analyzer = wanalysis.WordAnalyzer(words)

        for word in words:
            assert analyzer.has_silent_u(word) == words[word]

    def test_has_silent_letters(self):
        """Tests the has_silent_letters method."""

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

        analyzer = wanalysis.WordAnalyzer(words)

        for word in words:
            assert analyzer.has_silent_letters(word) == words[word]

    def test_check_silent_letters(self):
        """Tests the has_silent_letters method."""

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
        analyzer = wanalysis.WordAnalyzer(words)

        for word in words:
            assert analyzer.has_silent_letters(word) == words[word]

    def test_check_b_sound_swapping(self):
        """Tests the check_b_sound_swapping method."""

        words = {
            'absolver': 1,
            'observatorio': 1,
            # the following aren't words but serve as an example
            'vavebi': 2,
            'babevi': 2,
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.check_b_sound_swapping(word)

    def test_swap_g_for_j_check(self):
        """Tests swap_g_for_j_check."""

        words = {
            'gentil': 1,
            'girar': 1,
            'gato': 0,
            '': 0
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.swap_g_for_j_check(word)

    def test_check_j_sound(self):
        """Tests check_j_sound method."""

        # Uses nonwords that meet the specifications
        words = {
            'geje': 1,
            'jengibre': 1,
            'gegijije': 4,
            '': 0,
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.check_j_sound(word)

    def test_swap_c_for_s_check(self):
        """Tests swap_c_for_s_check method."""

        words = {
            'ceda': 1,
            'citronela': 1,
            'casa': 0,
            '': 0
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.swap_c_for_s_check(word)

    def test_check_s_sound(self):
        """Tests check_s_sound method."""

        # Uses nonwords that meet the specifications
        words = {
            'cese': 1,
            'cisi': 1,
            'sizice': 3,
            'zecese': 3,
            'zecuse': 1,
            'casa': 0,
            '': 0
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.check_s_sound(word)

    def test_swap_q_for_k_check(self):
        """Tests swap_q_for_k_check method."""

        # Uses nonwords that meet the specifications
        words = {
            'queso': 1,
            'quiero': 1,
            'queque': 2,
            'qi': 0,
            'casa': 0,
            '': 0
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.swap_q_for_k_check(word)

    def test_swap_c_for_k_check(self):
        """Tests swap_c_for_k_check method."""

        words = {
            'casa': 1,
            'cosa': 1,
            'coco': 2,
            'cocina': 1,
            'jaula': 0,
            '': 0
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.swap_c_for_k_check(word)

    def test_check_k_sound(self):
        """Tests check_k_sound method."""

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

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.check_k_sound(word)

    def test_swap_y_for_y_check(self):
        """Tests swap_y_for_y_check method."""

        words = {
            'carey': 0,
            'yeso': 1,
            'yautia': 1,
            '': 0
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.swap_y_for_y_check(word)

    def test_swap_l_for_y_check(self):
        """Tests swap_l_for_y_check method."""

        words = {
            'llanto': 1,
            'llollan': 2,
            'lamento': 0,
            'gato': 0,
            '': 0
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.swap_l_for_y_check(word)

    def test_check_y_sound(self):
        """Tests check_y_sound method."""

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

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.check_y_sound(word)

    def test_has_same_sound_letters(self):
        """Tests the has_same_sound_letters method."""

        # Uses nonwords that meet the specifications
        words = {
            'bota': 0,
            'bovasazeyollo': 3,
            'bovajigisazekocoyollo': 5,
            '': 0
        }

        analyzer = wanalysis.WordAnalyzer(words)
        for word in words.keys():
            assert words[word] == analyzer.has_same_sound_letters(word)

    def test_check_same_sound_letter(self):
        """Tests check_same_sound_letter method."""

        # Uses nonwords that meet the specifications
        words = {
            'bota': 0,
            'bovasazeyollo': 6,
            'bovajigisazekocoyollo': 10,
            '': 0
        }

        analyzer = wanalysis.WordAnalyzer(words)
        analyzer.check_same_sound_letter()
        assert analyzer.get_same_sound_letter_info() == words
