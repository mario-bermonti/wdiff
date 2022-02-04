# Contributing

Thank you for your interest in improving this project.

All contributions are welcome and greatly appreciated! Every little bit improves the
project and helps its users.

The following sections detail a variety of ways to contribute and how to get started.

Credit will always be given to the people making contributions.

If you do decide to work on an issue, please indicate so in a comment to the issue
so it's assigned to you and other people don't work on it simultaneously.

This is a beginner-friendly project so don't hesitate to write a comment in the issue you are
interested in if you have questions, would like to discuss some issue further, or you need help
in any way.

## Types of Contributions

### Spread the word
Tell others about your experience with wdiff. You can share it on social media and follow it on GitHub.

### Submit Feedback

The best way to send feedback is to file an issue at
 <https://github.com/mario-bermonti/wdiff/issues>.

Please let us know about your experience using wdiff. You can tell us about the things that you like, the things that can be improved, and the things that you would like wdiff to do.

If you are proposing a feature:

- How it would help you and other users (mainly researchers).
- Explain all the details of how it would work.
- Keep the scope as narrow as possible to make it easier to implement.
- Remember that this is a volunteer-driven project and for this reason it may not be feasible
  to implement the feature or it may take some time.

### Write Documentation

wdiff could always use more documentation. You can contribute to the documentation
by:
- Fixing typographical, grammatical, or spelling errors.
- Improving documentation that is unclear or incorrect.
- Creating or improving examples and tutorials.
- Writing blog posts, articles, and similar content that share how you are using this project and your best practices with us.

### Report Bugs
  You can report bugs at <https://github.com/mario-bermonti/wdiff/issues>.

  Please provide all the details that are asked when you create the issue to make sure
  it is understood correctly.

### Fix existing bugs

  Look through the GitHub issues for bugs. Anything tagged with \"bug\"
  and \"help wanted\" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
\"enhancement\" and \"help wanted\" is open to whoever wants to
implement it.

## Start contributing!

### Set up the development environment

Ready to contribute? Here\'s how to set up
wdiff in your local development environment.

You will need [Python 3.6+][download_python] installed.

1.  Fork the [wdiff repo][wdiff_gh] on GitHub.
2.  Clone your fork locally:

        git clone git@github.com:your_name_here/wdiff.git

3. We use `poetry` to manage dependencies. Install it with the following command.

        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

4.  Install the project, its dependencies, and the virtualenv:

         poetry install

5. Make sure everything is working properly before making any changes by running `poetry run invoke dev-tasks`.

### Development tasks (important side note)
In order to run anything inside the virtual environment every command has to be prefixed with `poetry run <command>`.

For example, to run python inside the virtual environment you would run `poetry run python`.

We have most of our development tasks pre-configured to run automatically with invoke.  :grin:

The most important tasks are:

| Command   | Description                |
|-----------|----------------------------|
| dev-tasks | Run all development tasks. |
| format    | Format code.               |
| tests     | Run tests.                 |
| coverage  | Create coverage report.    |
| lint      | Run all linting.           |
| mypy      | Run mypy.                  |
| docs      | Build documentation.       |
| clean     | Run all clean sub-tasks.   |



You can find see all the development tasks that pre-configured by running `poetry run invoke --list`.

### Making changes

#### Workflow

We work by protecting `master` branch and only merging changes that don't break existing functionality and are tested.

How do we do it?:

1. We identify something that must change
2. We create an issue on GitHub, if it doesn't already exist
3. We create a new branch named after the issue we want "fix" (`issue-$TASKNUMBER`)
4. We make changes and test everything works
5. Style the code
6. We then create a pull request to `master` branch that is reviewed and if approved, it is merged
   into `master`

This way we achieve an easy and scalable development process that avoids merge
conflicts and long-living branches.

In this method, the `master` branch always has the latest working version of the software, is stable,
and is working.

#### How to make changes

Follow this steps when working on changes to the project. Please see the `Workflow section` for
important details about making changes.

1.  Create a branch for local development. All the changes must be in this branch.

        $ git checkout -b name-of-your-bugfix-or-feature

2. Run the all checks to make sure everything is working before making
   any changes

        $ poetry run invoke dev-tasks

3. Add any changes you want
3. Add tests for the new changes
4. Run the tests and make sure they all pass

        $ poetry run invoke tests

4. Edit the documentation if appropriate (this is required for new features)
5. Make sure the changes to the documentation are correct and that the docs build

        $ poetry run invoke docs

6. Make sure everything is fine (e.g., tests, code style, coverage)

        $ poetry run invoke dev-tasks

   If you find that something is not working as expected, fix it, check that it is working appropriately
   by running the appropriate invoke command (see `Development tasks section`).

        $ poetry run invoke <command>

   After it is fixed, run all development tasks again

        $ poetry run invoke dev-tasks

7.  Commit your changes and push your branch to GitHub:

        $ git add .
        $ git commit

    wdiff follows specific guidelines for commit messages:

    - Make a reference to the relevant GitHub issues in your commit message (e.g., `Fix #1234`)
      We use imperative mood for commit messages (`fix x`, instead of `fixed x`).
      See [this commit guide][commit_guide]. A tip is to use a title for your commit message
      that completes "This commit will..." [Fix issue X].
    - The subject line should have < 80 chars
    - Leave one line blank
    - [Optional] Explain any relevant details or decisions made

8. Push your changes to GitHub

        $ git push origin name-of-your-bugfix-or-feature

9.  Submit a pull request through GitHub (see the `Pull Request Guidelines` section).

#### Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests for new functionality.
2.  If the pull request adds functionality, the docs should be updated.
3.  The pull request should pass all tests and must work for all the supported Python versions. It
    must also pass all checks in the GitHub CI.

Feel free to submit your pull request early so we can discuss it and iterate on the process.

### Tips

We really value your contributions and want to integrate your changes. The following are tips to
improve the probability that your changes are accepted.

- Make sure they don't break existing functionality
- Include tests for the changes you made
- Commit often
- Make small, easy to understand commits (i.e., atomic commits)
- Keep your changes in the narrowest scope possible (e.g., create tutorial for using the `X object`)
- It is recommended to open an issue before starting work on anything. This will allow a chance to
  talk it over with the maintainers and validate your approach.

## Releasing wdiff

Maintainers, please review [the guide for releasing new versions][release_guide]
of wdiff.


<!-- Credits -->
<!-- This file was developed based extensively on the contributing guides of many great projects: -->
<!-- https://github.com/briggySmalls/cookiecutter-pypackage/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/CONTRIBUTING.rst -->
<!-- https://github.com/pyjanitor-devs/pyjanitor/blob/dev/docs/CONTRIBUTION_TYPES.rst -->
<!-- https://github.com/cjolowicz/cookiecutter-hypermodern-python/blob/main/%7B%7Bcookiecutter.project_name%7D%7D/CONTRIBUTING.rst -->
<!-- https://github.com/wemake-services/wemake-python-package/blob/master/%7B%7Bcookiecutter.project_name%7D%7D/CONTRIBUTING.md -->
<!-- https://github.com/pandas-dev/pandas/blob/master/doc/source/development/contributing.rst#committing-your-code -->

[download_python]: https://www.python.org/downloads/
[wdiff_gh]: https://github.com/mario-bermonti/wdiff
[commit_guide]: https://chris.beams.io/posts/git-commit/
[release_guide]: ./release_guide.md
