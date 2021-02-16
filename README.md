- [wdiff](#sec-)
- [Getting Started](#sec-)
  - [Installing](#sec-)
  - [Usage](#sec-)
- [Contributing to this project](#sec-)
- [Author](#sec-)
- [License](#sec-)

# wdiff<a id="sec-"></a>

wdiff helps analyze how difficult it is to spell Spanish words. The objetive with wdiff is to improve research on spelling skill and may also be useful for games that require user's to spell Spanish words.

wdiff was design to be easy to use and as flexible as possible to facilitate conducting research on spelling skills.

wdiff determines the difficulty of words based on the following dimensions:

1.  Word length - how many letters it has
2.  Number of silent letters - letters that don't have a phonemic representation (e.g., *h*)
3.  Number of graphemes that share their phoneme with other graphemes (e.g., *s* and *z*)

# Getting Started<a id="sec-"></a>

## Installing<a id="sec-"></a>

`python -m pip install wdiff`

## Usage<a id="sec-"></a>

The most basic usage requires you to pass an iterable of words (e.g., list), run all possible analyses, and save the results to a file named `results.csv`.

```python
from wdiff.analyzer import Analyzer

words = ['guitarra', 'jinete', 'serpiente']
analyzer = Analyzer(words) # create analyzer
analyzer.run_all_analyses()
print(analyzer.results) # see results
analyzer.save_results()
```

You can further customize which analyses to run, extract the results as a `pandas.DataFrame`, and choose the name of the results file.

**Better documentation is coming very soon!**

# Contributing to this project<a id="sec-"></a>

If you encounter any bugs, please open an issue on github. To contribute to this project, clone the repository and submit a pull request. If you wish to become an active maintainer of the project, you can contact me at mbermonti1132@gmail.com

All contributions are welcome!

# Author<a id="sec-"></a>

This project was developed by Mario E. Bermonti-Pérez as part of his academic research. Feel free to contact me at [mbermonti@psm.edu](mailto:mbermonti@psm.edu) or [mbermonti1132@gmail.com](mailto:mbermonti1132@gmail.com)

# License<a id="sec-"></a>

This project is licensed under the GPL License. See the LICENSE.txt file for details.
