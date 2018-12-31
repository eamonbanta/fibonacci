import sys

import fibonacci


VALID_CHOICES = ('q', 'n', 'a', 't', 'i', 'g')
VALID_CHOICE_NAMES = [
    '(q)uit',
    '(n)aive (very slow for n > 40, exceeds recursion limit near n == 100)',
    '(a)rray',
    '(t)uple swap',
    '(i)ntermediate var swap',
    '(g)enerator',
]

CHOICE_TO_METHOD = {
    'n': fibonacci.naive_fib,
    'a': fibonacci.array_fib,
    't': fibonacci.tuple_swap_fib,
    'i': fibonacci.intermediate_var_swap_fib,
    'g': fibonacci.generator_fib,
}


def print_choice_list():
    print "Possible choices are:"
    for choice in VALID_CHOICE_NAMES:
        print choice


def main():

    return 0


if __name__ == "__main__":
    sys.exit(main())
