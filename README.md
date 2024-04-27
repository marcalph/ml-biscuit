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
├── README.md           <- The top-level README
├── src                 <- Source code for use in this project.
│   └── utils           <- Generated graphics and figures to be used in reporting
└── tests               <- Source code for use in this project.
```
