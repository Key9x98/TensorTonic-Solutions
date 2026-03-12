import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.sort(np.array(x))
    q = np.array(q)
    n = len(x)
    results = []

    for percentiles in q:
        pos = percentiles * (n - 1) / 100
        lower = int(np.floor(pos))
        upper = int(np.ceil(pos))
        print(pos)

        if lower == upper:
            value = x[lower]
        else:
            weight = pos - lower
            value = x[lower] + weight * (x[upper] - x[lower])
        results.append(value)
    return np.array(results)