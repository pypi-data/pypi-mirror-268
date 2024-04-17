 ![Tests](https://github.com/RichtersFinger/data-plumber/actions/workflows/tests.yml/badge.svg?branch=main) ![PyPI - License](https://img.shields.io/pypi/l/data-plumber) ![GitHub top language](https://img.shields.io/github/languages/top/RichtersFinger/data-plumber) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/data-plumber) ![PyPI version](https://badge.fury.io/py/data-plumber.svg) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/data-plumber) 


# data-plumber
`data-plumber` is a lightweight but versatile python-framework for multi-stage information processing.
It allows to construct processing pipelines from both atomic building blocks and via recombination of existing pipelines.
Forks enable more complex (i.e. non-linear) orders of execution.
Pipelines can also be collected into arrays that can be executed at once with the same input data.

## Contents
1. [Usage Example](#usage-example)
1. [Install](#install)
1. [Documentation](#documentation)
1. [Changelog](CHANGELOG.md)

## Usage example
Consider a scenario where the contents of a dictionary have to be validated and a suitable error message has to be generated.
Specifically, a valid input-dictionary is expected to have a key "data" with the respective value being a list of integer numbers.
A suitable pipeline might look like this
```
>>> from data_plumber import Stage, Pipeline, Previous
>>> pipeline = Pipeline(
...   Stage(  # validate "data" is passed into run
...     primer=lambda **kwargs: "data" in kwargs,
...     status=lambda primer, **kwargs: 0 if primer else 1,
...     message=lambda primer, **kwargs: "" if primer else "missing argument"
...   ),
...   Stage(  # validate "data" is list
...     requires={Previous: 0},
...     primer=lambda data, **kwargs: isinstance(data, list),
...     status=lambda primer, **kwargs: 0 if primer else 1,
...     message=lambda primer, **kwargs: "" if primer else "bad type"
...   ),
...   Stage(  # validate "data" contains only int
...     requires={Previous: 0},
...     primer=lambda data, **kwargs: all(isinstance(i, int) for i in data),
...     status=lambda primer, **kwargs: 0 if primer else 1,
...     message=lambda primer, **kwargs: "validation success" if primer else "bad type in data"
...   ),
...   exit_on_status=1
... )
>>> pipeline.run().last_message
'missing argument'
>>> pipeline.run(data=1).last_message
'bad type'
>>> pipeline.run(data=[1, "2", 3]).last_message
'bad type in data'
>>> pipeline.run(data=[1, 2, 3]).last_message
'validation success'
```
See section "Examples" in [Documentation](#documentation) for more explanation.

## Install
Install using `pip` with
```
pip install data-plumber
```
Consider installing in a virtual environment.

## Documentation

* [Overview](docs/overview.md)
* [Pipeline](docs/pipeline.md)
* [Stage](docs/stage.md)
* [Fork](docs/fork.md)
* [StageRef](docs/stageref.md)
* [PipelineOutput](docs/output.md)
* [Pipearray](docs/array.md)
* [Examples](docs/examples.md)
