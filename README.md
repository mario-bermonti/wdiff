
# Table of Contents

-   [Word Analysis](#org5a5bbc3)
-   [Getting Started](#org35423b7)
    -   [Prerequisites](#org0671de2)
    -   [Installing](#org8aff58e)
    -   [Usage](#org78b2984)
-   [Contributing to this project](#orgb502f60)
-   [Author](#orgbb7d417)
-   [License](#orgd03237e)


<a id="org5a5bbc3"></a>

# Word Analysis

This modules has a set of functions to analyze Spanish words and determine
their difficulty level based on the following dimensions:

1.  Word length
2.  Number of silent letters
3.  Number of different letters with the same sound: e.g., *s* and *z*
4.  Number of anagrams: words that can be made with its letters


<a id="org35423b7"></a>

# Getting Started


<a id="org0671de2"></a>

## Prerequisites

You will need to install the pandas package to be able to use this
module. To install it use `pip install pandas`.


<a id="org8aff58e"></a>

## Installing

`pip install wdiff`


<a id="org78b2984"></a>

## Usage

    import wdiff
    words = ['perro', 'gato', 'serpiente']
    wanalyzer = wdiff.WordAnalyzer()
    wanalyzer.set_words(words)
    wanalyzer.determine_length_difficulty(difficultyWeight=1)
    wanalyzer.determine_silent_letter_difficulty(difficultyWeight=1)
    wanalyzer.determine_same_sound_letter_difficulty(difficultyWeight=1)
    wanalyzer.determine_anagrams_difficulty(difficultyWeight=1)
    wanalyzer.determine_total_difficulty_index()
    wanalyzer.save_results()

Results will be saved in the current directory as a CSV file.


<a id="orgb502f60"></a>

# Contributing to this project

  If you encounter any bugs, please open an issue on github. To contribute to
this project, clone the repository and submit a pull request. If you wish to
become an active maintainer of the project, you can contact me
at mbermonti1132@gmail.com

All contributions are welcome!


<a id="orgbb7d417"></a>

# Author

Mario E. Bermonti-Perez. Feel free to contact me at mbermonti1132@gmail.com.


<a id="orgd03237e"></a>

# License

This project is licensed under the GPL License. See the LICENSE.txt file for
details.

