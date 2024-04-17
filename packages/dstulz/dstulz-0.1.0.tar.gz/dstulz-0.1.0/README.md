# DS Tools (dstuzl)

Set of fancy tools (functions) for data science.

Currently it contains 3 functions:

* `transpose2d` - Transpose input matrix (flips a matrix over its diagonal).
* `window1d` - Time Series Windowing.
* `convolution2d` - 2-dimensional Convolution.


## Installation

Run this command in terminal (using virtual environment is highly recommended).

```bash
pip install dstulz
```

It will install `dstulz` package and all it's dependencies (currently `numpy` only).

## Usage

Library contains single package named `dstulz` with single module `dstulz`.

Import function from `dstulz` module and use it! 

```python
>>> from dstulz.dstulz import transpose2d

>>> input_matrix = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]]
>>> result = transpose2d(input_matrix)
>>> print(result)
... [[1.1, 4.4], [2.2, 5.5], [3.3, 6.6]]
```

See functions docstrings for more info.

## Testing

Install testing dependencies using `poetry`

```bash
poetry install
```

Run tests using `pytest`

```bash
pytest -v
```
