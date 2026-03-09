import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    input = np.asarray(x, dtype=float)
    result = 1 / (1 + np.exp(-input))
    return result