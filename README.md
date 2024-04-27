# ML biscuit

A standardized (python only) ML project template with boilerplate code compliant with my OCDs - currently WIP, should be moved to a templating tool (e.g. cookiecutter) instead of the current copy/paste logic.

### required tooling

My opinionated hot take on what a python project should leverage as tooling encompasses:
- a packaging tool, here `poetry` 
- a minimal local ci-suite, here inmplemented using `pre-commit`

### directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── nb                 <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump. TODO(marcalph): default to lfs│
├── models             <- Trained and serialized models, model predictions, or model summaries
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-marcalph-initial-data-exploration`.│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figs           <- Generated graphics and figures to be used in reporting
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
└── src                <- Source code for use in this project.│   │
```
