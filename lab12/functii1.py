def product(a, b, ):
    """Calculate the product of a and b. """
    return a * b


def n_product(*args):
    p = 1
    for i in args:
        p *= i
    return p


print(n_product(1))
print(n_product(1, 2))
print(n_product(1, 2, 3))
