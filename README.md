
# wdiff


  
[![PyPI - Version](https://img.shields.io/pypi/v/wdiff.svg)](https://pypi.python.org/pypi/wdiff)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wdiff.svg)](https://pypi.python.org/pypi/wdiff)
  
![GitHub](https://img.shields.io/github/license/mario-bermonti/wdiff)
[![Tests](https://github.com/mario-bermonti/wdiff/workflows/tests/badge.svg)](https://github.com/mario-bermonti/wdiff/actions?workflow=tests)
[![Codecov](https://codecov.io/gh/mario-bermonti/wdiff/branch/master/graph/badge.svg?token=YOURTOKEN)](https://codecov.io/gh/mario-bermonti/wdiff)
[![Read the Docs](https://readthedocs.org/projects/wdiff/badge/)](https://wdiff.readthedocs.io/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)


Analyze how difficult a Spanish word will be to spell


* GitHub repo: <https://github.com/mario-bermonti/wdiff.git>
* Documentation: <https://wdiff.readthedocs.io/>
* Free software: GNU General Public License v3


## Features

wdiff helps analyze how difficult it is to spell Spanish words. The objetive with wdiff is to improve research on spelling skill and may also be useful for games that require user's to spell Spanish words.

wdiff was design to be easy to use and as flexible as possible to facilitate conducting research on spelling skills.

wdiff determines the difficulty of words based on the following dimensions:

1.  Word length - how many letters it has
2.  Number of silent letters - letters that don't have a phonemic representation (e.g., *h*)
3.  Number of graphemes that share their phoneme with other graphemes (e.g., *s* and *z*)

## Getting Started
### Installation
`python -m pip install wdiff`

### Usage

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

Check [the documentation][project_docs] for more details.  **Better documentation is coming very soon!**

## Contributing to this project
  All contributions are welcome!

  Will find a detailed description of all the ways you can contribute to wdiff in
  [the contributing guide][contributing_guide].

  This is a beginner-friendly project so don't hesitate to ask any questions or get in touch
  with the project's maintainers.

  Please review the [project's code of conduct][code_conduct] before making
  any contributions.

## Author
  This project was developed by Mario E. Bermonti Pérez as part of
  his academic research. Feel free to contact me at [mbermonti@psm.edu](mailto:mbermonti@psm.edu) or 
  [mbermonti1132@gmail.com](mailto:mbermonti1132@gmail.com).

## Credits

This package was created with [Cookiecutter][cookiecutter] and the [mario-bermonti/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cookiecutter-modern-pypackage]: https://github.com/mario-bermonti/cookiecutter-modern-pypackage
[project_docs]: https://wdiff.readthedocs.io/
[code_conduct]: ./CODE_OF_CONDUCT.md
[contributing_guide]: ./contributing.md
