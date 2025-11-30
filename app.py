def get_max_min(num_list):
    max_val = max(num_list)
    min_val = min(num_list)
    return {'max': max_val, 'min': min_val}


def factorial(n):
    """Return the factorial of a non-negative integer n.

    Raises ValueError for non-integers or negative inputs.
    Implemented iteratively to avoid recursion limits.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be a non-negative integer')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def _run_demo():
    print('get_max_min demo:', get_max_min([1, 3, 5, 2, 4]))
    tests = {0: 1, 1: 1, 5: 120, 10: 3628800}
    for k, v in tests.items():
        print(f'factorial({k}) = {factorial(k)} (expected {v})')


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            print(f"{n}! =", factorial(n))
        except Exception as e:
            print('Error:', e)
    else:
        _run_demo()