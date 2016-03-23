def naive_fib(n):
    """ The most obvious but insanely inefficient fibonacci algorithm.

    For n equal to 35, the program is already noticeably slow.

    For n equal to 50 there is a considerable wait.

    The algorithm hits the maximum recursion depth for python at around
    n = 99.
    """
    if n < 2:
        return n

    return naive_fib(n-1) + naive_fib(n-2)


def array_fib(n):
    """ Pretty fast but more memory intensive than the following algorithms """
    if n < 2:
        return n

    # create an array filled with almost all zeros
    a = [0] * (n + 1)
    a[1] = 1

    for i in xrange(2, n + 1):
        a[i] = a[i-1] + a[i-2]

    return a[n]


def tuple_swap_fib(n):
    """ Swaps values of a and b using tuples """
    if n < 2:
        return n

    a, b = 0, 1
    for _ in xrange(2, n + 1):
        a, b = b, a + b

    return b


def intermediate_var_swap_fib(n):
    """ Swaps values of a and b using a temp var """
    if n < 2:
        return n

    a = 0
    b = 1
    for _ in xrange(2, n + 1):
        tmp = b
        b = a + b
        a = tmp

    return b


def generator_fib(n):
    """ Uses a generator fibonacci sequence.

    This is just to show how it could be used. The only real
    practical situation to use a fib generator is if you don't
    know how many elements you want. Otherwise, using xrange as
    in the methods above, is just as memory-efficient.
    """
    if n < 2:
        return n

    def _gen_fib():
        a = 0
        b = 1
        while True:
            a, b = b, a + b
            yield b

    i = 2
    res = 1
    for x in _gen_fib():
        if i == n:
            res = x
            break
        i += 1

    return res


