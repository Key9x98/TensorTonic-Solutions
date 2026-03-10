import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    # result = 0.0
    # for i in range(len(x)):
    #     result += x[i] * p[i]

    x = np.array(x)
    p = np.array(p)
    if not np.allclose(np.sum(p), 1):
        raise ValueError("Probabilities must sum to 1")

    return np.sum(x*p)