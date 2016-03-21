def naive_fib(n):
    if n < 2:
        return n

    return naive_fib(n-1) + naive_fib(n-2)


def array_fib(n):
    if n < 2:
        return n

    # create an array filled with almost all zeros
    a = [0] * (n + 1)
    a[1] = 1

    for i in xrange(2, n + 1):
        a[i] = a[i-1] + a[i-2]

    return a[n]


def tuple_swap_fib(n):
    if n < 2:
        return n

    a, b = 0, 1
    for _ in xrange(2, n + 1):
        a, b = b, a + b

    return b
