"""
Module contains fansy functions for data science.
Read documentation for more information.
"""

import numpy as np


def transpose2d(input_matrix: list[list[float]]) -> list:
    """Transpose input matrix (flips a matrix over its diagonal).

    Args:
        input_matrix: Matrix (2D array/list) of float numbers.

    Returns:
        Transposed matrix.

    Raises:
        ValueError: If input "matrix" has invalid shape.
    """

    for row in input_matrix[1:]:
        if len(row) != len(input_matrix[0]):
            raise ValueError("Invalid matrix")

    return [list(i) for i in zip(*input_matrix)]


def window1d(
    input_array: list | np.ndarray, size: int, shift: int = 1, stride: int = 1
) -> list[list | np.ndarray]:
    """Time Series Windowing.

    Applies Rolling-Window to initial input data to perform time-series analysis.

    Args:
        input_array: List or 1D Numpy array of real numbers.
        size: Positive integer that determines the size (length) of the window.
        shift: Positive integer that determines the shift (step size) between different windows.
        stride: Positive integer that determines the stride (step size) within each window.

    Returns:
        List of lists or 1D Numpy arrays of real numbers.

    Raises:
        ValueError: If `size`, `shift` or `stride` argument is not positive.
    """
    for param in (size, shift, stride):
        if param <= 0:
            raise ValueError(f"Value for size, shift, stride must be positive.")
    output_array = []
    for i in range(0, len(input_array) - size + 1, shift):
        output_array.append(input_array[i : i + size : stride])
    return output_array


def convolution2d(input_matrix: np.ndarray, kernel: np.ndarray, stride: int = 1) -> np.ndarray:
    """2-dimensional Convolution.

    Create two-dimensional convolutional layer from input data using cross-correlation operation.

    Args:
        input_matrix: input data, 2D Numpy array of real numbers.
        kernel: 2D Numpy array of real numbers.
        stride: integer that is greater than 0.

    Returns:
        2D Numpy array with resultin convolution matrix
    """
    # calculate output matrix size based on input and kernel size
    output_size = (
        ((input_matrix.shape[0] - kernel.shape[0]) // stride) + 1,
        ((input_matrix.shape[1] - kernel.shape[1]) // stride) + 1,
    )
    result = np.zeros((output_size[0], output_size[1]))

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            y_pos = i * stride
            x_pos = j * stride
            result[i, j] = (
                input_matrix[y_pos : (y_pos + kernel.shape[0]), x_pos : (x_pos + kernel.shape[1])]
                * kernel
            ).sum()
    return result
