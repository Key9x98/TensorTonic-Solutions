def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    
    # result = 0.0
    # x = []
    # x.append(x0)
    # for i in range(steps):
    #     x.append(x[i] - lr * (2*a*x[i] + b))
    # return x[-1]
    
    x = x0
    
    for _ in range(steps):
        grad = 2 * a * x + b
        x = x - lr * grad
        
    return x