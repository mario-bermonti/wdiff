#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import wanalysis


class TestWordAnalyzer():
    def test_check_length(self):
        """Tests the check_length method of the WordAnalyzer class. Values
        are 3 times the actual length because they are multipled by the
        difficulty index (3).
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
