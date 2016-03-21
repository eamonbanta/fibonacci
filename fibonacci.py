def naive_fib(n):
    if n < 2:
        return n

    return naive_fib(n-1) + naive_fib(n-2)
